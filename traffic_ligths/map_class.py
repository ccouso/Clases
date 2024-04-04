class Map():
    
    def __init__(self, len_x, array_traffic_light, car) -> None:
        self.len_x = len_x
        self.array_traffic_light = array_traffic_light
        self.car = car
        self.init_map()
        pass

    def time_iteration(self):
        for traffic_light in self.array_traffic_light:
            traffic_light.time_iteration()
        if self.car.location + 1 < self.len_x:
            if self.check_traffic_light():
                self.car.move_car()
 
    def check_traffic_light(self):
        for traffic_light in self.array_traffic_light:
            if traffic_light.location == self.car.location + 1:
                if traffic_light.get_color() == 'R' or traffic_light.get_color() == 'O':
                    return False
        return True

    def draw_map(self):
        self.init_map()
        self.draw_car()
        self.draw_traffic_light()
        print(''.join(self.map))

    def init_map(self):
        self.map = []
        for i in range(self.len_x):
            self.map.append('.')

    def draw_car(self):
        for i in range(self.len_x):
            if i == self.car.location:
                self.map[i] = 'C'
    
    def draw_traffic_light(self):
        for traffic_light in self.array_traffic_light:
            if self.map[traffic_light.location] != 'C':
                self.map[traffic_light.location] = traffic_light.get_color()