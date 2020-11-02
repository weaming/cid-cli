# Author    : weaming
# Mail      : garden.yuen@gmail.com
# Created   : 2020-10-30 16:48:08

import sys
from cid import make_cid

version = '0.1'


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("cid")
    args = parser.parse_args()

    try:
        c = make_cid(args.cid)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    print('version:', c.version)
    print('  codec:', c.codec)
    print('    hex:', c.multihash.hex())
