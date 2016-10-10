#!/usr/bin/python

import unittest

class TestWalls(unittest.TestCase):

    def test_N_facingWall(self):
        self.assertEqual('foo'.upper(), 'FO')

    def test_S_facingWall(self):
        self.assertEqual('foo'.upper(), 'FO')

    def test_E_facingWall(self):
        self.assertEqual('foo'.upper(), 'FO')

    def test_W_facingWall(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
