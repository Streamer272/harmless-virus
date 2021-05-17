import pygame
from screen import Screen


# pygame text controller class
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

        except pygame.error:
            pass

    def draw(self) -> None:
        self.__screen.get_screen().blit(self.__font.render(self.__text, True, self.__color), self.__coordinates)
        self.__screen.update(False)

    def set_text(self, new_text: str, render: bool = True) -> None:
        self.__text = str(new_text)

        if render:
            self.__screen.render()

    def get_text(self) -> str:
        return self.__text
