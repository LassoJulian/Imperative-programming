import pygame, sys
import random
from button import Button


#Presented by Julian Lasso
#228431-3743
#Hope you like it

Background = pygame.image.load("Background.png")

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 69, 0)
lightskyblue = (135, 206, 250)


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

pygame.init()

pygame.display.set_caption("Endless Snake -Main Menu")
score_font = pygame.font.SysFont("comicsansms", 35)

ventanajuego = pygame.display.set_mode((1280,720))

def mostrarPuntajepj1(puntos):
    mensaje1 = get_font(45).render("Score: " + str(puntos), True, yellow)
    ventanajuego.blit(mensaje1, [10, 0])

def mostrarPuntajepj2(puntos):
    mensaje1 = get_font(45).render("Score: " + str(puntos), True, blue)
    ventanajuego.blit(mensaje1, [600, 600])


def overlaysingle():
    mensaje2 = get_font(45).render("The game will begin once you eat your first food", True, black)
    mensaje3 = get_font(45).render("eat your first food", True, black)
    ventanajuego.blit(mensaje2, [10,500])
    ventanajuego.blit(mensaje3, [10, 560])

def overlaysingle1():
    mensaje1 = get_font(45).render("GOOD LUCK!", True, black)
    ventanajuego.blit(mensaje1, [600,300])

def overlaysingle2():
    mensaje1 = get_font(45).render("Your time: ", True, black)
    ventanajuego.blit(mensaje1, [0,600])


