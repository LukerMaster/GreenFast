import pygame

import CircleGame.components as cp


class KeyboardInputManager:

    controller = cp.GameInputs()

    def get_controls(self):
        inputs = cp.RawInputs()
        """Returns a gamecontrols object from keyboard inputs"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            inputs.left = 1
        if keys[pygame.K_RIGHT]:
            inputs.right = 1
        if keys[pygame.K_UP]:
            inputs.up = 1
        if keys[pygame.K_DOWN]:
            inputs.down = 1
        pygame.event.pump()
        self.controller.give_inputs(inputs)

        return self.controller
