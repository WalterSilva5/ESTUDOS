import pytest
from get_full_name import get_full_name

def test_get_full_name():
    """Test get_full_name()."""
    full_name = get_full_name('janis', 'joplin')
    assert full_name == 'janis joplin'