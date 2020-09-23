import sys
import argparse
import numpy as np

from game import GameOfLife
from patterns import pattern_dict


def str2bool(v):
    """
    Takes user input as a string and returns boolean.
    Taken from stack overflow 
    https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
    """
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_pixels",
        help="Number of pixels in width/height", type=int, default=800)
    parser.add_argument("--num_cells",
        help="Number of cells in width/height", type=int, default=25)
    parser.add_argument("--num_frames",
        help="Number of frames in simulation. Continues indefinitly otherwise", type=int)
    parser.add_argument("--save_frames",
        help="Saves frames as png. Only works if num_frames specified",
        type=str2bool, default=False)
    parser.add_argument("--random_init",
        help="Creates a randomly intialized grid",
        type=str2bool, default=False)
    parser.add_argument("--add_patterns",
        help="Allows user to add predefined patterns to grid",
        type=str2bool, default=False)
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    pattern_list = []
    if args.add_patterns:
        print('Enter the name of the pattern, col, row. e.g. pulsar 1 1')
        while True:
            instruction = input()
            if instruction is '':
                break
            pattern_str, col, row = instruction.split()
            # Get pattern from pattern_dict and convert to np array
            pattern = np.array(pattern_dict[pattern_str], dtype=np.int8)
            pattern_list.append((pattern, int(col), int(row)))

    game = GameOfLife(n_pixels=args.num_pixels, N=args.num_cells,
                      num_frames=args.num_frames, save_frames=args.save_frames,
                      random_init=args.random_init)
    for pattern in pattern_list:
        game.add_pattern(*pattern)
    game.run()


if __name__ == '__main__':
    main()