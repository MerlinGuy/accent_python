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
        names = TestAccent.get_names('test_data.json')
        for uni, ascii in names.iteritems():
            stripped = strip_accent(uni, True)
            self.assertEquals(stripped, ascii)

    def test_has_unicode(self):
        names = TestAccent.get_names('test_data2.json')
        for uni, loc in names.iteritems():
            indx = first_unicode(uni)
            self.assertEquals(loc, indx)

    def test_encode_ascii(self):
        names = TestAccent.get_names('test_data.json')
        for uni, ascii in names.iteritems():
            stripped = encode_ascii(uni)
            self.assertEquals(stripped, ascii)

    def test_encode_ascii_fail(self):
        stripped = encode_ascii(u"ABC\u0F04defg")
        self.assertEquals(stripped, 'ABCdefg')

    # def test_create_unifile(self):
    #     output = []
    #     names = TestAccent.get_names('names.json')
    #     for name in names:
    #         new_name = strip_accent(name, True, True)
    #         if name != new_name:
    #             output.append(name)
    #     jdata = json.dumps(output)
    #     self.write_json('uni_names.json', jdata)
    #
    # def test_create_test_file(self):
    #     output = {}
    #     names = TestAccent.get_names('uni_names.json')
    #     for name in names:
    #         new_name = strip_accent(name, True, True)
    #         if name != new_name:
    #             output[name] = new_name
    #     jdata = json.dumps(output)
    #     self.write_json('test_data.json', jdata)
    #
    # def test_create_test_file2(self):
    #     output = {}
    #     names = TestAccent.get_names('uni_names.json')
    #     for name in names:
    #         indx = first_unicode(name)
    #         if indx > -1:
    #             output[name] = indx
    #     jdata = json.dumps(output)
    #     self.write_json('test_data2.json', jdata)

    @staticmethod
    def get_names(filename):
        with open(filename) as json_data:
            names = json.load(json_data)
            json_data.close()
        return names

    @staticmethod
    def write_json(filename, text):
        f = open(filename, 'w')
        f.write(text)
        f.close()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestAccent("test_accent"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

