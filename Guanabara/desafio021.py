# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygamer.mixer.music.load('ex021.mp3')
pygamer.mixer.music.play()
pygame.event.wait()