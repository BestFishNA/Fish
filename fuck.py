UnitNumber = int(input("Unit Number plox "))

FloorNummy = UnitNumber // 100
UnitNummy = UnitNumber % 100

if 0 < FloorNummy < 13:
    if FloorNummy == 3:
        if 0 < UnitNummy < 9:
            print("its a unit")
        else:
            print("fuck u")
    elif FloorNummy < 8 or FloorNummy == 10:
        if 0 < UnitNummy < 13:
            print("its a unit")
        else: 
            print("fuck u")
    else:
        if 0 < UnitNummy < 15:
            print("its a unit")
        else:
            print("fuck u")
else:
    print("That straight up isnt a floor chief")
