from pathlib import Path

from mitm import MITM, crypto, middleware, protocol

from src.collector_module.config import Config


class Collector:
    def __init__(self) -> None:
        self.config = Config()
        self.server: MITM

        self.__run_proxy_server()

    def __run_proxy_server(self) -> None:
        if self.config.cert_file_path is not None:
            path = Path(self.config.cert_file_path)
            certificate_authority = crypto.CertificateAuthority.init(path=path)
        else:
            certificate_authority = crypto.CertificateAuthority()

        self.server = MITM(
            host=self.config.host,
            port=self.config.port,
            protocols=[protocol.HTTP],
            middlewares=[middleware.Log],
            certificate_authority=certificate_authority,
        )

        self.server.run()

    def get_request(self) -> str:
        return ""
