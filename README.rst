Bencoder.pyx
============

A fast bencode implementation in Cython supports both Python2 & Python3 .

.. image:: https://img.shields.io/travis/whtsky/bencoder.pyx/master.svg?maxAge=3600&label=macOS
    :alt: macOS Test Status
    :target: https://travis-ci.org/whtsky/bencoder.pyx
.. image:: https://img.shields.io/appveyor/ci/whtsky/bencoder-pyx/master.svg?maxAge=3600&label=Windows
    :alt: Windows Test Status
    :target: https://ci.appveyor.com/project/whtsky/bencoder-pyx
.. image:: https://img.shields.io/circleci/ci/whtsky/bencoder-pyx/master.svg?maxAge=3600&label=Linux
    :alt: Linux Test Status
    :target: https://circleci.com/gh/whtsky/bencoder.pyx
.. image:: https://img.shields.io/pypi/l/bencoder.pyx.svg
    :alt: PyPI License
    :target: https://pypi.org/project/bencoder.pyx/
.. image:: https://codecov.io/gh/whtsky/bencoder.pyx/branch/master/graph/badge.svg
    :alt: Codecov Coverage
    :target: https://codecov.io/gh/whtsky/bencoder.pyx
.. image:: https://pypistats.com/badge/bencoder-pyx.png
    :alt: bencoder-pyx PyPI Downloads
    :target: https://pypistats.com/package/bencoder-pyx

Install
-------


.. code-block:: bash

    pip install bencoder.pyx


Usage
-----


.. code-block:: python

    from bencoder import bencode, bdecode, bdecode2
    
    assert bencode("WWWWWW") == b'6:WWWWWW'
    assert bencode(233) == b'i233e'
    
    with open("debian-8.3.0-amd64-netinst.iso.torrent", "rb") as f:
        torrent = bdecode(f.read())
        print(torrent['announce'])
    
    decoded, length = bdecode2(b'6:WWWWWWi233e')
    assert decoded == b'WWWWWW'
    assert length == 8

ChangeLog
----------

Version 1.2.1
~~~~~~~~~~~~~~~

+ Drop support for Python 2.6
+ Performance boost for `bencode` method. `#7 <https://github.com/whtsky/bencoder.pyx/issues/7>`_

Version 1.2.0
~~~~~~~~~~~~~~~

+ Add `bdecode2` method. `#6 <https://github.com/whtsky/bencoder.pyx/pull/6>`_

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
