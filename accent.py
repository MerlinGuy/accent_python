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


CAP_LOW = 64
CAP_HI = 91
LOW_LOW = 96
LOW_HI = 123
ASCII_BOUNDRY = 127

ORDINAL = {
    8305: 'i', 8341: 'h', 8342: 'k', 8343: 'l', 8344: 'm', 8345: 'n', 8346: 'p', 8347: 's', 8348: 't',
    8580: 'c', 192: 'a', 193: 'a', 194: 'a', 195: 'a', 196: 'a', 197: 'a', 199: 'c', 200: 'e', 201: 'e',
    202: 'e', 203: 'e', 204: 'i', 205: 'i', 206: 'i', 207: 'i', 209: 'n', 210: 'o', 211: 'o', 212: 'o',
    213: 'o', 214: 'o', 216: 'o', 217: 'u', 218: 'u', 219: 'u', 220: 'u', 221: 'y', 223: 's', 224: 'a',
    225: 'a', 226: 'a', 227: 'a', 228: 'a', 229: 'a', 231: 'c', 232: 'e', 233: 'e', 234: 'e', 235: 'e',
    236: 'i', 237: 'i', 238: 'i', 239: 'i', 241: 'n', 242: 'o', 243: 'o', 244: 'o', 245: 'o', 246: 'o',
    248: 'o', 249: 'u', 250: 'u', 251: 'u', 252: 'u', 253: 'y', 255: 'y', 257: 'a', 8450: 'c', 259: 'a',
    261: 'a', 263: 'c', 265: 'c', 8458: 'g', 267: 'c', 8460: 'h', 269: 'c', 271: 'd', 8464: 'i', 8465: 'i',
    8466: 'l', 275: 'e', 8468: 'l', 277: 'e', 279: 'e', 8472: 'p', 281: 'e', 8474: 'q', 8475: 'r', 8476: 'r',
    285: 'g', 287: 'g', 289: 'g', 291: 'g', 8484: 'z', 293: 'h', 295: 'h', 8488: 'z', 297: 'i', 299: 'i',
    8492: 'b', 301: 'i', 8495: 'e', 304: 'i', 8497: 'f', 8498: 'f', 8499: 'm', 8500: 'o', 309: 'j', 311: 'k',
    8506: 'q', 316: 'l', 318: 'l', 320: 'l', 8513: 'g', 8514: 'l', 8515: 'l', 324: 'n', 8517: 'd', 326: 'n',
    8519: 'e', 8467: 'l', 8521: 'j', 333: 'o', 8526: 'f', 335: 'o', 337: 'o', 339: 'o', 341: 'r', 343: 'r',
    345: 'r', 347: 's', 349: 's', 351: 's', 353: 's', 355: 't', 357: 't', 359: 't', 361: 'u', 363: 'u',
    365: 'u', 367: 'u', 369: 'u', 371: 'u', 373: 'w', 375: 'y', 376: 'y', 378: 'z', 380: 'z', 382: 'z',
    383: 's', 384: 'b', 10625: 'z', 10626: 'z', 387: 'b', 8469: 'n', 390: 'o', 392: 'c', 393: 'd', 394: 'd',
    396: 'd', 398: 'e', 400: 'e', 402: 'f', 403: 'g', 407: 'i', 409: 'k', 410: 'l', 412: 'm', 413: 'n',
    414: 'n', 415: 'o', 417: 'o', 421: 'p', 427: 't', 429: 't', 430: 't', 432: 'u', 434: 'v', 436: 'y',
    438: 'z', 462: 'a', 464: 'i', 466: 'o', 468: 'u', 477: 'e', 485: 'g', 487: 'g', 489: 'k', 491: 'o',
    496: 'j', 501: 'g', 505: 'n', 8473: 'p', 513: 'a', 515: 'a', 517: 'e', 519: 'e', 521: 'i', 523: 'i',
    525: 'o', 527: 'o', 529: 'r', 531: 'r', 533: 'u', 535: 'u', 537: 's', 539: 't', 543: 'h', 544: 'n',
    545: 'd', 549: 'z', 551: 'a', 553: 'e', 559: 'o', 563: 'y', 564: 'l', 565: 'n', 566: 't', 567: 'j',
    570: 'a', 571: 'c', 572: 'c', 8765: 's', 8766: 's', 575: 's', 576: 'z', 579: 'b', 580: 'u', 581: 'v',
    582: 'e', 583: 'e', 584: 'j', 585: 'j', 586: 'q', 587: 'q', 588: 'r', 589: 'r', 590: 'y', 591: 'y',
    592: 'a', 593: 'a', 595: 'b', 596: 'o', 597: 'c', 598: 'd', 599: 'd', 600: 'e', 603: 'e', 604: 'e',
    605: 'e', 606: 'e', 607: 'j', 608: 'g', 609: 'g', 610: 'g', 613: 'h', 614: 'h', 616: 'i', 618: 'i',
    619: 'l', 620: 'l', 621: 'l', 623: 'm', 624: 'm', 625: 'm', 626: 'n', 627: 'n', 628: 'n', 629: 'o',
    633: 'r', 634: 'r', 635: 'r', 636: 'r', 637: 'r', 638: 'r', 639: 'r', 640: 'r', 641: 'r', 642: 's',
    647: 't', 648: 't', 649: 'u', 651: 'v', 652: 'v', 653: 'w', 654: 'y', 655: 'y', 656: 'z', 657: 'z',
    663: 'c', 665: 'b', 666: 'e', 667: 'g', 668: 'h', 669: 'j', 670: 'k', 671: 'l', 672: 'q', 686: 'h',
    688: 'h', 690: 'j', 691: 'r', 692: 'r', 694: 'r', 695: 'w', 696: 'y', 737: 'l', 738: 's', 739: 'x',
    8959: 'z', 780: 'v', 8999: 'x', 829: 'x', 851: 'x', 867: 'a', 868: 'e', 869: 'i', 870: 'o', 871: 'u',
    872: 'c', 873: 'd', 874: 'h', 875: 'm', 876: 'r', 877: 't', 878: 'v', 879: 'x', 7424: 'a', 7427: 'b',
    7428: 'c', 7429: 'd', 7431: 'e', 7432: 'e', 7433: 'i', 7434: 'j', 7435: 'k', 7436: 'l', 7437: 'm',
    7438: 'n', 7439: 'o', 7440: 'o', 7441: 'o', 7442: 'o', 7443: 'o', 7446: 'o', 7447: 'o', 7448: 'p',
    7449: 'r', 7450: 'r', 7451: 't', 7452: 'u', 7453: 'u', 7454: 'u', 7455: 'm', 7456: 'v', 7457: 'w',
    7458: 'z', 385: 'b', 7522: 'i', 7523: 'r', 7524: 'u', 7525: 'v', 573: 'l', 574: 't', 7747: 'm',
    19904: 'i', 128473: 'x', 7681: 'a', 7683: 'b', 7685: 'b', 7687: 'b', 7691: 'd', 7693: 'd', 7695: 'd',
    7697: 'd', 9746: 'x', 7699: 'd', 7705: 'e', 7707: 'e', 7711: 'f', 7713: 'g', 7715: 'h', 7717: 'h',
    7719: 'h', 7721: 'h', 7723: 'h', 7725: 'i', 9776: 'i', 7729: 'k', 7731: 'k', 7733: 'k', 7735: 'l',
    7739: 'l', 7741: 'l', 7743: 'm', 7745: 'm', 8459: 'h', 7749: 'n', 7751: 'n', 7753: 'n', 7755: 'n',
    8461: 'h', 7765: 'p', 7767: 'p', 7769: 'r', 7771: 'r', 7775: 'r', 7777: 's', 7779: 's', 273: 'd',
    7787: 't', 8579: 'c', 7789: 't', 7791: 't', 7793: 't', 7795: 'u', 7797: 'u', 7799: 'u', 7805: 'v',
    7807: 'v', 328: 'n', 7809: 'w', 7811: 'w', 7813: 'w', 7815: 'w', 7817: 'w', 9866: 'i', 7819: 'x',
    7821: 'x', 7823: 'y', 7825: 'z', 7827: 'z', 7829: 'z', 7830: 'h', 7831: 't', 7832: 'w', 7833: 'y',
    7834: 'a', 7835: 's', 7841: 'a', 283: 'e', 8477: 'r', 7865: 'e', 7867: 'e', 7869: 'e', 7881: 'i',
    7883: 'i', 7885: 'o', 7887: 'o', 7909: 'u', 7911: 'u', 7923: 'y', 7925: 'y', 7927: 'y', 7929: 'y',
    8493: 'c', 10005: 'x', 10006: 'x', 10007: 'x', 10008: 'x', 303: 'i', 8496: 'e', 305: 'i', 314: 'l',
    322: 'l', 8516: 'y', 8518: 'd', 8520: 'i', 7843: 'a', 352: 's', 321: 'L', 230: 'ae', 142: 'x'
}


