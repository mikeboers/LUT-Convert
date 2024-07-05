#!/usr/bin/env python3

from __future__ import print_function, division

import math
import sys
from optparse import OptionParser

from PIL import Image


def main():

    opt_parser = OptionParser(usage='%prog [options] input.png output.cube')
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

    print('%d steps -> %d values' % (steps, steps**6), file=sys.stderr)
    # Assume that we are going from 8 bits to 10.

    out = open(args[1], 'w')
    #out.write('#Created by: Adobe Photoshop CS6\n')
    #out.write('#Copyright: Copyright 2012 Adobe Systems Inc.\n')
    #out.write('TITLE "Testing"\n')
    #out.write('\n')
    #out.write('#LUT size\n')
    out.write('LUT_3D_SIZE %d\n' % (steps ** 2))
    #out.write('\n')
    #out.write('#data domain\n')
    out.write('DOMAIN_MIN 0.0 0.0 0.0\n')
    out.write('DOMAIN_MAX 1.0 1.0 1.0\n')
    #out.write('\n')
    #out.write('#LUT data points\n')

    if False:
        steps1 = steps + 1
        steps3 = steps ** 2 * (steps + 1)
        steps5 = steps ** 4 * (steps + 1)
        data = list(in_.getdata())
        def lookup(ri, gi, bi):
            return data[
                ri * steps1 + gi * steps3 + bi * steps5
            ]
        for bi in xrange(steps):
            for gi in xrange(steps):
                for ri in xrange(steps):
                    r, g, b = lookup(ri, gi, bi)[:3]
                    out.write('%f %f %f\n' % (r / 255.0, g / 255.0, b / 255.0))
    else:
        for pixel in in_.getdata():
            r, g, b = pixel[:3]
            out.write('%f %f %f\n' % (r / 255.0, g / 255.0, b / 255.0))




if __name__ == '__main__':
    main()
