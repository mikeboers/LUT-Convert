#!/usr/bin/env python3

from __future__ import print_function, division

import math
import sys
from optparse import OptionParser

from PIL import Image


def main():

    print("Warning: This script does not return accurate results.", file=sys.stderr)
    
    opt_parser = OptionParser(usage='%prog [options] input.png output.3dl')
    opts, args = opt_parser.parse_args()

    if len(args) != 2:
        opt_parser.print_usage()
        exit(1)

    in_ = Image.open(args[0]).convert("RGB")
    w, h = in_.size
    if w != h:
        print('HALD input is not square.', file=sys.stderr)
        exit(2)
    steps = int(round(math.pow(w, 1/3)))
    if steps ** 3 != w:
        print('HALD input size is invalid: %d is not a cube.' % w, file=sys.stderr)
    print('%d steps' % steps, file=sys.stderr)
    # Assume that we are going from 8 bits to 10.

    out = open(args[1], 'w')
    header = [1023 * i // (steps - 1) for i in range(steps)]
    out.write(' '.join(str(x) for x in header))
    out.write('\n')

    steps1 = steps + 1
    steps3 = steps ** 2 * (steps + 1)
    steps5 = steps ** 4 * (steps + 1)
    data = list(in_.getdata())
    def lookup(ri, gi, bi):
        return data[
            ri * steps1 + gi * steps3 + bi * steps5
        ]
    for ri in range(steps):
        for gi in range(steps):
            for bi in range(steps):
                r, g, b = lookup(ri, gi, bi)
                out.write('%d %d %d\n' % (r * 4, g * 4, b * 4))



if __name__ == '__main__':
    main()
