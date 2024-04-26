# from pathlib import Path

from mitm import MITM, crypto, middleware, protocol

# path = Path("/etc/ssl/certs")
# certificate_authority = crypto.CertificateAuthority.init(path=path)

mitm = MITM(
    host="127.0.0.1",
    port=8888,
    protocols=[protocol.HTTP],
    middlewares=[middleware.Log],
    # certificate_authority = certificate_authority
    certificate_authority=crypto.CertificateAuthority(),
)

# os.environ['REQUESTS_CA_BUNDLE'] = '/home/azhurin/.local/share/mitm/mitm.pem'


mitm.run()

# PosixPath('/home/azhurin/.local/share/mitm')
