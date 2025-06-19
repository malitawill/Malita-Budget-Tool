#import unittest
from data.db_connection import create_connection

def test_connection_successful():
    conn=create_connection()
    assert conn is not None