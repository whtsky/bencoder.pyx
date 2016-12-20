# -*- coding: utf-8 -*-

from bencoder import bdecode
import os
import sys

TORRENT_PATH = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    "debian-8.3.0-amd64-netinst.iso.torrent"
)


def test_decode_str(benchmark):
    assert benchmark(bdecode, b'6:WWWWWW') == b"WWWWWW"


def test_decode_int(benchmark):
    assert benchmark(bdecode, b'i233e') == 233


def test_decode_large_int(benchmark):
    assert bdecode(b'i1455189890e') == 1455189890
    assert bdecode(b'i25735241490e') == 25735241490

    MAX_SIZE = sys.maxsize + 1
    BENCODED_MAXSIZE = ('i{0:d}e'.format(MAX_SIZE)).encode()
    assert benchmark(bdecode, BENCODED_MAXSIZE) == MAX_SIZE


def test_decode_list(benchmark):
    assert benchmark(bdecode, b'l1:a1:bi3ee') == [b'a', b'b', 3]


def test_decode_dict(benchmark):
    od = dict()
    od[b'ka'] = b'va'
    od[b'kb'] = 2
    assert benchmark(bdecode, b'd2:ka2:va2:kbi2ee') == od


def test_ordered_dict(benchmark):
    from bencoder import OrderedDict
    rv = benchmark(bdecode, b'd2:ka2:va2:kbi2ee')
    assert isinstance(rv, OrderedDict)
    assert list(rv.keys()) == [b'ka', b'kb']
    assert list(bdecode(b'd2:kc2:va2:kei2ee').keys()) == [b'kc', b'ke']
    assert list(bdecode(b'd2:ke2:va2:kci2ee').keys()) == [b'ke', b'kc']


def test_encode_complex():
    od = dict()
    od[b'KeyA'] = [b'listitemA', {b'k': b'v'}, 3]
    od[b'KeyB'] = {b'k': b'v'}
    od[b'KeyC'] = 3
    od[b'KeyD'] = b'AString'
    expected_result = b'd4:KeyAl9:listitemAd1:k1:vei3ee4:KeyBd1:k1:ve4:KeyCi3e4:KeyD7:AStringe'
    assert bdecode(expected_result) == od


def test_decode_debian_torrent():
    with open(TORRENT_PATH, "rb") as f:
        torrent = bdecode(f.read())
    assert torrent[b'announce'] == b'http://bttracker.debian.org:6969/announce'
    assert torrent[b'comment'] == b'"Debian CD from cdimage.debian.org"'
