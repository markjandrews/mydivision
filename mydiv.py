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

    processor = config.klass(requests.post(config.uri, json=config.data), config)

    print('Checking "%s" results: %s' % (processor.name, sorted(processor.balls)), end='')

    if processor.sups is not None:
        print(' %s' % sorted(processor.sups), end='')

    print()

    for dividend in processor.dividends:
        print('%s Winners: %s Amount: $%.2f' % (dividend['name'], dividend['winners'], dividend['value']))

    print()

    with open(args.input_file, 'r') as inf:
        picked_list = json.load(inf)

    total_won = 0
    for picked_item in picked_list:
        amount_won = processor.check_winner(picked_item)
        if amount_won:
            total_won += amount_won

    print('Total Won: ${0:.2f}'.format(total_won))


if __name__ == '__main__':
    main()
