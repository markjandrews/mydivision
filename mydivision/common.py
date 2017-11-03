from io import StringIO

from lxml import etree


class BaseDraw(object):

    def __init__(self, response, config):

        assert response.status_code == 200, response.status_code
        self._balls = None
        self._sups = None
        self._dividends = None
        self._data = response.json()
        self._config = config

    @property
    def name(self):
        return self.__class__.__name__.replace('Draw', '')

    @property
    def balls(self):
        raise NotImplementedError

    @property
    def sups(self):
        raise NotImplementedError
