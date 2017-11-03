import re
from io import StringIO

from lxml import etree

from .common import BaseDraw


class PowerBallDraw(BaseDraw):
    @property
    def balls(self):
        if self._balls is None:
            self._balls = self._data['DrawResults'][0]['PrimaryNumbers']

        return self._balls

    @property
    def sups(self):
        if self._sups is None:
            self._sups = self._data['DrawResults'][0]['SecondaryNumbers']

        return self._sups

    @property
    def dividends(self):
        if self._dividends is None:
            self._dividends = []

            for dividend_info in self._data['DrawResults'][0]['Dividends']:
                dividend = {'name': 'Division %s' % dividend_info['Division'],
                            'value': dividend_info['BlocDividend'],
                            'winners': dividend_info['BlocNumberOfWinners'],
                            'num_balls': self._config.winning_combs[dividend_info['Division']]['num_balls'],
                            'needs_powerball': self._config.winning_combs[dividend_info['Division']]['needs_powerball']}

                self._dividends.append(dividend)

        return self._dividends

    def check_winner(self, picked_item):
        winning_balls = set(picked_item[0]).intersection(self.balls)
        winning_powerball = picked_item[1][0] == self.sups[0]

        for dividend in self.dividends:
            if len(winning_balls) == dividend['num_balls']:
                if not dividend['needs_powerball'] or winning_powerball:
                    amount_won = dividend['value']
                    print(dividend['name'], sorted(winning_balls), end='')

                    if winning_powerball:
                        print(' (%s)' % self.sups[0], end='')

                    print(' ${0:.2f}'.format(amount_won))
                    return amount_won
