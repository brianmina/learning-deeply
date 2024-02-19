import pytest

from employee import Employee



@pytest.fixture
def employee_salary():
    """Creates the instance of the Employee class"""
    salary = 70_000
    info_employee = Employee("Brian", "Mina", salary)
    return info_employee


def test_give_default_raise(employee_salary):
    """Adds the default raise to the annual salary??"""
    employee_salary.give_raise()
    assert employee_salary.annual_salary == 75_000


def test_give_custom_raise(employee_salary):
    """Adds a custom raise to the annual salary?"""
    employee_salary.give_raise(10_000)
    assert employee_salary.annual_salary == 80_000
