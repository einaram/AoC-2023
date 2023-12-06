def merge(time_distance_list):
    time, distance = list(zip(*time_distance_list))
    return [(
        int("".join([str(x) for x in time])),int("".join([str(x) for x in distance]))
        )]

time_distance_list_test = [
    (7,9),
    (15,40),
    (30,200),
]

time_distance_list = [
    (56,499),
    (97,2210),
    (77,1097),
    (93,1440),
]

time_distance_list_test2 =   merge(time_distance_list_test) 
time_distance_list2 = merge(time_distance_list) 

# Speed increase per ms hold:
mm_per_ms = 1

races={}
for race_time,max_distance in time_distance_list2:
    races[race_time]=0
    for hold in range(0,race_time+1):
        speed = hold*mm_per_ms
        distance = speed*(race_time-hold)
        if distance > max_distance:
            races[race_time] +=1


import math
print(math.prod(races.values()))