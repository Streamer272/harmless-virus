import pygame


class Screen:
    def __init__(self, size=(200, 200)):
        pygame.init()
        self.__screen__ = pygame.display.set_mode(size)
        self.__components__ = []

    def clear(self):
        self.__screen__.fill((0, 0, 0))

        for component in self.__components__:
            # noinspection PyBroadException
            try:
                component.draw()

            except:
                pass

    # noinspection PyMethodMayBeStatic
    def update(self):
        pygame.display.update()

    def get_screen(self):
        return self.__screen__

    # noinspection PyMethodMayBeStatic
    def destroy(self):
        pygame.quit()

    def add_component(self, component):
        self.__components__.append(component)

    def remove_component(self, component):
        self.__components__.pop(self.__components__.index(component))
