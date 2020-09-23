import numpy as np


pattern_dict = {
    ### Gliders ###
    'glider':                 [[1, 0, 0],
                               [0, 1, 1],
                               [1, 1, 0]],
    'lightweight_spaceship':  [[0, 1, 0, 0, 1],
                               [1, 0, 0, 0, 0],
                               [1, 0, 0, 0, 1],
                               [1, 1, 1, 1, 0]],
    'middleweight_spaceship': [[0, 0, 0, 1, 0, 0],
                               [0, 1, 0, 0, 0, 1],
                               [1, 0, 0, 0, 0, 0],
                               [1, 0, 0, 0, 0, 1],
                               [1, 1, 1, 1, 1, 0]],
    ### Oscilators ###
    'toad':     [[1, 1, 1, 0],
                 [0, 1, 1, 1]],
    'pulsar':   [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    'figure_eight':     [[1, 1, 1, 0, 0, 0],
                         [1, 1, 1, 0, 0, 0],
                         [1, 1, 1, 0, 0, 0],
                         [0, 0, 0, 1, 1, 1],
                         [0, 0, 0, 1, 1, 1],
                         [0, 0, 0, 1, 1, 1]],
    'pentadecathlon':   [[1, 1, 1],
                         [1, 0, 1],
                         [1, 1, 1],
                         [1, 1, 1],
                         [1, 1, 1],
                         [1, 1, 1],
                         [1, 0, 1],
                         [1, 1, 1]],
    'r_pentimino':      [[0, 1, 1],
                         [1, 1, 0],
                         [0, 1, 0]]
}
