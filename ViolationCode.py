## KISS - Keep It Simple, Stupid Model: Calculator
class HorribleCalculator:
    def __init__(self, user_input_x_value, user_input_y_value):
        self.user_input_x_value = user_input_x_value
        self.user_input_y_value = user_input_y_value

    def mathCalculator_AdditionCalculation(self):
        if self.user_input_x_value < 0:
            return
        elif self.user_input_y_value < 0:
            return
        else:
            return self.input1 + self.input2

    def mathCalculator_SubtractionCalculation(self):
        SubtractionResult = self.user_input_x_value - self.user_input_y_value
        return SubtractionResult

    def multiply(self):
        if self.user_input_x_value == 0:
            return 0
        elif self.user_input_y_value == 0:
            return 0
        else:
            return self.user_input_x_value * self.user_input_y_value

    def divide(self):
        if self.user_input_x_value == 0:
            return 0
        elif self.user_input_y_value == 0:
            return
        else:
            return self.user_input_x_value / self.user_input_y_value