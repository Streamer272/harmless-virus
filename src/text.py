import pygame
from screen import Screen


class Text:
    def __init__(self, screen: Screen, font: pygame.font.Font, text: str, coordinates: tuple,
                 color: tuple = (35, 250, 35)):
        self.__screen = screen
        self.__font = font
        self.__text = text
        self.__coordinates = coordinates
        self.__color = color

        self.draw()

    def __del__(self):
        self.__screen.remove_component(self)

    def draw(self):
        self.__screen.get_screen().blit(self.__font.render(str(self.__text), True, self.__color), self.__coordinates)
        pygame.display.update()
