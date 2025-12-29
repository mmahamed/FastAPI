import pytest

class Student:
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years


# Without using fixtures
def test_person_initialization():
    p = Student('John', 'Doe', 'Computer Science', 3)
    assert p.first_name == 'John'
    assert p.last_name == 'Doe'
    assert p.major == 'Computer Science'
    assert p.years == 3


# Using fixtures
@pytest.fixture
def default_employee():
    return Student('John', 'Doe', 'Computer Science', 3)

def test_person_initialization_with_fixture(default_employee):
    assert default_employee.first_name == 'John'
    assert default_employee.last_name == 'Doe'
    assert default_employee.major == 'Computer Science'
    assert default_employee.years == 3