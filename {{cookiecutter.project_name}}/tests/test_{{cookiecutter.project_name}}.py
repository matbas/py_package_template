#!/usr/bin/env python3

import unittest


from {{ cookiecutter.project_name }} import {{ cookiecutter.project_name }}


class Test{{ cookiecutter.project_name }}(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
