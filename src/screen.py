import pygame
from threading import Thread
from time import sleep


# pygame screen controller class
class Screen:
    def __init__(self, size=(200, 200)) -> None:
        pygame.init()
        self.__screen = pygame.display.set_mode(size)
        self.__components = []
        self.__threads = []
        self.__exit_callback = lambda: 0

        self.clear()

    def __del__(self) -> None:
        try:
            self.destroy()

        except any:
            pass

    def get_screen(self) -> pygame.Surface:
        return self.__screen

    # noinspection PyMethodMayBeStatic
    def destroy(self) -> None:
        pygame.quit()

    def clear(self) -> None:
        self.__screen.fill((0, 0, 0))

    def render(self) -> None:
        for component in self.__components:
            try:
                component.draw()

            except NameError:
                pass

        self.update()

    # noinspection PyMethodMayBeStatic
    def update(self) -> None:
        pygame.display.update()

    def add_component(self, component: any) -> None:
        self.__components.append(component)

    def remove_component(self, component: any) -> None:
        self.__components.remove(component)

    def add_thread(self, thread: any, timeout: int) -> None:
        def _() -> None:
            sleep(timeout)
            thread()

        self.__threads.append(_)

    def set_exit_callback(self, exit_callback: any) -> None:
        self.__exit_callback = exit_callback

    def mainloop(self) -> None:
        # starts all threads
        for thread in self.__threads:
            Thread(target=thread).start()

        while True:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.destroy()

                    # in case of exit function fails (window can be already closed)
                    try:
                        self.__exit_callback()

                    except any:
                        pass

                    return None
