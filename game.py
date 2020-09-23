import numpy as np
from datetime import datetime
import pygame
import sys
import os

from patterns import *


# RGB Color values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (125, 125, 125)

pygame.init()

class GameOfLife:
    """
    Main class for handling Game of Life and GUI.

    Args:
        N: The number of cells in height/width.
        n_pixels: The number of pixels in height/width
        num_frames: Used to control how long the simulation runs for,
                    if no value is specified it will run indefinitley.
        save_frames: Creates new folder in images and saves each frame.
        random_init: Creates a randomly initialized grid.
    """
    def __init__(self, N=25, n_pixels=800, num_frames=None, 
                 save_frames=False, random_init=False):
        self.N = N
        self.n_pixels = n_pixels
        self.fps = 5
        self.screen = pygame.display.set_mode((self.n_pixels, self.n_pixels))
        self.surface = pygame.Surface((self.n_pixels, self.n_pixels))
        self.clock = pygame.time.Clock()
        self.square_size = self.n_pixels // self.N
        self.buffer = self.square_size // 2

        self.run_simulation = False
        self.num_frames = num_frames
        self.frame_counter = 0
        self.save_frames = save_frames
        if self.save_frames:
            # Creates a new directory with current datetime as name
            date_object = datetime.now()
            date_str = dt_object.strftime("%d-%m-%Y-%H:%m")
            self.dir_name = 'images/img_dir_' + date_str
            os.mkdir(self.dir_name)

        # Uses 8 directions (cardinal & diagonal) to get neighbors
        self.directions = ((0, 1), (0, -1), (1, 1), (1, -1),
                          (-1, 1), (-1, -1), (1, 0), (-1, 0))
        if random_init:
            self.matrix = np.random.randint(2, size=(self.N, self.N), dtype=np.int8)
        else:
            self.matrix = np.zeros((self.N, self.N), dtype=np.int8)

    def save_frame(self):
        """
        Saves each frame into a folder in the 'images' directory
        """
        fname = os.path.join(self.dir_name, f'image_{self.frame_counter}.png')
        pygame.image.save(self.screen, fname)

    def add_pattern(self, pattern, row, col):
        height, width = pattern.shape
        self.matrix[row:row+height, col:col+width] = pattern

    def simulate(self):
        """
        Simulates one timestep and updates matrix
        """
        new_matrix = self.matrix.copy()
        for i in range(self.N):
            for j in range(self.N):
                neighbors = []
                for d in self.directions:
                    neighbors.append(self.matrix[(i+d[0])%self.N][(j+d[1])%self.N])
                n_neigbors = sum(neighbors)
                if self.matrix[i][j] == 1:
                    if (n_neigbors < 2) or (n_neigbors > 3):
                        new_matrix[i][j] = 0
                else:
                    if n_neigbors == 3:
                        new_matrix[i][j] = 1

        self.matrix = new_matrix.copy()
        self.frame_counter += 1

    def update_display(self):
        """
        Updates GUI display
        """
        self.screen.fill(GRAY)
        for i in range(self.N):
            for j in range(self.N):
                rect = ((self.square_size+1) * j,
                        (self.square_size+1) * i,
                         self.square_size,
                         self.square_size)
                if self.matrix[i][j] == 1:
                    pygame.draw.rect(self.screen, BLACK, rect)
                else:
                    pygame.draw.rect(self.screen, WHITE, rect)
        pygame.display.update()

    def run(self):
        """
        Main pygame event loop
        """
        while True:
            if self.frame_counter == self.num_frames:
                self.run_simulation = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if self.run_simulation:
                        self.run_simulation = False
                    else:
                        self.run_simulation = True

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    x_pos = (x - self.buffer) // self.square_size
                    y_pos = (y - self.buffer) // self.square_size
                    if self.matrix[y_pos][x_pos] == 0:
                        self.matrix[y_pos][x_pos] = 1
                    else:
                        self.matrix[y_pos][x_pos] = 0

            if self.run_simulation == True:
                if self.save_frames and self.num_frames:
                    self.save_frame()
                self.simulate()

            self.update_display()
            self.clock.tick(self.fps)
