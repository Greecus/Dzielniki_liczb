import time
from threading import Thread
import multiprocessing
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

def find_deviders(n:int):
    deviders=[]
    for i in range(1,int(n/2+1)):
        if n%i==0:
            deviders.append(i)
    deviders.append(n)
    logger.debug(deviders)
    #return deviders

if __name__ == '__main__':
    start=time.time()
    for n in (128, 255, 99999, 10651060):
        find_deviders(n)
    end=time.time()
    duration_normal=end-start

    start=time.time()
    threads=[]
    for n in (128, 255, 99999, 10651060):
        thread=Thread(target=find_deviders,args=(n, ))
        thread.start()
        threads.append(thread)
    [el.join() for el in threads]
    end=time.time()
    duration_threading=end-start

    start=time.time()
    threads=[]
    for n in (128, 255, 99999, 10651060):
        thread=multiprocessing.Process(target=find_deviders,args=(n, ))
        thread.start()
        threads.append(thread)
    [el.join() for el in threads]
    end=time.time()
    duration_processes=end-start

    print(f"Duration threading:{duration_threading}\nDuration normal:{duration_normal}\nDuration processes:{duration_processes}")