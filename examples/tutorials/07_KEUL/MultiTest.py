from multiprocessing import Process
import time

def first_loop(number):
    nb = 1
    for _ in range(number):
        print("First loop number " + str(nb))
        nb += 1

def second_loop(number):
    nb = 1
    for _ in range(number):
        print("Second loop number " + str(nb))
        nb += 1

def process_all():
    p1 = Process(target=first_loop, args=(10,))
    p1.start()

    p2 = Process(target=second_loop, args=(10,))
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    process_all()