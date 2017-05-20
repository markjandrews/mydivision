from mydivision.pbdraw import PowerBallDraw
from mydivision.ozdraw import OzLottoDraw


class Config(object):
    def __init__(self, **kwargs):

        for key, value in kwargs.items():
            setattr(self, key, value)

configs = {'pb': Config(uri='https://thelott.com/tattersalls/results/latest-results', klass=PowerBallDraw),
           'oz': Config(uri='https://thelott.com/tattersalls/results/latest-results', klass=OzLottoDraw)}
