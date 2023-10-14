import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,580))
screen_caption = pygame.display.set_caption("Mashapa Developmenet")
clock = pygame.time.Clock()
test_surface = pygame.image.load('cartoon_road-1024x576.jpg')

car_surface = pygame.image.load('car3-removebg-preview (1).png')

car2_surf = pygame.image.load('blue_car-removebg-preview (1).png')
car_pos_x = 2
car2_pos_x = 600

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    screen.blit(test_surface,(0,0))
    screen.blit(car2_surf,(car2_pos_x,420))
    car_pos_x += 2
    if car_pos_x > 900 : car_pos_x = 2
    screen.blit(car_surface,(car_pos_x,320))
    car2_pos_x -= 2
    if car2_pos_x < -900: car2_pos_x = 600
    clock.tick(80)