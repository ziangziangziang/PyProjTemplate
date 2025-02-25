#
# test_module1.py - ${module1 unittest}
#
# (c) Ziang Zhang
#
# Written by Ziang Zhang <ZIANGZHANG1997@GMAIL.COM>
#
# The code is licensed under the GNU GPLv3 license.
# Tue Feb 25 2025
#

import unittest
from templatepyproj import do_nothing

class TestFunc1(unittest.TestCase):

    def test_do_nothing(self):
        """
        Test the do_nothing function.
        """
        # Call the function
        do_nothing()

        # Check that the function does not raise any exceptions
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()