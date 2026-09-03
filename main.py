import pygame

pygame.init()
pantalla = pygame.display.set_mode((800, 600))  # ancho, alto
pygame.display.set_caption("Crucigrama")
reloj = pygame.time.Clock()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    pantalla.fill((255, 255, 255))  # limpiar pantalla (blanco)

    # aquí dibujas todo

    pygame.display.flip()  # actualizar pantalla
    reloj.tick(60)  # limitar a 60 FPS

pygame.quit()