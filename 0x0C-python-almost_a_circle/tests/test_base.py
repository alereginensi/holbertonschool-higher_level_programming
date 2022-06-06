#!/usr/bin/python3

'''Test for Base'''


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''class that tests the Base'''
    def test_task1(self):
        '''test for task1'''
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = base()

        self.assertIsNotNone(id)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 4)

if __name__ == '__main__':
    unittest.main()
