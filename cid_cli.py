# Author    : weaming
# Mail      : garden.yuen@gmail.com
# Created   : 2020-10-30 16:48:08

import sys
from cid import make_cid
import multihash, multibase

version = '1.0'


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

    if c.version == 0:
        mb_codec = 'base58btc'
    else:
        mb_codec = multibase.get_codec(args.cid).encoding
    mh = multihash.decode(c.multihash)
    print(f'{mb_codec} - cidv{c.version} - {c.codec} - {mh.name}-{len(mh.digest)*8}-{mh.digest.hex()}')
    # print(f'// see also https://cid.ipfs.io/#{args.cid}', file=sys.stderr)


if __name__ == '__main__':
    main()
