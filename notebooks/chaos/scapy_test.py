from scapy.layers.http import HTTP  # read the doc
from scapy.sendrecv import sniff

sniff(lfilter=lambda x: HTTP in x, prn=lambda x: x.summary())
