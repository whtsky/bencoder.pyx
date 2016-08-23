Bencoder.pyx
============

A fast bencode implementation in Cython supports both Python2 & Python3 .

.. image:: https://img.shields.io/travis/whtsky/bencoder.pyx/develop.svg?maxAge=3600&label=macOS
    :target: https://travis-ci.org/whtsky/bencoder.pyx
.. image:: https://img.shields.io/appveyor/ci/whtsky/bencoder-pyx/develop.svg?maxAge=3600&label=Windows
    :target: https://ci.appveyor.com/project/whtsky/bencoder-pyx
.. image:: https://semaphoreci.com/api/v1/whtsky/bencoder-pyx/branches/develop/shields_badge.svg
    :target: https://semaphoreci.com/whtsky/bencoder-pyx

.. image:: https://img.shields.io/travis/whtsky/bencoder.pyx/develop.svg?maxAge=3600&label=wheels
    :target: https://travis-ci.org/whtsky/bencoder.pyx
.. image:: https://codecov.io/gh/whtsky/bencoder.pyx/branch/develop/graph/badge.svg
    :target: https://codecov.io/gh/whtsky/bencoder.pyx

Install
-------


.. code-block:: bash

    pip install bencoder.pyx


Usage
-----


.. code-block:: python

    from bencoder import bencode, bdecode
    
    assert bencode("WWWWWW") == b'6:WWWWWW'
    assert bencode(233) == b'i233e'
    
    with open("debian-8.3.0-amd64-netinst.iso.torrent", "rb") as f:
        torrent = bdecode(f.read())
        print(torrent['announce'])

ChangeLog
----------

Version 1.1.3
~~~~~~~~~~~~~~~

+ Performance Improvement
+ Fix package metainfo `#3 <https://github.com/whtsky/bencoder.pyx/issues/3>`_

Version 1.1.2
~~~~~~~~~~~~~~~

+ Support encode large int

Version 1.1.0
~~~~~~~~~~~~~~~

+ Use OrderedDict instaed of dict
+ Support encoding subclasses of dict
