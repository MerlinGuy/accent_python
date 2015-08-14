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


def break_name(name, lowerit=False, check_comma=False):
    if name is None or len(name) == 0:
        return [name]

    if lowerit:
        name = name.lower()

    if check_comma:
        pieces = name.split(',')
        if len(pieces) > 1:
            npieces = []
            npieces.extend(pieces[1].split())
            npieces.extend(pieces[0].split())
            pieces = npieces
        else:
            pieces = pieces[0].split()
    else:
        pieces = name.split()

    return pieces


def break_list(nlist):
    temp = []
    for item in nlist:
        temp.append(break_name(item, True, True))
    return temp


def find_name_in_list(name, nlist):
    if name is None or nlist is None:
        return []

    if not isinstance(nlist, list):
        nlist = break_list(nlist)

    if isinstance(name, basestring):
        name = break_name(name, True, True)

    matches = []
    indx = 0
    length = len(nlist)
    while indx < length:
        item = nlist[indx]
        found = True
        for word in name:
            if word not in item:
                found = False
                break

        if found:
            matches.append(item)

        indx += 1

    return matches
