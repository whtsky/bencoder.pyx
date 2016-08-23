# cython: language_level=3

# The contents of this file are subject to the BitTorrent Open Source License
# Version 1.1 (the License).  You may not copy or use this file, in either
# source code or executable form, except in compliance with the License.  You
# may obtain a copy of the License at http://www.bittorrent.com/license/.
#
# Software distributed under the License is distributed on an AS IS basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied.  See the License
# for the specific language governing rights and limitations under the
# License.

# Based on https://github.com/karamanolev/bencode3/blob/master/bencode.py

__version__ = '1.1.3'

import array

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from cpython.version cimport PY_MAJOR_VERSION
IS_PY2 = PY_MAJOR_VERSION == 2
if IS_PY2:
    END_CHAR = 'e'
    ARRAY_TYPECODE = b'b'
else:
    END_CHAR = ord('e')
    ARRAY_TYPECODE = 'b'


class BTFailure(Exception):
    pass


def decode_int(bytes x, int f):
    f += 1
    cdef long new_f = x.index(b'e', f)
    n = int(x[f:new_f])
    if x[f] == b'-'[0]:
        if x[f + 1] == b'0'[0]:
            raise ValueError()
    elif x[f] == b'0'[0] and new_f != f + 1:
        raise ValueError()
    return n, new_f + 1


def decode_string(bytes x, int f):
    cdef long colon = x.index(b':', f)
    cdef long n = int(x[f:colon])
    if x[f] == b'0'[0] and colon != f + 1:
        raise ValueError()
    colon += 1
    return x[colon:colon + n], colon + n


def decode_list(bytes x, int f):
    r, f = [], f + 1
    while x[f] != END_CHAR:
        v, f = decode_func[x[f]](x, f)
        r.append(v)
    return r, f + 1


def decode_dict(bytes x, int f):
    r = OrderedDict()
    f += 1
    while x[f] != END_CHAR:
        k, f = decode_string(x, f)
        r[k], f = decode_func[x[f]](x, f)
    return r, f + 1


decode_func = dict()

for func, keys in [
    (decode_list, 'l'),
    (decode_dict, 'd'),
    (decode_int, 'i'),
    (decode_string, [str(x) for x in range(10)])
]:
    for key in keys:
        if IS_PY2:
            decode_func[key] = func
        else:
            decode_func[ord(key)] = func


def bdecode(bytes x):
    try:
        r, l = decode_func[x[0]](x, 0)
    except (IndexError, KeyError, ValueError):
        raise BTFailure("not a valid bencoded string")
    if l != len(x):
        raise BTFailure("invalid bencoded value (data after valid prefix)")
    return r


def encode(v, r):
    tp = type(v)
    if tp in encode_func:
        return encode_func[tp](v, r)
    else:
        for tp, func in encode_func.items():
            if isinstance(v, tp):
                return func(v, r)
    raise BTFailure(
        "Can't encode {0}(Type: {1})".format(v, type(v))
    )


def encode_int(long x, r):
    r.fromstring(b'i')
    r.fromstring(str(x).encode())
    r.fromstring(b'e')


def encode_long(x, r):
    r.fromstring(b'i')
    r.fromstring(str(x).encode())
    r.fromstring(b'e')


def encode_bytes(bytes x, r):
    r.fromstring(str(len(x)).encode())
    r.fromstring(b':')
    r.fromstring(x)


def encode_string(str x, r):
    r.fromstring(str(len(x)).encode())
    r.fromstring(b':')
    r.fromstring(x.encode())


def encode_list(x, r):
    r.fromstring(b'l')
    for i in x:
        encode(i, r)
    r.fromstring(b'e')


def encode_dict(x, r):
    r.fromstring(b'd')
    item_list = list(x.items())
    item_list.sort()
    for k, v in item_list:
        if isinstance(k, str):
            k = k.encode()
        encode_bytes(k, r)
        encode(v, r)
    r.fromstring(b'e')


encode_func = {
    int: encode_int,
    bool: encode_int,    
    long: encode_long,
    bytes: encode_bytes,
    str: encode_string,
    list: encode_list,
    tuple: encode_list,
    dict: encode_dict,
    OrderedDict: encode_dict,
}


def bencode(x):
    r = array.array(ARRAY_TYPECODE)
    encode(x, r)
    return r.tostring()
