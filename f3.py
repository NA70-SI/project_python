import threading
import time
import sharedState
import f1
from f2 import CreateCustomerElement
from f1 import Lane_services , Lane_situation


customer_ins = CreateCustomerElement()
service_ins = Lane_services()
situation_ins = Lane_situation()
# targeting functions to start thread

# idea of using thread was taken from chat gpt
# Each thread below is responsible for clearing lane.
service_thread1 = threading.Thread(target=service_ins.clearing_regular_lane1)
service_thread2 = threading.Thread(target=service_ins.clearing_regular_lane2)
service_thread3 = threading.Thread(target=service_ins.clearing_regular_lane3)
service_thread4 = threading.Thread(target=service_ins.clearing_regular_lane4)
service_thread5 = threading.Thread(target=service_ins.clearing_regular_lane5)
service_thread6 = threading.Thread(target=service_ins.clearing_self_lane)
generateThread = threading.Thread(target=customer_ins.generate_customer)

# thread starting
generateThread.start()
service_thread1.start()
service_thread2.start()
service_thread3.start()
service_thread4.start()
service_thread5.start()
service_thread6.start()

t = 0
while sharedState.is_done:
    if t > 300:
        sharedState.is_done = False
    time.sleep(30)
    t += 30

# waiting threads to finish
service_thread1.join()
service_thread2.join()
service_thread3.join()
service_thread4.join()
service_thread5.join()
service_thread6.join()
generateThread.join()

