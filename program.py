import time


def random_number(low_s, high_s):
    return int(low_s + int(time.time() * 1000) % (high_s - low_s))


low = 0
high = 100
count = 0
rand_list = []

print("Press enter for a random number or press q to quit : ")
x = input()
while True:
    sel = ' '
    if sel == 'q':
        break
    rand = random_number(low, high)

    rand_list.append(rand)

    print("%d --> %d" % (count, rand))
    count += 1

print(rand_list)
