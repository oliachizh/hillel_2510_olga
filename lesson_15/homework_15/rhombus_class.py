class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a # > 0
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == 'side_a' and value <= 0:
            raise AttributeError("Side of the rhombus cant be <=0")
        elif key =='angle_a' and (value >= 180 or value <= 0):
            raise AttributeError("Angle cant be Greater Than or Equal to 180° or Less/Equal to 0°")

        if key == 'angle_a':
            super().__setattr__('angle_b', 180-value)
            super().__setattr__('angle_c', value)
            super().__setattr__('angle_d', 180- value)
        if key not in ['side_a', 'angle_a']:
            raise AttributeError("Invalid attr")

        super().__setattr__(key, value)

    def __str__(self):
        return (f"Rhombus side_a = {self.side_a}, "
                f"angle_a = {self.angle_a}, "
                f"angle_b = {self.angle_b}, "
                f"angle_d = {self.angle_d}, "
                f"angle_c = {self.angle_c} ")


rhombus_1 = Rhombus(40, 80)
rhombus_1.angle_a = 40
print(rhombus_1)




