import pygame

pygame.init()
print('Found ' + str(pygame.joystick.get_count()) + ' joysticks.')
controller = pygame.joystick.Joystick(0)
controller.init()

while True:
    for event in pygame.event.get():
        print(event)