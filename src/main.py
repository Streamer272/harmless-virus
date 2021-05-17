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

    txt1 = Text(screen, pygame.font.SysFont("Helvetica", 36), "                     YOUR PC HAS BEEN INFECTED!!!",
                (20, 20), color=(255, 0, 0))

    screen.add_component(txt1)

    def hacker_number_spam():
        y = 40

        for _ in range(25):
            number_spam_line = Text(screen, pygame.font.SysFont("Helvetica", 18), "    ", (20, y + 20))

            for __ in range(100):
                number_spam_line.set_text(number_spam_line.get_text() + str(randint(0, 1)), False)

            screen.add_component(number_spam_line, False)
            number_spam_line.draw()

            y += 20
            sleep(0.5)

    def on_exit():
        print("exited!!!")

    screen.add_thread(hacker_number_spam, 2)
    screen.set_exit_callback(on_exit)

    screen.mainloop()
