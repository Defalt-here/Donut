import pygame as pg
import numpy as np
from math import sin,cos,pi
WIDTH = 800
HEIGHT = 800

BLACK = (0,0,0)
GREEN = (0,255,0)
PINK = (255,20,147)
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH,HEIGHT))

class Projection:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((width,height))
        self.background = BLACK
        self.surfaces = {}
    def add_surface(self,name,surface):
        self.surfaces[name] = surface
    def display(self):
        for surface in self.surfaces.values():
            for node in surface.nodes:
                pg.draw.circle(self.screen, GREEN,(WIDTH/2 + int(node[0]), HEIGHT/2 + int(node[2])),2)
    def rotate_xyz(self,theta):
        for surface in self.surfaces.values():
            center = surface.find_center()
            c = np.cos(theta)
            s = np.sin(theta)

            if theta == spin_x:
                matrix = np.array([
                    [1,0,0,0],
                    [0,c,0,-s],
                    [0,s,c,0],
                    [0,0,0,1]
                ])
                surface.rotate(center,matrix)
            elif theta == spin_y:
                matrix = np.array([
                    [c,0,s,0],
                    [0,1,0,0],
                    [-s,0,c,0],
                    [0,0,0,1]
                    ])
                surface.rotate(center,matrix)
            elif theta == spin_z:
                matrix = np.array([
                    [c,-s,0,0],
                    [s,c,0,0],
                    [0,0,1,0],
                    [0,0,0,1]
                    ])
                surface.rotate(center,matrix)
class Object:
    def __init__(self):
        self.nodes = np.zeros((0,4))
    def add_nodes(self,node_array):
        ones_column = np.ones((len(node_array),1))
        ones_added = np.hstack((node_array,ones_column))
        self.nodes = np.vstack((self.nodes, ones_added))
    def find_center(self):
        mean = self.nodes.mean(axis=0)
        return mean
    def rotate(self,center,matrix):
        for i, node in enumerate(self.nodes):
            self.nodes[i] = center + np.matmul(matrix,node-center)
xyz = []
# Cube
# def maker(x,y,z):
#     coord = (x,y,z)
#     xyz.append(coord)
    
# maker(-100,100,100)
# maker(-100,100,-100)
# maker(100,100,-100)
# maker(100,100,100)
# maker(-100,-100,100)
# maker(-100,-100,-100)
# maker(100,-100,-100)
# maker(100,-100,100)
R1 = 70
R2 = 140
#donut
for theta in np.arange(0,2*pi,0.4):
    for phi in np.arange(0,2*pi,0.15):
        x = int((R2+R1 * cos(theta))*cos(phi))
        y = int(R1 * sin(theta))
        z = int((R2+R1*cos(theta))*sin(phi))
        xyz.append((x,y,z))
spin_x = 0;
spin_y = 0;
spin_z = 0;
running = True
while running:
    clock.tick(60)
    pv = Projection(WIDTH,HEIGHT)
    object = Object()
    object.add_nodes(np.array(xyz))
    pv.add_surface('object',object)
    pv.rotate_xyz(spin_x)
    pv.rotate_xyz(spin_y)
    pv.rotate_xyz(spin_z)
    pv.display()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.update()
    spin_x += 0.01;
    spin_y += 0.01;
    spin_z += 0.01;