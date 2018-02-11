# -*- coding: utf-8 -*-

from bencoder import bencode, bdecode
import os
import sys

TORRENT_PATH = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    "debian-8.3.0-amd64-netinst.iso.torrent"
)


def test_encode_str():
    assert bencode("WWWWWW") == b'6:WWWWWW'


def test_encode_int():
    assert bencode(233) == b'i233e'


def test_encode_large_int():
    assert bencode(1455189890) == b'i1455189890e'
    assert bencode(25735241490) == b'i25735241490e'
    MAX_SIZE = sys.maxsize + 1
    BENCODED_MAXSIZE = ('i%de' % MAX_SIZE).encode()

    assert bencode(MAX_SIZE) == BENCODED_MAXSIZE


def test_encode_bytes():
    b = b"TheseAreSomeBytes"
    coded = bencode(b)
    l = str(len(b)).encode()
    assert coded == l + b':' + b


def test_encode_string():
    b = "TheseAreSomeString"
    coded = bencode(b)
    l = str(len(b))
    assert coded == (l + ':' + b).encode()


def test_encode_list():
    assert bencode(['a', 'b', 3]) == b'l1:a1:bi3ee'


def test_encode_tuple():
    assert bencode(('a', 'b', 3)) == b'l1:a1:bi3ee'


def test_encode_true():
    assert bencode(True) == bencode(1)


def test_encode_false():
    assert bencode(False) == bencode(0)


def test_encode_dict():
    od = dict()
    od['ka'] = 'va'
    od['kb'] = 2
    assert bencode(od) == b'd2:ka2:va2:kbi2ee'


def test_encode_dict_subclass():
    class AAA(dict):
        pass

    od = AAA()
    od['ka'] = 'va'
    od['kb'] = 2
    assert bencode(od) == b'd2:ka2:va2:kbi2ee'


def test_encode_complex():
    od = dict()
    od['KeyA'] = ['listitemA', {'k': 'v'}, 3]
    od['KeyB'] = {'k': 'v'}
    od['KeyC'] = 3
    od['KeyD'] = 'AString'
    expected_result = b'd4:KeyAl9:listitemAd1:k1:vei3ee4:KeyBd1:k1:ve4:KeyCi3e4:KeyD7:AStringe'
    assert bencode(od) == expected_result


def test_infohash():
    import hashlib
    with open(TORRENT_PATH, "rb") as f:
        torrent = bdecode(f.read())
    infohash = hashlib.sha1(bencode(torrent[b'info'])).hexdigest()
    assert infohash == "4194e473d6c49630e1c6247d6716076809bb96ae"
