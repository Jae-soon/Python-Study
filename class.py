# # 마린
# name = "마린"
# hp = 40
# damage = 5

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# #탱크
# tank_name = "시즈탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# # 탱크2
# tank_name2 = "시즈탱크"
# tank_hp2 = 150
# tank_damage2 = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name2))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp2, tank_damage2))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 공격합니다. [공격력 : {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "11시", tank_damage)
# attack(tank_name2, "11시", tank_damage2)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # 멤버 변수(클래스 내에서 정의된 변수)
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(hp, damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("시즈탱크", 150, 35)
wraith1 = Unit("레이스", 80, 5)

# 클래스 외부에서 멤버변수를 사용할 수 있음
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 클로킹
wraith2 = Unit("레이스", 80, 5)
# 클래스 외부에서 객체에 멤버 변수 추가
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))