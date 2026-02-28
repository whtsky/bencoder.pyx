import pathlib

from bencoder import bdecode, bencode


class TimeCodec:
    def setup(self):
        project_root = pathlib.Path(__file__).resolve().parents[1]
        torrent_path = project_root / "tests" / "debian-8.3.0-amd64-netinst.iso.torrent"
        self.encoded = torrent_path.read_bytes()
        self.payload = bdecode(self.encoded)

    def time_bencode(self):
        bencode(self.payload)

    def time_bdecode(self):
        bdecode(self.encoded)
