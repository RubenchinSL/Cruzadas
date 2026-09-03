import pygame

pygame.init()

# --- Configuración del tablero ---
# Este estilo de cruzada suele ser más alto que ancho
FILAS, COLUMNAS = 22, 14
TAM_CASILLA = 26
MARGEN = 2  # separación entre casillas para simular la cuadrícula

ANCHO_TABLERO = COLUMNAS * TAM_CASILLA
ALTO_TABLERO = FILAS * TAM_CASILLA

# --- Zonas de la ventana ---
ALTO_BARRA_TITULO = 40
ANCHO_PANEL_PALABRAS = 220   # columna derecha con las palabras por nº de letras

MARGEN_EXTERIOR = 20  # aire alrededor del tablero

ANCHO_VENTANA = MARGEN_EXTERIOR * 2 + ANCHO_TABLERO + ANCHO_PANEL_PALABRAS
ALTO_VENTANA = ALTO_BARRA_TITULO + MARGEN_EXTERIOR * 2 + ALTO_TABLERO

# Offset: dónde empieza el tablero dentro de la ventana (debajo de la barra, a la izquierda)
OFFSET_X = MARGEN_EXTERIOR
OFFSET_Y = ALTO_BARRA_TITULO + MARGEN_EXTERIOR

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS_FONDO = (235, 235, 235)   # fondo claro, como el papel de la revista
GRIS_BARRA = (90, 90, 90)      # barra de título tipo "CRUZADAS"

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Crucigrama")

# 0 = casilla blanca (se puede escribir), 1 = casilla negra (bloqueada)
tablero = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

# Ejemplo: bloqueamos algunas casillas a mano para probar
tablero[0][2] = 1
tablero[3][5] = 1
tablero[7][7] = 1


def dibujar_tablero():
    pantalla.fill(GRIS_FONDO)  # fondo tipo "papel" de toda la ventana

    # Barra de título superior (tipo "CRUZADAS")
    barra = pygame.Rect(0, 0, ANCHO_VENTANA, ALTO_BARRA_TITULO)
    pygame.draw.rect(pantalla, GRIS_BARRA, barra)

    # Fondo negro solo detrás del tablero, para que sigan viéndose las líneas de la rejilla
    fondo_tablero = pygame.Rect(OFFSET_X, OFFSET_Y, ANCHO_TABLERO, ALTO_TABLERO)
    pygame.draw.rect(pantalla, NEGRO, fondo_tablero)

    for fila in range(FILAS):
        for col in range(COLUMNAS):
            x = OFFSET_X + col * TAM_CASILLA
            y = OFFSET_Y + fila * TAM_CASILLA
            rect = pygame.Rect(x, y, TAM_CASILLA - MARGEN, TAM_CASILLA - MARGEN)
            color = NEGRO if tablero[fila][col] == 1 else BLANCO
            pygame.draw.rect(pantalla, color, rect)

    # El panel de la derecha (lista de palabras por nº de letras) se dibujará
    # más adelante con pygame.font, en el espacio que queda a partir de:
    # x = OFFSET_X + ANCHO_TABLERO + MARGEN_EXTERIOR


reloj = pygame.time.Clock()
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    dibujar_tablero()
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()