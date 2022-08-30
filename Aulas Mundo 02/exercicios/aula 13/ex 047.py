from time import sleep
for c in range(1, 50):
    if (c%2) == 0:
        print('{:2} é par'.format(c))
    sleep(0.10)
