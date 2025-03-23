#
# Created on Fri Mar 21 2025 by Ziang Zhang
#
# Copyright (c) 2025 St. Jude Children's Research Hospital
#
# Use of this source code is governed by an GNU GPLv3
# license that can be found in the LICENSE file or at
# https://www.gnu.org/licenses/gpl-3.0.html
#
import unittest
import sys

def get_python_version():
    """
    This function returns the version of Python that is currently running.
    """
    return sys.version_info

class TestPyVersion(unittest.TestCase):
    """
    The test might look funny.
    It was used to test the `tox` package.
    """
    def test_py37(self):
        """
        Test if the python version is 3.7
        """
        
        major, minor = get_python_version()[:2]
        self.assertEqual(major, 3)
        self.assertEqual(minor, 7)
        
    def test_py38(self):
        """
        Test if the python version is 3.8
        """
        
        major, minor = get_python_version()[:2]
        self.assertEqual(major, 3)
        self.assertEqual(minor, 8)

    def test_py39(self):
        """
        Test if the python version is 3.9
        """
        
        major, minor = get_python_version()[:2]
        self.assertEqual(major, 3)
        self.assertEqual(minor, 9)

    def test_py310(self):
        """
        Test if the python version is 3.10
        """
        
        major, minor = get_python_version()[:2]
        self.assertEqual(major, 3)
        self.assertEqual(minor, 10)
        