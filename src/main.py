import pygame
from threading import Thread
from time import sleep
from random import randint

from screen import Screen
from text import Text


def draw_text(screen, font, text, coordinates):
    label = font.render(str(text), True, (35, 250, 35))
    screen.blit(label, coordinates)
    pygame.display.update()


def init_main_window(initial_text, after_callback, delete_callback):
    pygame.init()
    screen = pygame.display.set_mode((850, 600))

    pygame.display.set_caption("WARNING!")
    pygame.display.set_icon(pygame.image.load("./warning-icon.png"))
    screen.fill((0, 0, 0))

    font_medium = pygame.font.SysFont("Helvetica", 20, bold=True)
    font_small = pygame.font.SysFont("Helvetica", 16)

    draw_text(screen, font_medium, initial_text, (20, 20))

    Thread(target=after_callback, args=[screen, font_small]).start()

    while True:
        try:
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    Thread(target=delete_callback).start()

        except pygame.error:
            pygame.quit()
            break


if __name__ == "__main__":
    screen = Screen((850, 600))
    pygame.display.set_caption("WARNING!!!")
    pygame.display.set_icon(pygame.image.load("./warning-icon.png"))

    txt1 = Text(screen, pygame.font.SysFont("Helvetica", 32), "Test test", (20, 20))
    txt2 = Text(screen, pygame.font.SysFont("Helvetica", 22), "Test xx", (20, 50))

    screen.add_component(txt1)
    screen.add_component(txt2)

    def _():
        txt2.set_text("xx lmao")

    screen.add_thread(_, 2)

    screen.mainloop()
