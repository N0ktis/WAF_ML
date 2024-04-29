import re
from typing import Dict, List, Optional, Tuple

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

from src.analytics_module.config import Config


class LLM_AnalyticsClass:
    """
    Class for analysing HTTP-requests with LLM
    """

    def __init__(self) -> None:
        """
        Init neccessasry attributes and config
        """
        self.config = Config()
        self.model: AutoModelForCausalLM
        self.tokenizer: AutoTokenizer
        self.pipeline: pipeline
        self.system_prompt: str
        self.user_prompt: str

        self.__init_artifacts()
        self.__init_pipeline()

    def __init_artifacts(self) -> None:
        """
        Init system and user prompts from .txt files
        """
        with open(self.config.user_prompt_path) as user_prompt_file:
            self.user_prompt = user_prompt_file.read()

        with open(self.config.system_prompt_path) as system_prompt_file:
            self.system_prompt = system_prompt_file.read()

    def __init_pipeline(self) -> None:
        """
        Init model tokenizer and pipleine.
        Inference device detected automaticly depends on installed CUDA version
        """
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.config.prod_model, trust_remote_code=True
        )
        # self.model = AutoModelForCausalLM.from_pretrained(
        #     self.config.codellama_13b_gptq,
        #     torch_dtype=torch.bfloat16,
        #     trust_remote_code=True,
        # )
        self.pipeline = pipeline(
            "text-generation",
            model=self.config.prod_model,
            tokenizer=self.tokenizer,
            torch_dtype=torch.float16,
            device_map="auto",
            trust_remote_code=True,
            # device=1,
        )

    def __check_answer_template(self, answer: str) -> bool:
        """
        Checks if LLM answer matchs answer template wich was declared in user's prompt

        Args:
            answer (str): answer from LLM

        Returns:
            bool: True - answer matchs tempplate, Flase - otherwise
        """
        if re.match(self.config.answer_template, answer):
            return True
        else:
            return False

    def __get_prompt(self, user_data: str) -> List[Dict[str, str]]:
        """
        Generate prompt in correct format for LLM

        Args:
            user_data (str): data which should be inserted in final prompt

        Returns:
            List[Dict[str, str]]: final prompt for LLM
        """
        messages = [
            {
                "role": "system",
                "content": self.system_prompt,
            },
            {"role": "user", "content": f"'''{user_data}'''\n{self.user_prompt}"},
        ]

        return messages

    def generate(self, msg: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Put prompt to model ang generate answer

        Args:
            msg (List[Dict[str,str]]): input prompt for LLM

        Returns:
            List[Dict[str, str]]: input prompt for LLM with answer from LLM
        """
        result = self.pipeline(
            msg,
            max_new_tokens=5,
            do_sample=True,
            use_cache=False,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
        )
        return result

    def pred(self, input_data: str) -> Tuple[Optional[int], int]:
        """
        Predict anomaly of input HTTP-request

        Args:
            input_data (str): HTTP-request

        Returns:
            Optional[str]: binary class of HTTP-request
        """

        msg = self.__get_prompt(input_data)

        for i in range(self.config.n_tries):

            gen = self.generate(msg)
            prediction = gen[0]["generated_text"][2]["content"]  # type: ignore
            prediction = "".join(prediction.lower().split())

            if self.__check_answer_template(prediction):
                if prediction[0][1:-1]=='no':
                    return 0, i
                else:
                    return 1, i

        return None, i
