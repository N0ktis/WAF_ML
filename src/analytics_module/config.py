from pathlib import Path

from src.base_config import BaseConfig


class Config(BaseConfig):
    """
    Configuration for decision module
    """

    module_name: str = "Decision"

    models: str = ".\\models\\"
    data: str = ".\\data\\"
    prompts_dir: str = ".\\prompts\\"
    context_lenght: int = 16_000
    n_tries: int = 3
    answer_template: str = r"{(yes|no)}"

    @property
    def data_file_path(self) -> Path:
        return Path(f"{self.data}http_data.parquet")

    @property
    def system_prompt_path(self) -> Path:
        """Return path to file with system prompt"""
        return Path(f"{self.prompts_dir}s_prompt.txt")

    @property
    def user_prompt_path(self) -> Path:
        """Return path to file with user prompt"""
        return Path(f"{self.prompts_dir}u_prompt.txt")

    @property
    def prod_model(self) -> Path:
        return self.stable_Code_Instruct_3B

    # @property
    # def codellama_13b_gptq(self) -> Path:
    #     return Path(f"{self.models}CodeLlama_13B_GPTQ\\")

    # @property
    # def llama_3_8B_Instruct_GPTQ_8_Bit(self) -> Path:
    #     return Path(f"{self.models}Llama_3_8B_Instruct_GPTQ_8_Bit\\")

    # @property
    # def Yi_34B_200K_Rawrr1_LORA_DPO_Experimental_R3(self) -> Path:
    #     return Path(f"{self.models}Yi_34B_200K_Rawrr1_LORA_DPO_Experimental_R3\\")

    @property
    def codellama_13b_gptq(self) -> Path:
        return Path(f"{self.models}CodeLlama_13B_GPTQ\\")

    @property
    def phillama_3_8b_v0_1(self) -> Path:
        return Path(f"{self.models}phillama_3.8b_v0.1\\")

    @property
    def phi_3_mini_4k_instruct(self) -> Path:
        return Path(f"{self.models}Phi_3_mini_4k_instruct\\")

    @property
    def neuralMonarch_7B_GPTQ(self) -> Path:
        return Path(f"{self.models}NeuralMonarch_7B_GPTQ\\")

    @property
    def stable_Code_Instruct_3B(self) -> Path:
        return Path(f"{self.models}Stable_Code_Instruct_3B\\")

    # @property
    # def pastiche_crown_clown_7b_dare_awq(self) -> Path:
    #     return Path(f"{self.models}pastiche_crown_clown_7b_dare_awq\\")
