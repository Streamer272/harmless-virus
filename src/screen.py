import pygame
from threading import Thread
from time import sleep


class Screen:
    def __init__(self, size=(200, 200)) -> None:
        pygame.init()
        self.__screen = pygame.display.set_mode(size)
        self.__components = []
        self.__threads = []

        self.clear()

    def __del__(self) -> None:
        self.destroy()

    def get_screen(self) -> pygame.Surface:
        return self.__screen

    # noinspection PyMethodMayBeStatic
    def destroy(self) -> None:
        pygame.quit()

    def clear(self, render: bool = False) -> None:
        print("additional clear")
        self.__screen.fill((0, 0, 0))
        self.update(render)

    def render(self, clear: bool = True) -> None:
        print("additional render")

        if clear:
            self.clear()

        for component in self.__components:
            try:
                component.draw()

            except:
                pass

        self.update(False)

    def update(self, render: bool = True):
        pygame.display.flip()

        if render:
            self.render()

    def add_component(self, component: any, render: bool = True) -> None:
        self.__components.append(component)

        if render:
            self.render()

    def remove_component(self, component: any, render: bool = True) -> None:
        self.__components.remove(component)

        if render:
            self.render()

    # noinspection PyMethodMayBeStatic
    def add_thread(self, thread: any, timeout: int) -> None:
        def _() -> None:
            sleep(timeout)
            thread()

        self.__threads.append(_)

    def mainloop(self, destroy_after_exit: bool = True) -> None:
        for thread in self.__threads:
            Thread(target=thread).start()

        while True:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    if destroy_after_exit:
                        self.destroy()

                    return None
