import pytest
import psycopg2

test_db = psycopg2.connect(dbname="ecommerce_test")
cursor = test_db.cursor()

# def build_customer(first_name, last_name):
#     customer_str = """INSERT INTO customers (first_name, last_name) 
#     VALUES (%s, %s);"""
#     cursor.execute(customer_str, (first_name, last_name))
#     test_db.commit()

# def teardown_customers():
#     customer_str = """DELETE FROM customers;"""
#     cursor.execute(customer_str)
#     test_db.commit()

# @pytest.fixture
# def customers_table():
#     teardown_customers()
#     build_customer('Bob', 'Smith')
#     yield
#     teardown_customers()

def test_find_customer(customers_table):
    cursor.execute('SELECT first_name, last_name FROM customers;')
    customers = cursor.fetchall()
    assert customers == [('Bob', 'Smith')]

def test_count_customers(customers_table):
    cursor.execute('SELECT COUNT(*) FROM customers;')
    num_customers = cursor.fetchall()
    assert num_customers == [(1,)]

def test_empty_customers():
    cursor.execute('SELECT COUNT(*) FROM customers;')
    num_customers = cursor.fetchall()
    assert num_customers == [(0,)]
