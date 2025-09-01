from threading import Semaphore
import time
import threading
import random

max_c = 10
full = Semaphore(0)
empty = Semaphore(max_c)
mutex = Semaphore(1)

queue = []

def producer(i):
    empty.acquire()
    mutex.acquire()
    print("Produced:", i)
    queue.append(i)
    mutex.release()
    full.release()

def consumer(i):
    full.acquire()
    mutex.acquire()
    item = queue.pop(0)
    print("Consumer has consumed:", item)
    mutex.release()
    empty.release()

total = []

for i in range(max_c):
    tp = threading.Thread(target=producer, args=[i])
    tc = threading.Thread(target=consumer, args=[i])
    total.append(tp)
    total.append(tc)

random.shuffle(total)

for thread in total:
    thread.start()
    time.sleep(1)  # Optional: slows down thread start to better see the output

for thread in total:
    thread.join()

