"""inisilizing lib"""
import pygame
pygame.init()

"""making height of window"""
h=600
w=600

"""setting screen"""
screen=pygame.display.set_mode((h,w))

"""displaying image"""
pygame.display.set_caption("display image")
dispimg=pygame.image.load("Images/image1.jpg")
screen.blit(dispimg,(0,0))
eventstatus="None"
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            eventstatus="QUIT"
            break
        
    if eventstatus =="QUIT":
        break
print("closing")