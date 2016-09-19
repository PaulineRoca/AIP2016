import pygame, random
from pygame.locals import *
from numpy import *
from math import *

W, H = 500, 500
n_items, mark_items = 8, 3
r, R = 20, 30
speed = 1
bg_col, fg_col, mark_col = (255, 255, 255), (0, 0, 0), (255, 0, 0)

def length(a): return sqrt(dot(a, a))
def distance(a, b): return length(a - b)

def init():
    s = []
    for i in range(n_items):
        while True:
            p = array([random.randint(R, W - R), random.randint(R, H - R)]) # try a position
            ok = True       # check to see if it's too close to any previous object
            for prev in s:  # go through all previous objects
                if distance(p, prev[0]) < 2*R:
                    ok = False  # it's too close, must continue while loop (trying new positions)
                    break
            if ok: break    # if the position is not too close to any previous objects, can stop
        ang = random.uniform(0, 2*pi)   # random direction
        s.append([p, speed*array([cos(ang), sin(ang)])])
    return s

def draw(s, mark = []):
    for i in range(len(s)):
        if i in mark: col = mark_col
        else: col = fg_col
        pygame.draw.circle(surf, col, (int(s[i][0][0]), int(s[i][0][1])), r)

def evolve(s):
    new = []
    for obj in s:
        p = obj[0] + obj[1]     # object advances
        d = obj[1]
        if p[0] < R:
            d[0] *= -1     # check for collisions with vert. walls
            p[0] = R
        if p[0] > W - R:
            d[0] *= -1     # check for collisions with vert. walls
            p[0] = W - R
        if p[1] < R:
            d[1] *= -1     # horiz. walls
            p[1] = R
        if p[1] > H - R:
            d[1] *= -1     # horiz. walls
            p[1] = H - R
        new.append([p, d])
    for i in range(len(new)):       # check for collisions between objects
        for j in range(i):          # go through every distinct pair of objects
            if distance(new[i][0], new[j][0]) < 2*R:       # collision!
                a = new[i][1] + new[j][1]
                a /= length(a)
                new[i][1] = 2*dot(new[i][1], a)*a - new[i][1]
                new[j][1] = 2*dot(new[j][1], a)*a - new[j][1]
    return new

try:
    stim = init()
    pygame.init()
    surf = pygame.display.set_mode((W, H))
    quit, show = False, False
    while not quit:
        for ev in pygame.event.get():
            if ev.type in (QUIT, KEYDOWN): quit = True
            if ev.type == MOUSEBUTTONDOWN: show = True
            if ev.type == MOUSEBUTTONUP: show = False
        surf.fill(bg_col)
        if show: draw(stim, range(mark_items))
        else: draw(stim)
        pygame.display.flip()
        stim = evolve(stim)
finally: pygame.quit()
