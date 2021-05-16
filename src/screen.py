import pygame


class Screen:
    def __init__(self, size=(200, 200)) -> None:
        pygame.init()
        self.__screen = pygame.display.set_mode(size)
        self.__components = []

        self.clear()

    def __del__(self) -> None:
        self.destroy()

    def get_screen(self) -> pygame.Surface:
        return self.__screen

    # noinspection PyMethodMayBeStatic
    def destroy(self) -> None:
        pygame.quit()

    def clear(self, render: bool = False) -> None:
        self.__screen.fill((0, 0, 0))

        if render:
            self.render()

    def render(self, clear: bool = True) -> None:
        if clear:
            self.clear()

        for component in self.__components:
            # noinspection PyBroadException
            try:
                component.draw()

            except:
                pass

    # noinspection PyMethodMayBeStatic
    def update(self, render: bool = True):
        pygame.display.update()

        if render:
            self.render()

    def add_component(self, component: any, render: bool = True) -> None:
        self.__components.append(component)

        if render:
            self.render()

    def remove_component(self, component: any, render: bool = True) -> None:
        self.__components.pop(self.__components.index(component))

        if render:
            self.render()

    # noinspection PyMethodMayBeStatic
    def mainloop(self, destroy_after_exit: bool = True) -> None:
        while True:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    if destroy_after_exit:
                        self.destroy()

                    return None
