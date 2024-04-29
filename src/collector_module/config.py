from pathlib import Path
from typing import Optional

from src.base_config import BaseConfig


class Config(BaseConfig):
    """
    Configuration for collector module
    """

    module_name: str = "Collector"

    CA_cert_dir: Optional[str] = "/etc/ssl/certs/"
    host: str = "127.0.0.1"
    port: int = 8888

    @property
    def cert_file_path(self) -> Path:
        """Return CA cert directory path."""
        return Path(f"{self.project_root}{self.CA_cert_dir}")
