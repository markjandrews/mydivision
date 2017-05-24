from mydivision.pbdraw import PowerBallDraw
from mydivision.ozdraw import OzLottoDraw
from mydivision.pbphdraw import PowerBallPHDraw


class Config(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


configs = {
    'pb': Config(uri='https://thelott.com/tattersalls/results/latest-results', cost_per_game=0.92, klass=PowerBallDraw),
    'pbph': Config(uri='https://thelott.com/tattersalls/results/latest-results', cost_per_game=18.60,
                   klass=PowerBallPHDraw),
    'oz': Config(uri='https://thelott.com/tattersalls/results/latest-results', cost_per_game=1.30, klass=OzLottoDraw)}
