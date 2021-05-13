import pygame
from threading import Thread
from time import sleep
from random import randint


def draw_text(screen, font, text, coordinates):
    label = font.render(str(text), True, (35, 250, 35))
    screen.blit(label, coordinates)
    pygame.display.update()


def init_main_window(initial_text, after_callback, delete_callback):
    pygame.init()
    screen = pygame.display.set_mode((850, 600))

    pygame.display.set_caption("WARNING!")
    pygame.display.set_icon(pygame.image.load("../warning-icon.png"))
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


if __name__ == '__main__':
    def after(screen, font):
        sleep(3)

        # start numbers spam

    def delete():
        sleep(3)

        def after_(screen_, font_):
            global x

            # draw_text(screen_, font_, "Stealing user data... 25%", (20, 50))
            # sleep(1)
            # draw_text(screen_, font_, "Stealing user passwords... 50%", (20, 70))
            # sleep(1)
            # draw_text(screen_, font_, "Downloading browser history... 75%", (20, 90))
            # sleep(1)
            # draw_text(screen_, font_, "Sending browser history to MOM... 100%", (20, 110))

            x = 0
            label = font_.render(str(f"xx {x}"), True, (35, 250, 35))
            screen_.blit(label, (20, 50))

            def x_(screen__, font__):
                global x

                while True:
                    screen__.fill((0, 0, 0))
                    label = font_.render(str(f"xx {x}"), True, (35, 250, 35))
                    screen_.blit(label, (20, 50))
                    x += 1
                    print("Updated x to " + str(x))
                    sleep(1)

            Thread(target=x_, args=[screen_, font_]).start()

        def delete_():
            delete()

        Thread(target=init_main_window, args=["DON'T CLOSE THIS WINDOW!!!", after_, delete_]).start()

    Thread(target=init_main_window, args=["YOUR PC HAS A VIRUS!!!", after, delete]).start()
