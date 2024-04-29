from pathlib import Path
from typing import Optional


class BaseConfig:
    """
    Base configuration for project
    """
    project_name: str = "WAF_ML"
    random_seed = 2077  # cyberpunk
    project_root = str(Path(__file__).parent.parent)