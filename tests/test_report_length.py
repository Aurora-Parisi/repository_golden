from lib.report_length import report_length 

def test_function_reports_how_long_string_is():
    actual = report_length("three")
    expected = "This string was 5 characters long."
    assert actual == expected 
