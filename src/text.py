import pygame
from screen import Screen


class Text:
    def __init__(self, screen: Screen, font: pygame.font.Font, text: str, coordinates: tuple,
                 color: tuple = (35, 250, 35)):
        self.__screen__ = screen
        self.__font__ = font
        self.__text__ = text
        self.__coordinates__ = coordinates
        self.__color__ = color

        self.draw()

    def draw(self):
        self.__screen__.get_screen().blit(self.__font__.render(str(self.__text__)), True, self.__color__,
                                          self.__coordinates__)
        pygame.display.update()
