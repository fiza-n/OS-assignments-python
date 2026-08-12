import threading
import time
import random


order_queue = []
MAX_CAPACITY = 5


lock = threading.Lock()
condition = threading.Condition(lock)

def producer(id):
    for i in range(8):
        time.sleep(random.uniform(0.1, 0.4)) 
        order = f"Order-{id}-{i}"
        
        with condition:
           
            while len(order_queue) >= MAX_CAPACITY:
                print(f"(Full) Restaurant {id} waiting. Queue size: {len(order_queue)}")
                condition.wait()
            
            order_queue.append(order)
            print(f" Produced: {order}  Queue: {len(order_queue)}")
            
           
            condition.notify_all()

def consumer(id):
    for i in range(8):
        time.sleep(random.uniform(0.5, 1.0)) 
        
        with condition:
          
            while len(order_queue) == 0:
                print(f" delivery agent {id} waiting for orders")
                condition.wait()
            
            order = order_queue.pop(0)
            print(f" Consumed: {order} Queue: {len(order_queue)}")
            
          
            condition.notify_all()


p1 = threading.Thread(target=producer, args=(1,))
c1 = threading.Thread(target=consumer, args=(1,))
p1.start(); c1.start()
p1.join(); c1.join()

# import threading
# import time
# import random


# order_queue = []


# lock = threading.Lock()
# condition = threading.Condition(lock)

# def producer_unbounded(id):
#     for i in range(10):
#         time.sleep(random.uniform(0.1, 0.2)) 
#         order = f"Order-{id}-{i}"
        
#         with condition:

#             order_queue.append(order)
#             print(f"Produced : {order}  Queue: {len(order_queue)}")
            
           
#             condition.notify_all()

# def consumer_unbounded(id):
#     for i in range(10):
#         time.sleep(random.uniform(0.5, 1.0))
        
#         with condition:
#             while len(order_queue) == 0:
#                 print(f" delivery agent {id} waiting")
#                 condition.wait()
            
#             order = order_queue.pop(0)
#             print(f" Consumed: {order}  Queue: {len(order_queue)}")


# p2 = threading.Thread(target=producer_unbounded, args=(2,))
# c2 = threading.Thread(target=consumer_unbounded, args=(2,))
# p2.start(); c2.start()
# p2.join(); c2.join()