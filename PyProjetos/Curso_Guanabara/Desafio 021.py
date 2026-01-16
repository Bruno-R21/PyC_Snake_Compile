# (Desafio 21) Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

import pygame 
pygame.init()

pygame.mixer.music.load('Sorriso.wav')
pygame.mixer.music.play()
pygame.event.wait()

'''import pygame
import os
pygame.init()

if os.path.exists('Sorriso.wav'):
    pygame.mixer.music.load('Sorriso.wav')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)

    clock = pygame.time.clock()
    clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)

else:
    print('O arquivo Sorriso.wav não funcionando')'''

#Infelizmente por problemas de atualização do Python e da descontinuidade da bliblioteca pygame, não consegui fazer o código funcionar.     






