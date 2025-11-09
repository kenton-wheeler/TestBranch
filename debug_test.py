def accelerate(speed):
    print("Accelerating...")
    speed += 5
    return speed

def brake(speed):
    print("Braking...")
    speed -= 5
    return speed

def step(miles):
    miles += 1
    return miles

if __name__ == '__main__':

    speed = 0
    miles = 0
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                        "or [S]top: ").upper()
        if action not in "ABS" or len(action) != 1:
            print("Invalid command")
            continue
        if action == 'A':
            speed = accelerate(speed)
        elif action == 'B':
            speed = brake(speed)
        elif action == 'S':
            print(f"You travelled {miles} miles with a current speed of {speed}")
            break
        miles = step(miles)
