from typing import Dict, List, Optional

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from src.decision_module.config import Config


class Decision:
    def __init__(self) -> None:
        self.tokenizer: AutoTokenizer
        self.model: AutoModelForCausalLM
        self.config = Config()
        self.system_prompt: str
        self.user_prompt: str

        self.__init_model()
        self.__init_prompts()

    def __init_prompts(self) -> None:
        with open(self.config.system_prompt_path) as system_f:
            self.system_prompt = system_f.read()

        with open(self.config.user_prompt_path) as user_f:
            self.user_prompt = user_f.read(0)

    def __init_model(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.config.model_dir, trust_remote_code=True
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            self.config.model_dir, torch_dtype=torch.bfloat16, trust_remote_code=True
        )

        self.model.eval()
        self.model = self.model.cuda()

    def __check_template(self, answer: str) -> bool:
        return True

    def __set_prompt(self, user_data: str) -> List[Dict[str, str]]:

        messages = [
            {
                "role": "system",
                "content": self.system_prompt,
            },
            {"role": "user", "content": f"{self.user_prompt} {user_data}"},
        ]

        return messages

    def pred(self, input_data: str) -> Optional[str]:

        msg = self.__set_prompt(input_data)

        prompt = self.tokenizer.apply_chat_template(
            msg, add_generation_prompt=True, tokenize=False
        )

        inputs = self.tokenizer([prompt], return_tensors="pt").to(self.model.device)

        for _ in range(self.config.n_tries):

            tokens = self.model.generate(
                **inputs,
                max_new_tokens=1024,
                temperature=0.5,
                top_p=0.95,
                top_k=100,
                do_sample=True,
                use_cache=True,
            )

            output = self.tokenizer.batch_decode(
                tokens[:, inputs.input_ids.shape[-1] :], skip_special_tokens=False
            )[0]

            if self.__check_template(output):
                return output

        return None
