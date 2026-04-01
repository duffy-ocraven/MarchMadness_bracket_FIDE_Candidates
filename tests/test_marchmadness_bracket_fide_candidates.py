"""Test module for marchmadness_bracket_fide_candidates."""

from marchmadness_bracket_fide_candidates import __author__, __email__, __version__


def test_project_info():
    """Test __author__ value."""
    assert __author__ == "Duffy OCraven"
    assert __email__ == "duftkt@quinda.com"
    assert __version__ == "0.0.0"
