"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

# from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2


def Mode(hist) -> int:
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    (key, value) = max(hist.Items(), key=(lambda item: item[1]))

    return key


def AllModes(hist) -> list:
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """

    freqs=list(hist.Items())
    freqs_sorted=sorted(freqs,key=itemgetter(1), reverse=True)


    return freqs_sorted


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert (mode == 39)

    # test AllModes
    modes = AllModes(hist)
    assert (modes[0][1] == 4693)

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
