import pygame
import foundation as fd
import renderer as rd

cube = fd.mesh(
    (
        (0.25, -0.25, -0.25),
        (0.25, 0.25, -0.25),
        (-0.25, 0.25, -0.25),
        (-0.25, -0.25, -0.25),
        (0.25, -0.25, 0.25),
        (0.25, 0.25, 0.25),
        (-0.25, -0.25, 0.25),
        (-0.25, 0.25, 0.25),
    ),
    (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        (5, 7),
    ),
)


queue = rd.renderQueue()
queue.addToQueue(cube)
renderer = rd.renderer(queue)

while True:
    renderer.render()