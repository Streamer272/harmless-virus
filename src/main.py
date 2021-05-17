import pygame
from time import sleep
from random import randint

from screen import Screen
from text import Text


def main():
    screen = Screen((850, 600))
    pygame.display.set_caption("WARNING!!!")
    pygame.display.set_icon(pygame.image.load("./warning-icon.png"))

    title = Text(screen, pygame.font.SysFont("Helvetica", 36), "                     YOUR PC HAS BEEN INFECTED!!!",
                 (20, 20), color=(255, 0, 0))

    screen.add_component(title)

    def hacker_number_spam():
        y = 40

        # in case of user quiting before text has finished drawing
        try:
            for _ in range(25):
                number_spam_line = Text(screen, pygame.font.SysFont("Helvetica", 18), "    ", (20, y + 20))

                for __ in range(100):
                    number_spam_line.set_text(number_spam_line.get_text() + str(randint(0, 1)), False)

                screen.add_component(number_spam_line, False)
                number_spam_line.draw()

                y += 20
                sleep(0.5)

        except pygame.error:
            pass

    def on_exit():
        print("exited!!!")

    screen.add_thread(hacker_number_spam, 2)
    screen.set_exit_callback(on_exit)

    screen.mainloop()


if __name__ == "__main__":
    main()
