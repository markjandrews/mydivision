from io import StringIO

from lxml import etree


class BaseDraw(object):

    def __init__(self, response):
        self._balls = None
        self._sups = None
        self._dividends = None
        self._tree = etree.parse(StringIO(response.content.decode('utf-8')), etree.HTMLParser())

    @property
    def name(self):
        return self.__class__.__name__.replace('Draw', '')

    @property
    def balls(self):
        raise NotImplementedError

    @property
    def sups(self):
        raise NotImplementedError