def strip_accent(text, match_upper=False, throw_error=False):
    new_word = ""
    indx = 0
    length = len(text)
    found = False
    while indx < length:
        x = text[indx]
        ordinal = ord(x)
        if ordinal > ASCII_BOUNDRY:
            if ordinal in ORDINAL:
                x = ORDINAL[ordinal]
                if match_upper and (indx == 0 or (not isletter(text[indx - 1]))):
                    x = x.upper()
                found = True
            elif throw_error:
                raise Exception("Ordinal not in Accent dict: " + str(ordinal) + " - char: " + x)

        new_word += x
        indx += 1

    if found and match_upper:
        new_word = upperit(new_word)

    return new_word


def upperit(text):
    start = 0
    cap_count = 0
    indx = 0
    new_word = ""
    while indx < len(text):
        ochar = ord(text[indx])

        if CAP_HI > ochar > CAP_LOW:
            cap_count += 1
        elif LOW_HI > ochar > LOW_LOW:
            pass
        else:
            if cap_count > 1:
                new_word += text[start:indx].upper()
            else:
                new_word += text[start:indx]
            cap_count = 0
            start = indx

        indx += 1

    if cap_count > 1:
        new_word += text[start:indx].upper()
    else:
        new_word += text[start:indx]

    return new_word


def isletter(char):
    ochar = ord(char)
    return CAP_HI > ochar > CAP_LOW or LOW_HI > ochar > LOW_LOW


def first_unicode(text):
    indx = 0
    while indx < len(text):
        if ord(text[indx]) > ASCII_BOUNDRY:
            return indx
        indx += 1
    return -1


def get_ordinals(char):
    ords = []
    if char and len(char) == 1:
        lchar = char.lower()
        for key, value in ORDINAL.items():
            if value == lchar:
                ords.append(key)
    return ord


def strip_list(nlist):
    striped = []
    for name in nlist:
        striped.append(strip_accent(name))
    return striped


def encode_ascii(uni):
    return uni.encode('ascii', 'ignore')