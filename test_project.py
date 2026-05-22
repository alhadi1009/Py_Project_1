from project import validate_name, validate_Author, ShowMenu

def test_validate_name():
    assert validate_name("John Doe") == True
    assert validate_name("123") == False

def test_validate_Author():
    assert validate_Author("A. Rahman") == True
    assert validate_Author("123") == False
def test_ShowMenu():
    result = ShowMenu()
    assert "PDF Generate" in result