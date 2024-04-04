from traffic_light import Traffic_light
from car_class import Car
from map_class import Map

########### Input data #############
iter = 20
intial_car_location = 0
initial_car_velocity = 1
len_map = 20
array_traffic_light = []
traffic_light_location_1 = 3
traffic_light_color_1 = 'RED'
traffic_light_location_2 = 9
traffic_light_color_2 = 'GREEN'
####################################


########### Init classes #############

# Init traffic light array
array_traffic_light.append(Traffic_light(traffic_light_color_1, traffic_light_location_1))
array_traffic_light.append(Traffic_light(traffic_light_color_2, traffic_light_location_2))

# Init car
car = Car(intial_car_location, initial_car_velocity)

# Init map
map = Map(len_map, array_traffic_light, car)

####################################


############## Main ################
for i in range(iter):
    map.time_iteration()
    map.draw_map()