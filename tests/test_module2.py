#
# test_module2.py - ${module2 unittest}
#
# (c) Ziang Zhang
#
# Written by Ziang Zhang <ZIANGZHANG1997@GMAIL.COM>
#
# The code is licensed under the GNU GPLv3 license.
# Tue Feb 25 2025
#
import unittest
from templatepyproj import say_hello
from io import StringIO
import sys

class TestFunc2(unittest.TestCase):
    def test_say_hello(self):
        """
        Test the say_hello function. Evaluate the stdout output.
        """
        
        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function
        say_hello()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Check that the output is correct
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")
if __name__ == '__main__':
    unittest.main()