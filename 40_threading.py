import time
import threading

# def task_1(task_number):
#     print(f"task {task_number}  ongoing....")
#     time.sleep(5)
    

# def task_2():
#     time.sleep(5)
#     print("task two ongoing....")


# t1 = threading.Thread(target = task_1, args=[1])
# t1.start()

# t2 = threading.Thread(target = task_2)
# t2.start()



#practice
def func(second):
    print(f"sleeping for {second} seconds")
    time.sleep(second)

# time1 = time.perf_counter()    
# #Normal code
# func(4)
# func(2)
# func(1)
# time2 = time.perf_counter()
# print(time2-time1)

#using thread
time3 = time.perf_counter()
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[8])
t3 = threading.Thread(target=func, args=[1])


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()



time4 = time.perf_counter()
# Calculating Time
print(time4 - time3)
