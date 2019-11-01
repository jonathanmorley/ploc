#!/usr/bin/env python

import fnmatch
import json
import os
import subprocess
import unittest


class IntegrationTestAgainstTokei(unittest.TestCase):

    def test_py_files(self):
        for root, _, files in os.walk('.'):
            for file in fnmatch.filter(files, '*.py'):
                file_path = os.path.join(root, file)
                cloc = int(subprocess.check_output(['./ploc.py', file_path]).strip())
                tokei_json = subprocess.check_output(['tokei', file_path, '--output=json'])
                tokei = json.loads(tokei_json)['inner']['Python']['code']
                self.assertEqual(cloc, tokei)


if __name__ == '__main__':
    unittest.main()
