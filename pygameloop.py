import pygame


class PygameLoop:
    is_on = True
    desired_dt = 8.33
    __accumulated_dt = 0
    __start_time = 0
    __end_time = 0
    def update_fn(self, dt):
        pass

    def loop(self):
        if not pygame.get_init():
            pygame.init()
        self.__start_time = pygame.time.get_ticks()
        while self.is_on:
            self.__end_time = pygame.time.get_ticks()
            if self.__end_time - self.__start_time > 1:
                self.__accumulated_dt += self.__end_time - self.__start_time
                self.__start_time = self.__end_time

            if self.__accumulated_dt > self.desired_dt:
                self.update_fn(self.__accumulated_dt*0.001)
                self.__accumulated_dt = 0
