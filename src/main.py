import pygame
from time import sleep
from random import randint

from screen import Screen
from text import Text


def main():
    screen = Screen((850, 600))
    pygame.display.set_caption("WARNING!!!")
    pygame.display.set_icon(pygame.image.load("./warning-icon.png"))

    # adding title
    screen.add_component(Text(screen, pygame.font.SysFont("Helvetica", 36),
                              "                     YOUR PC HAS BEEN INFECTED!!!", (20, 20), color=(255, 0, 0)))

    def spam_hacker_number():
        y = 40

        # in case of user quits before text has finished drawing
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
        sleep(3)

        # noinspection PyShadowingNames
        screen = Screen((850, 600))
        pygame.display.set_caption("ur ded boi")
        pygame.display.set_icon(pygame.image.load("./dead-icon.png"))

        # adding title
        screen.add_component(Text(screen, pygame.font.SysFont("Helvetica", 36),
                                  "                       DO NOT CLOSE THIS WINDOW!!!", (20, 20), color=(255, 0, 0)))

        def show_troll_message():
            troll_message = Text(screen, pygame.font.SysFont("Helvetica", 26), "", (20, 75))
            screen.add_component(troll_message, False)

            # percentage : what message will be displayed under that percentage
            percentages = {
                100: "Sending browser history to: MOM, GRANDMA... ",
                75: "Downloading browser history... ",
                50: "Stealing credit card numbers... ",
                25: "Stealing passwords... ",
            }

            # in case of user quits before text has finished drawing
            try:
                for i in range(101):
                    message = ""

                    for percentage in percentages:
                        if i < percentage:
                            message = percentages[percentage]

                    troll_message.set_text(f"{message}{i}% complete")

                    sleep(0.1)

            except pygame.error:
                pass

        screen.add_thread(show_troll_message, 0)
        screen.set_exit_callback(on_exit)

        screen.mainloop()

    screen.add_thread(spam_hacker_number, 2)
    screen.set_exit_callback(on_exit)

    screen.mainloop()


if __name__ == "__main__":
    main()
