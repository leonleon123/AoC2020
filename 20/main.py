import re
from math import prod, sqrt

import numpy as np
import scipy.signal as sg


class Tile:
    def __init__(self, block):
        if len(block):
            tmp = block.split("\n")
            self.id = int(re.search("[0-9]+", tmp[0]).group())
            self.matrix = np.array([np.array([1 if x == "#" else 0 for x in line]) for line in tmp[1:]]).T
            self.edge_check = np.array([*self.edges(),*[np.flip(x) for x in self.edges()]])

    def match_edge(self, edge, tiles):
        return [tile.id for tile in tiles if tile.id != self.id and any(np.all(edge == tile.edge_check, 1))]

    def match_edges(self, tiles):
        return  self.match_edge(self.matrix[0, :], tiles) + \
                self.match_edge(self.matrix[-1, :], tiles) + \
                self.match_edge(self.matrix[:, 0], tiles)  + \
                self.match_edge(self.matrix[:, -1], tiles)

    def rotateL(self):
        self.matrix = np.rot90(self.matrix)

    def rotateR(self):
        self.matrix = np.flip(np.rot90(self.matrix))

    def flip(self, axis):
        self.matrix = np.flip(self.matrix, axis)

    def edges(self):
        return np.array([self.matrix[0, :],self.matrix[-1, :],self.matrix[:, 0],self.matrix[:, -1]])

def init_corner_match_fun(tile, prev_tile, tile_array, d):
    return tile.match_edge(tile.edges()[0], tile_array) == [] and tile.match_edge(tile.edges()[2], tile_array) == []

def normal_match_fun(tile, prev_tile, tile_array, d):
    return  np.all(prev_tile.edges()[1 if d[0] else 3] == tile.edges()[0 if d[0] else 2]) or \
            np.all(prev_tile.edges()[0 if d[0] else 2] == tile.edges()[1 if d[0] else 3]) 

def field_match_fun(k):
    return lambda tile, prev_tile, tile_array, d: np.sum(sg.convolve2d(tile.matrix, k) == np.sum(k))

def match_tile_rotation(tile, prev_tile, tile_array, d,  match_fun):
    if match_fun(tile, prev_tile, tile_array, d): return tile
    for i in range(4):
        tile.rotateL()
        if match_fun(tile, prev_tile, tile_array, d): return tile
        tile.flip(0)
        if match_fun(tile, prev_tile, tile_array, d): return tile
        tile.flip(0)
        tile.flip(1)
        if match_fun(tile, prev_tile, tile_array, d): return tile
        tile.flip(1)

with open("input.txt") as file:
    tile_array = [Tile(block) for block in file.read().split("\n\n")]
    tiles = {tile.id: tile for tile in tile_array}
    edges = {tile.id: tile.match_edges(tile_array) for tile in tile_array}
    corners = [tile.id for tile in tile_array if len(edges[tile.id]) == 2]
    curr, prev = match_tile_rotation(tiles[corners[0]], None, tile_array, None, init_corner_match_fun), None

    parts = [[None] * int(sqrt(len(tile_array))) for _ in range(int(sqrt(len(tile_array))))]
    parts[0][0] = curr
    visited = set([curr.id])
    ind = [0,0]
    d = [(-1, 0), (1, 0),  (0, -1), (0, 1)]

    out = np.zeros((int(sqrt(len(tile_array))) * 8, int(sqrt(len(tile_array))) * 8))

    while visited != tiles.keys():
        for i in range(4):
            matched = curr.match_edge(curr.edges()[i], tile_array)
            if len(matched) > 0 and matched[0] not in visited:
                tmp = True
                ind[0] += d[i][0]
                ind[1] += d[i][1]
                visited.add(matched[0])
                prev = curr
                curr = match_tile_rotation(tiles[matched[0]], prev, tile_array, d[i], normal_match_fun) 
                parts[ind[0]][ind[1]] = curr
                break

    for i in range(len(parts)):
        for j in range(len(parts)):
            out[i*8:(i+1)*8, j*8:(j+1)*8] = parts[i][j].matrix[1:-1, 1:-1]

    k = np.array([
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
        [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],
        [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],
    ])

    a = Tile("")
    a.matrix = out
    match_tile_rotation(a, None, None, None, field_match_fun(k))
    print(prod(corners))
    print(int(np.sum(a.matrix) - np.sum(k) * field_match_fun(k)(a, None, None, None)))
