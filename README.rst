Bencoder.pyx
============

A fast bencode implementation in Cython supports both Python2 & Python3 .

.. image:: https://travis-ci.org/whtsky/bencoder.pyx.svg?branch=master
    :target: https://travis-ci.org/whtsky/bencoder.pyx

.. image:: https://ci.appveyor.com/api/projects/status/ur6vy8wdj789oxqv/branch/master?svg=true
    :target: https://ci.appveyor.com/project/whtsky/bencoder-pyx

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

Version 1.1.0
~~~~~~~~~~~~~~~

+ Use OrderedDict instaed of dict
+ Support encoding subclasses of dict
