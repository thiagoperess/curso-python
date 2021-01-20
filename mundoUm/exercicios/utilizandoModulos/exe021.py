# EXERCICIO 021

# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# SOLUÇÃO

import pygame
pygame.init()
pygame.mixer.music.load('exe021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
