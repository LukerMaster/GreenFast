class RawInputs:
    left = 0
    right = 0
    up = 0
    down = 0
    esc = 0

class GameInputs:
    _x_axis = 0.0
    _y_axis = 0.0
    esc = False

    def _set_axis_vals(self, x, y):

        length = (x**2 + y**2)**0.5

        if length != 0 and length > 1:
            x /= length
            y /= length

        self._x_axis = x
        self._y_axis = y

    def give_direct_input(self, x_axis, y_axis, esc):
        """Give inputs by directly giving values"""
        self._set_axis_vals(x_axis, y_axis)
        self.esc = esc

    def give_inputs(self, inputs):
        """Give inputs by Inputs object"""
        self._set_axis_vals(inputs.down - inputs.up, inputs.right - inputs.left)
        self.esc = inputs.esc

    def get_axis_vals(self):
        """Used by the game itself to move the circles"""
        return self._x_axis, self._y_axis
