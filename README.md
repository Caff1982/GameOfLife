# Game of Life

This is a python implementation of Conway's Game of Life using the pygame module as a GUI.

![](https://github.com/Caff1982/GameOfLife/blob/master/images/example.gif)

### Description

The purpose of this project is to provide a simple but versatile application to explore cellular automata, specifically Conway's Game of Life.

The application allows the user to create a starting grid freehand, load some common patterns or use random initialization. It also allows for frames to be saved as images if required.

### Requirements

- Python 3
- Numpy
- Pygame

### Usage

Start by cloning the repository and using pip to install requirements. 
By default the application loads with a blank grid of 25x25 cells and 800x800 pixels. Cells can then be turned on by clicking on them. To start the simulation press the space-bar.
```bash
python  main.py
```
Settings can be changed by passing command line arguments. To add patterns set "--add_patterns True", you will then be prompted for the pattern you want to add and the position. Press Enter when finished to load the application.
```bash
usage: main.py [-h] [--num_pixels NUM_PIXELS] [--num_cells NUM_CELLS]
               [--num_frames NUM_FRAMES] [--save_frames SAVE_FRAMES]
               [--random_init RANDOM_INIT] [--add_patterns ADD_PATTERNS]

optional arguments:
  -h, --help            show this help message and exit
  --num_pixels NUM_PIXELS
                        Number of pixels in width/height
  --num_cells NUM_CELLS
                        Number of cells in width/height
  --num_frames NUM_FRAMES
                        Number of frames in simulation. Continues indefinitely
                        otherwise
  --save_frames SAVE_FRAMES
                        If True saves frames as png. Only works if num_frames
                        specified
  --random_init RANDOM_INIT
                        If True creates a randomly intialized grid
  --add_patterns ADD_PATTERNS
                        If True allows user to add predefined patterns to grid
```

Example usage:
```bash
python main.py --num_frames 15 --num_cells 36 --add_patterns True
```