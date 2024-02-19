import pytest
from main import StudentsInMLOps

@pytest.fixture
def instance():
    return StudentsInMLOps()

def test_enrollStudents(instance):
    instance.enrollStudents(5)
    assert instance.getTotalStrength() == 5

def test_dropStudents(instance):
    instance.enrollStudents(10)
    instance.dropStudents(3)
    assert instance.getTotalStrength() == 7

def test_getClassName(instance):
    assert instance.getClassName() == "StudentsInMLOps"
