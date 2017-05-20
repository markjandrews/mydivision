import argparse
import json
import re
import sys
from io import StringIO

import requests
from lxml import etree

from config import configs


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Finds out winning divisions for picked numbers')
    parser.add_argument('-f', '--input-file', required=True, help='Path to picked numbers json')
    parser.add_argument('game', choices=configs.keys())

    args = parser.parse_args(argv)

    # Get results
    config = configs[args.game]

    processor = config.klass(requests.get(config.uri))

    with open(args.input_file, 'r') as inf:
        picked_list = json.load(inf)

    for picked_item in picked_list:
        processor.check_winner(picked_item)


if __name__ == '__main__':
    main()
