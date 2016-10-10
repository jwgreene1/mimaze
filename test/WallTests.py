#!/usr/bin/python

import unittest

class TestWalls(unittest.TestCase):

    def test_N_facing_wall(self):
        self.assertEqual('foo'.upper(), 'FO')

    def test_S_facing_wall(self):
        self.assertEqual('foo'.upper(), 'FO')

    def test_E_facing_wall(self):
        self.assertEqual('foo'.upper(), 'FO')

    def test_W_facing_wall(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
