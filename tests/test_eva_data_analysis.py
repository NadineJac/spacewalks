import pytest
from eva_data_analysis import text_to_duration

def test_text_to_duration_float():
    """
    Test that text_to_duration returns expected value for durations with a non-zero minute component
    """
    assert text_to_duration("10:20") == pytest.approx(10.33333333333)


def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected value for durations with typical whole hour durations
    """
    assert text_to_duration("10:00") == 10