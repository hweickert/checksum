import sys
import pytest

if sys.version_info.major == 2:
    from StringIO import StringIO
else:
    from io import StringIO


def test_import_works():
    import checksum

def test_get_for_handle():
    import checksum
    file_handle = StringIO('abc123')

    res = checksum.get_for_handle(file_handle, hash_mode='md5')

    assert res == 'e99a18c428cb38d5f260853678922e03'