def Multiplayer():


    ventanajuego.fill(white)
    pygame.display.set_caption("Endless snake - Multiplayer")
    pygame.display.update()
    clock = pygame.time.Clock()

    continuar = True




    x1 = random.randrange(0, 600, 10)
    y1 = random.randrange(0, 400, 10)
    snake = pygame.draw.rect(ventanajuego, green, [x1, y1, 10, 10])

    desplazamiento_X = 0
    desplazamiento_Y = 0

    x1_comida = random.randrange(0, 600, 10)
    y1_comida = random.randrange(0, 400, 10)
    pygame.draw.rect(ventanajuego, red, [x1_comida, y1_comida, 10, 10])

    x2 = random.randrange(0, 600, 10)
    y2 = random.randrange(0, 400, 10)
    snake = pygame.draw.rect(ventanajuego, green, [x2, y2, 10, 10])

    puntospj1 = 0
    puntospj2 = 0
    mostrarPuntajepj1(0)
    pygame.display.update()





    while (continuar == True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuar = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    desplazamiento_X = -10
                    desplazamiento_Y = 0

                elif event.key == pygame.K_RIGHT:
                    desplazamiento_X = 10
                    desplazamiento_Y = 0

                elif event.key == pygame.K_UP:
                    desplazamiento_X = 0
                    desplazamiento_Y = -10

                elif event.key == pygame.K_DOWN:
                    desplazamiento_X = 0
                    desplazamiento_Y = 10


        x1 += desplazamiento_X
        y1 += desplazamiento_Y

        ventanajuego.fill(white)  # para borrar lo que se lleva de recorrido

        mostrarPuntajepj1(puntospj1)
        if (puntospj1==0):
            overlaysingle()
        if (puntospj1==1):
            overlaysingle1()
        pygame.draw.rect(ventanajuego, red, [x1_comida, y1_comida, 10, 10])

        pygame.draw.rect(ventanajuego, green, [x1, y1, 10, 10])
        pygame.display.update()

        if (x1 == x1_comida and y1 == y1_comida):
            puntospj1 += 1
            ventanajuego.fill(black)
            pygame.draw.rect(ventanajuego, green, [x1, y1, 10, 10])
            mostrarPuntajepj1(puntospj1)
            x1_comida = random.randrange(0, 600, 10)
            y1_comida = random.randrange(0, 400, 10)
            pygame.draw.rect(ventanajuego, red, [x1_comida, y1_comida, 10, 10])
            pygame.display.update()


        clock.tick(10)


def Singleplayer():



    ventanajuego.fill(white)
    pygame.display.set_caption("Endless snake - Singleplayer")
    pygame.display.update()
    clock = pygame.time.Clock()


    continuar = True

    x1 = random.randrange(0, 600, 10)
    y1 = random.randrange(0, 400, 10)
    snake = pygame.draw.rect(ventanajuego, green, [x1, y1, 10, 10])

    desplazamiento_X1 = 0
    desplazamiento_Y1 = 0

    x1_comida = random.randrange(0, 600, 10)
    y1_comida = random.randrange(0, 400, 10)
    pygame.draw.rect(ventanajuego, red, [x1_comida, y1_comida, 10, 10])

    x2 = random.randrange(0, 600, 10)
    y2 = random.randrange(0, 400, 10)
    snake = pygame.draw.rect(ventanajuego, orange, [x2, y2, 10, 10])

    desplazamiento_X2 = 0
    desplazamiento_Y2 = 0

    puntospj1 = 0
    puntospj2 = 0
    mostrarPuntajepj1(0)
    mostrarPuntajepj2(0)
    pygame.display.update()

    while (continuar == True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuar = False


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    desplazamiento_X1 = -10
                    desplazamiento_Y1 = 0
                elif event.key == pygame.K_RIGHT:
                    desplazamiento_X1 = 10
                    desplazamiento_Y1 = 0
                elif event.key == pygame.K_UP:
                    desplazamiento_X1 = 0
                    desplazamiento_Y1 = -10
                elif event.key == pygame.K_DOWN:
                    desplazamiento_X1 = 0
                    desplazamiento_Y1 = 10
                elif event.key == pygame.K_a:
                    desplazamiento_X2 = -10
                    desplazamiento_Y2 = 0
                elif event.key == pygame.K_d:
                    desplazamiento_X2 = 10
                    desplazamiento_Y2 = 0
                elif event.key == pygame.K_w:
                    desplazamiento_X2 = 0
                    desplazamiento_Y2 = -10
                elif event.key == pygame.K_s:
                    desplazamiento_X2 = 0
                    desplazamiento_Y2 = 10


        x1 += desplazamiento_X1
        y1 += desplazamiento_Y1
        x2 += desplazamiento_X2
        y2 += desplazamiento_Y2

        ventanajuego.fill(white)  # para borrar lo que se lleva de recorrido
        mostrarPuntajepj1(puntospj1)
        mostrarPuntajepj2(puntospj2)
        if (puntospj1==0 and puntospj2==0):
            overlaysingle()

        if (puntospj1==1 or puntospj2==1):
            overlaysingle1()

        pygame.draw.rect(ventanajuego, red, [x1_comida, y1_comida, 10, 10])

        pygame.draw.rect(ventanajuego, green, [x1, y1, 10, 10])
        pygame.draw.rect(ventanajuego, orange, [x2, y2, 10, 10])
        pygame.display.update()

        if (x1 == x1_comida and y1 == y1_comida):
            puntospj1 += 1
            ventanajuego.fill(black)
            pygame.draw.rect(ventanajuego, green, [x1, y1, 10, 10])
            pygame.draw.rect(ventanajuego, orange, [x2, y2, 10, 10])
            mostrarPuntajepj1(puntospj1)
            x1_comida = random.randrange(0, 600, 10)
            y1_comida = random.randrange(0, 400, 10)
            pygame.draw.rect(ventanajuego, red, [x1_comida, y1_comida, 10, 10])
            pygame.display.update()

        if (x2 == x1_comida and y2 == y1_comida):
            puntospj2 += 1
            ventanajuego.fill(black)
            pygame.draw.rect(ventanajuego, green, [x1, y1, 10, 10])
            pygame.draw.rect(ventanajuego, orange, [x2, y2, 10, 10])
            mostrarPuntajepj2(puntospj2)
            x1_comida = random.randrange(0, 600, 10)
            y1_comida = random.randrange(0, 400, 10)
            pygame.draw.rect(ventanajuego, red, [x1_comida, y1_comida, 10, 10])
            pygame.display.update()






        clock.tick(10)



def Credits():

    while True:
        pygame.display.set_caption("Endless snake - Credits")
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        ventanajuego.fill("white")

        CREDITS_TEXT = get_font(45).render("This is endless Snake.", True, "Black")
        CREDITS_TEXT2 = get_font(45).render("Game by Julian Lasso", True, "Black")
        CREDITS_TEXT3 = get_font(45).render("Code 2228431, Univalle", True, "Black")
        CREDITS_RECT3 = CREDITS_TEXT.get_rect(center=(640, 480))
        CREDITS_RECT2 = CREDITS_TEXT.get_rect(center=(640, 320))
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(640, 160))
        ventanajuego.blit(CREDITS_TEXT, CREDITS_RECT)
        ventanajuego.blit(CREDITS_TEXT2, CREDITS_RECT2)
        ventanajuego.blit(CREDITS_TEXT3, CREDITS_RECT3)


        OPTIONS_BACK = Button(image=None, pos=(640, 640),
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(ventanajuego)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    pygame.mixer.music.load("doppler.mp3")
    pygame.mixer.music.play()
    while True:
        ventanajuego.fill(black)
        pygame.display.set_caption("Endless snake - Main Menu")
        ventanajuego.blit(Background, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        SINGLEPLAYER_BUTTON = Button(image=pygame.image.load("Credits Rect.png"), pos=(640, 250),
                            text_input="MULTIPLAYER", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
        MULTIPLAYER_BUTTON = Button(image=pygame.image.load("Credits Rect.png"), pos=(640, 400),
                             text_input="SINGLE PLAYER", font=get_font(75), base_color="#d7fcd4",
                             hovering_color="Green")
        CREDITS_BUTTON = Button(image=pygame.image.load("Single Player Rect.png"), pos=(960, 550),
                            text_input="CREDITS", font=get_font(75), base_color="#d7fcd4", hovering_color="Yellow")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(200, 550),
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Red")

        ventanajuego.blit(MENU_TEXT, MENU_RECT)

        for button in [SINGLEPLAYER_BUTTON,MULTIPLAYER_BUTTON ,CREDITS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(ventanajuego)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SINGLEPLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Singleplayer()
                if MULTIPLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Multiplayer()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Credits()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()





      
