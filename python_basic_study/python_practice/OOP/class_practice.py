# class CAR() 는 사실
# class Car(object) object 가 생략된 것

class Car:
    max_speed = 300
    max_people = 5

    def start(self):
        print('START==')

    def stop(self):
        print('STOOOOP!!')


k9 = Car()

print(k9.max_people)

# class name 첫 문자가 대문자
# class 는 대부분 직접 만지지 않는다
# class -  붕어빵 틀
# instance - 붕어빵


k5 = Car()
k3 = Car()

print(k9.max_people)
print(k3.max_people)
print(type(k9))
print(dir(k9))

