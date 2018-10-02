import pygame

controller = pygame.joystick.Joystick(0)
controller.init()

while True:
    for event in pygame.event.get():
        print(event)