import pytest

employees = []

customers = []

def test_find_employees(employees_table):
    assert employees[0] == 'bob'

def test_num_employees(employees_table):
    assert len(employees) == 1

def test_find_customers(customers_table):
    assert customers[0] == 'bob'

def test_num_customers(customers_table):
    assert len(customers) == 1

def test_num_customers_without_fixture():
    len(customers) == 0
