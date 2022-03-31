class Car():
    max_speed = 300
    max_people = 5

    def start(self):
        print('START==')

    def stop(self):
        print('STOOOOP!!')

    # magic method
    def __str__(self):
        return 'hello world'

    #
    def __init__(self):
        print('instance has made')


k9 = Car()
k5 = Car()
k3 = Car()


class Hybrid(Car):
    battery = 1000
    battery_km = 300


print(k9)
