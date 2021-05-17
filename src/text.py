import pygame
from screen import Screen


class Text:
    def __init__(self, screen: Screen, font: pygame.font.Font, text: str, coordinates: tuple,
                 color: tuple = (35, 250, 35), draw: bool = True):
        self.__screen = screen
        self.__font = font
        self.__text = str(text)
        self.__coordinates = coordinates
        self.__color = color

        if draw:
            self.draw()

    def __del__(self):
        try:
            self.__screen.remove_component(self)

        except:
            pass

    def draw(self):
        self.__screen.get_screen().blit(self.__font.render(self.__text, True, self.__color), self.__coordinates)
        pygame.display.update()

    def set_text(self, new_text: str) -> None:
        self.__text = str(new_text)
        self.__screen.render()
