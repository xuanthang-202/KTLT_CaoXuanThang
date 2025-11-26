print("Sinh vien: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("###########################")
#################################
import math
pos = [0, 0]

while True:
    s = input()
    if not s:
        break
    
    try:
        movement = s.split()
        direction = movement[0].upper()
        steps = int(movement[1])
    except (IndexError, ValueError):
        continue

    if direction == "UP":
        pos[1] += steps
    elif direction == "DOWN":
        pos[1] -= steps
    elif direction == "LEFT":
        pos[0] -= steps
    elif direction == "RIGHT":
        pos[0] += steps
    else:
        pass

distance = math.sqrt(pos[0]**2 + pos[1]**2)

print(round(distance))
