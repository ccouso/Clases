

class Traffic_light():

    def __init__(self, initial_color, location):
        self.color = initial_color
        self.location = location
        self.TIME_TO_CHANGE = 0
        self.set_time_to_change()
        

    def set_time_to_change(self):
        dict_color = {
            'RED': 5,
            'GREEN': 5,
            'ORANGE': 1
            }
        self.TIME_TO_CHANGE = dict_color[self.color]

    def time_iteration(self):
        self.TIME_TO_CHANGE -= 1
        if self.TIME_TO_CHANGE == 0:
            self.change_color()

    def change_color(self):
        if self.color == 'RED':
            self.color = 'GREEN'
        elif self.color == 'GREEN':
            self.color = 'ORANGE'
        elif self.color == 'ORANGE':
            self.color = 'RED'
        self.set_time_to_change()

    def get_color(self):
        if self.color == 'RED':
            return 'R'
        elif self.color == 'GREEN':
            return 'G'
        elif self.color == 'ORANGE':
            return 'O'
        