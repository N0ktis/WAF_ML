from pathlib import Path
from typing import Optional


class Config:
    """
    Configuration for decision module
    """

    modul_name: str = "Decision"

    model_dir: Optional[str] = "./model"
    prompts_dir: str = "./prompts/"
    random_seed = 2077  # cyberpunk
    context_lenght: int = 16_000
    n_tries: int = 3
    # answer_template: str

    @property
    def system_prompt_path(self) -> Path:
        """Return path to file with system prompt"""
        return Path(f"{self.prompts_dir}s_prompt.txt")

    @property
    def user_prompt_path(self) -> Path:
        """Return path to file with user prompt"""
        return Path(f"{self.prompts_dir}u_prompt.txt")
