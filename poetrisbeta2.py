import pygame
import random

from pygame.locals import K_ESCAPE, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE

pygame.init()
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 15
fuente = pygame.font.Font(None, 30)

WIDTH = 1200
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])

jugando = True
pos_x = int(WIDTH / 2)
pos_y = int(HEIGHT / 2)
#try:
 #   rojo = int(input("un numero del 1 al 255: "))
  #  verde = int(input("otro: "))
  #  azul = int(input("y otro mas: "))
  #  colorpelota = (rojo,verde,azul)
#except:
    #colorpelota = (211,110,112)
colorpelota = (211,110,112)
#try: 
    #radio = int(input("¿cuantos años tenes? "))
#except:
    #radio = 30
radio = 30
#try:
    #velocidad = int(input("un número entre el 10 y el 20 "))
#except:
   # velocidad = 18
velocidad = 18

#try:
#    texto = input ("que palabras queres usar?: ")
#except: 
   # texto = "miro conozco contemplo busco se que no es soy un una une amigue ciega detras de casa chancho recorrido malvones sol somos crezco grito escucho al a la enredadera escupo gallina soy muro pared brote plantas mate valiente fuerte baldosas abrazo manos vacia amada gota lluvia barro tierra la la la la el el el un un un un una una una esto esta"

texto = "? ¿ ! ¡ , , , , , , , , . . . . . ( ) , ? ¡ ¿ un máquina una es esto que digo lo que mas me interesa es contemplar el vacio existencial de la mirada perdida el bisonte aca no me sumerjo en atrocidades mas bien me invento mi propio rugido estrepitoso como la noche aguardiente aguardenada de la solitaria tarea de encontrarme presente en el cipayo extremos del lodo antiguo y torturado como una magnolia fluorescente miro conozco contemplo busco se que no es soy un una une amigue ciega detras de casa chancho recorrido malvones sol somos crezco grito escucho al a la enredadera escupo gallina soy muro pared brote plantas mate valiente fuerte baldosas abrazo manos vacia amada gota lluvia barro tierra la la la la el el el un un un un una una una esto esta"
lista = texto.split()
lista1 = []
lista2 = []
lista3 = []
#try:
   # verso1 = int(input("¿cuántas palabras tendrá el primer verso?")) - 1
#except: 
  #  verso1 = 2
#try:
   # verso2 = int(input("¿cuántas palabras tendrá el segundo?")) - 1
#except: 
   # verso2 = 2
#try:
   # verso3 = int(input("¿y el tercero?")) - 1
#except: 
 #   verso3 = 2
verso1 = 2
verso2 = 2
verso3 = 2

frame = 0

while jugando:
    frame += 1

    for event in pygame.event.get():

        # procesar eventos

        # TODO: ver si alt f4 cierra el programa
        if event.type == pygame.QUIT:
            jugando = False
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            jugando = False

    # calcular la nueva posición de los personajes

    pressed_key = pygame.key.get_pressed()

    if pressed_key[pygame.K_UP]:
        pos_y -= velocidad
        if pos_y < 0:
            pos_y = HEIGHT
    elif pressed_key[pygame.K_DOWN]:
        pos_y += velocidad
        if pos_y > HEIGHT: 
            pos_y = 0
    elif pressed_key[pygame.K_RIGHT]:
        pos_x = pos_x + velocidad
        if pos_x > WIDTH:
            pos_x = 0
    elif pressed_key[pygame.K_LEFT]:
        pos_x = pos_x - velocidad
        if pos_x < 0:
            pos_x = WIDTH


    # redibujar pantalla

    colorpantalla = (255, 200, 255)
    screen.fill(colorpantalla)

    if frame == 1:
        palabra = random.choice(lista)
        mensaje = fuente.render(palabra, 1, (0, 0, 0))
        x_random = random.randint(0, WIDTH)
        x_random += 1 and x_random < WIDTH - 2
        y_random = random.randint(0, HEIGHT)
        y_random += 1 and y_random < HEIGHT - 2

    if len(lista1) <= verso1 and pos_x - radio < x_random < pos_x + radio and pos_y - radio < y_random < pos_y + radio:
        linea1 = lista1.append(palabra)
        palabra =  palabra = random.choice(lista)
        mensaje = fuente.render(palabra, 1, (0, 0, 0))
        x_random = random.randint(0, WIDTH)
        x_random += 1 and x_random < WIDTH - 2
        y_random = random.randint(0, HEIGHT)
        y_random += 1 and y_random < HEIGHT - 2
    elif len(lista1) >= verso1 and len(lista2) <= verso2 and pos_x - radio < x_random < pos_x + radio and pos_y - radio < y_random < pos_y + radio:
        linea2 = lista2.append(palabra)
        palabra =  palabra = random.choice(lista)
        mensaje = fuente.render(palabra, 1, (0, 0, 0))
        x_random = random.randint(0, WIDTH)
        x_random += 1 and x_random < WIDTH - 2
        y_random = random.randint(0, HEIGHT)
        y_random += 1 and y_random < HEIGHT - 2
    elif len(lista2) >= verso2 and len(lista3) <= verso3 and pos_x - radio < x_random < pos_x + radio and pos_y - radio < y_random < pos_y + radio:
        linea3 = lista3.append(palabra)
        palabra =  palabra = random.choice(lista)
        mensaje = fuente.render(palabra, 1, (0, 0, 0))
        x_random = random.randint(0, WIDTH)
        x_random += 1 and x_random < WIDTH - 2
        y_random = random.randint(0, HEIGHT)
        y_random += 1 and y_random < HEIGHT - 2
    elif len(lista3) > verso3:
        jugando = False

    if pressed_key[K_SPACE]:
        palabra = random.choice(lista)
        mensaje = fuente.render(palabra, 1, (0, 0, 0))
        x_random = random.randint(0, WIDTH)
        x_random += 1 and x_random < WIDTH - 2
        y_random = random.randint(0, HEIGHT)
        y_random += 1 and y_random < HEIGHT - 2

    linea1 = " ".join(lista1) 
    linea2 = " ".join(lista2) 
    linea3 = " ".join(lista3) 

    puntaje1 = fuente.render(linea1, 15, (0, 0, 0))
    puntaje2 = fuente.render(linea2, 15, (0, 0, 0))
    puntaje3 = fuente.render(linea3, 15, (0, 0, 0))
   
    screen.blit(puntaje1, (15,15))
    screen.blit(puntaje2, (15,31))
    screen.blit(puntaje3, (15,46))
    screen.blit(mensaje, (x_random, y_random))
    pygame.draw.circle(screen, colorpelota, (pos_x, pos_y), radio)
    
    
    pygame.display.flip()
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount
    if frame == FRAMES_PER_SECOND * 5:
        frame = 0
    

pygame.quit()

print (linea1)
print (linea2)
print (linea3)