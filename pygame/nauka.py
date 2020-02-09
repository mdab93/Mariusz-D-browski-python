import pygame, sys

pygame.init()

# tworzenie okna
screen = pygame.display.set_mode((1280, 720))

# tworzenie zmiennej do przechowywania rozmiarow rysowanego prostokonta
box = pygame.Rect(10, 10, 10, 10)

# petla dzieki ktorej okno sie nie zamyka
while True:

    # zaczytanie komend systemowych (np. zamkniecie okna X)
    for event in pygame.event.get():

        # mozliwosc zamkniecia okna
        if event.type == pygame.QUIT:
            sys.exit(0)

    # zmiana parametrów w zmiennej box
    # box.x +=  1

    # sprawdzenie czy klawisz jest wcisniety
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        box.x += 1
    if keys[pygame.K_LEFT]:
        box.x -= 1
    if keys[pygame.K_UP]:
        box.y -= 1
    if keys[pygame.K_DOWN]:
        box.y += 1

    # ekran główny czyszczony
    screen.fill((0, 0, 0))

    # rysowanie
    pygame.draw.rect(screen, (255, 0, 0), box)
    # rysowanie odbywa się na ukrytej "kartce" zamiana kartek:
    pygame.display.flip()