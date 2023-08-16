from cost import CostFunction
from config import ALGORITHM_PARAMS, GOOD_ENOUGH_SCORE
from utils import array_to_chess_board

import numpy as np
from geneticalgorithm2 import geneticalgorithm2 as ga
from geneticalgorithm2 import Actions, MiddleCallbacks

class Model():
    def __init__(self):
        self.model = None
        self.f = CostFunction().f
    def run(self):
        middle_callbacks = [
            MiddleCallbacks().UniversalCallback(action=Actions.Stop(), condition= lambda data:data.last_generation.scores[0] <= GOOD_ENOUGH_SCORE) ]

        varbound = np.array([[0, 12]] * 64)
        self.model = ga(function=self.f, dimension=64, variable_type='int', variable_boundaries=varbound, algorithm_parameters=ALGORITHM_PARAMS)
        self.model.run(middle_callbacks = middle_callbacks, no_plot = True, disable_printing= True)
    
    def get_best_board(self): 
        if not self.model:
            self.run()
        return array_to_chess_board(list(self.model.result.variable))