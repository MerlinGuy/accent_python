# -*- coding: utf-8 -*-
__author__ = 'jeff boehmer (ft. collins research, llc)'

# The MIT License (MIT)
#
# Copyright (c) [year] [fullname]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import unittest
from accent import *
import json


class TestAccent(unittest.TestCase):

    def test_accent(self):
        names = TestAccent.get_names('names.json')
        for name in names:
            new_name = strip_accent(name, True, True)
            if name != new_name:
                print name + " to " + new_name

    def test_has_unicode(self):
        names = TestAccent.get_names('names.json')
        for name in names:
            indx = first_unicode(name)
            if indx > -1:
                print name + " at " + str(indx)

    def test_accent_word(self):
        name = u'DAŠKO, Mario'
        new_name = strip_accent(name, True)
        if name != new_name:
            print name + " to " + new_name

    @staticmethod
    def get_names(filename):
        with open(filename) as json_data:
            names = json.load(json_data)
            json_data.close()
        return names


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestAccent("test_accent"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

