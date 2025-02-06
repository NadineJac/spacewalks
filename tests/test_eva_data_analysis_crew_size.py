import pytest
from eva_data_analysis import calculate_crew_size

def test_eva_data_analysis_crew_size(): # FIXME
    """
    Test that the crew size is 2 or ?
    """
    
    # Typical value 1
    actual_result =  calculate_crew_size("Mike Foale;Claude Nicollier;")
    expected_result = 2
    assert actual_result == expected_result
    
    # Typical value 2
    actual_result =  calculate_crew_size("Joe Tanner;Heide Stefanyshyn-Piper;") 
    expected_result = 2
    assert actual_result == expected_result