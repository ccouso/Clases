class Car():
    def __init__(self, location, vel) -> None:
        self.location = location
        self.vel = vel
        pass

    def move_car(self):
        self.location += self.vel
        pass
