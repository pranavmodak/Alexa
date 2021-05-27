# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:33:15 2021

@author: modak_ng8awn0
"""

import pygame
import sys
h=1000
w=1000
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('Covexa')
aaaaaa=pygame.movie.load("alexa/"+ "aaaaaa" +".mp4").convert_alpha()
screen.blit(aaaaaa,(0,0))
pygame.display.update()
pygame.init()
clo_obj=pygame.time.Clock()
movie=pygame.movie.Movie("movie_aaaa.mp4")
sur_obj=pygame.display.set_mode(movie.get_size())
mov_scre=pygame.Surface(movie.get_size()).convert()
movie.set_display(mov_scre)
movie.play()
while True:
    for eve in pygame.event.get():
        if eve==pygame.QUIT:
            movie.stop()
            pygame.quit()
            sys.exit()
    sur_obj.blit(mov_scre,(0,0))
    pygame.display.update()
    clo_obj.tick(60)