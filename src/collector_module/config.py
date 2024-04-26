from pathlib import Path
from typing import Optional


class Config:
    """
    Configuration for collector module
    """

    modul_name: str = "Collector"

    CA_cert_dir: Optional[str] = "/etc/ssl/certs/"
    random_seed = 2077  # cyberpunk
    host: str = "127.0.0.1"
    port: int = 8888

    @property
    def cert_file_path(self) -> Path:
        """Return CA cert directory path."""
        return Path(f"{self.CA_cert_dir}")
