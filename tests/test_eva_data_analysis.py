import pytest
from eva_data_analysis import text_to_duration
from eva_data_analysis import calculate_crew_size

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


@pytest.mark.parametrize("input_value, expected_results",[
    ("Mike Foale;",1),
    ("Joe Tanner;Heide Stefanyshyn-Piper;",2)
])
def test_eva_data_analysis_crew_size(input_value, expected_results): 
    """
    Test that the calculate_crew_size returns expected ground truth values for crew values
    """
    # Typical value 1
    actual_result =  calculate_crew_size(input_value)
    assert actual_result == expected_result
        
    # Edge case
    """                                                                                                                               
    Test that calculate_crew_size returns expected ground truth values                                                                
    for edge case where crew is an empty string                                                                                       
    """                                                                                                                               
    actual_result = calculate_crew_size("")                                                                                           
    assert actual_result is None 