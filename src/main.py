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
                number_spam_line = Text(screen, pygame.font.SysFont("Lucida Console", 18), "    ", (20, y + 20))
                screen.add_component(number_spam_line)

                for __ in range(65):
                    number_spam_line.set_text(number_spam_line.get_text() + str(randint(0, 1)))

                number_spam_line.draw()
                screen.render()

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

        def show_troll_messages() -> None:
            def new_stage(percentages: dict, y_position: int) -> None:
                troll_message = Text(screen, pygame.font.SysFont("Helvetica", 26), "", (20, 75 + y_position))
                screen.add_component(troll_message)

                # in case of user quits before text has finished drawing
                try:
                    for current_percentage in range(101):
                        message = ""

                        for percentage in percentages:
                            if current_percentage <= percentage:
                                message = percentages[percentage]

                        troll_message.set_text(f"{message}{current_percentage}% complete")

                        screen.clear()
                        screen.render()
                        sleep(randint(10, 90) / 100)

                except pygame.error:
                    pass

            for i in range(3):
                if i == 0:
                    new_stage({
                        100: "Publishing your credit card information... ",
                        75: "Retrieving credit card password... ",
                        50: "Saving credit card information... ",
                        25: "Retrieving credit card information... ",
                    }, 30 * i)

                elif i == 1:
                    new_stage({
                        100: "Sending browser history to: MOM, GRANDMA... ",
                        75: "Formatting browser history... ",
                        50: "Reading browser history... ",
                        25: "Downloading browser history... ",
                    }, 30 * i)

                elif i == 2:
                    new_stage({
                        100: "Changing your steam account password... ",
                        75: "Cracking steam account... ",
                        50: "Downloading games passwords... ",
                        25: "Downloading games data... ",
                    }, 30 * i)

            cya_message = Text(screen, pygame.font.SysFont("Helvetica", 26), "Thanks and have a nice day!", (20, 165))
            screen.add_component(cya_message)
            screen.clear()
            screen.render()

        screen.add_thread(show_troll_messages, 0)
        screen.set_exit_callback(on_exit)

        screen.render()
        screen.mainloop()

    screen.add_thread(spam_hacker_number, 2)
    screen.set_exit_callback(on_exit)

    screen.render()
    screen.mainloop()


if __name__ == "__main__":
    main()
