
import threading, Queue

orders_chunks = [[1,2,3],[4,5,6],[7,8,9],[0,0,1]]

def func1(orders, queue):
    sum = 0
    for order in orders:
        sum += order
    
    queue.put(sum)

q = Queue.Queue()

threads = []

for orders in orders_chunks:
    t = threading.Thread(target=func1, args=(orders, q))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

[q.get() for _ in xrange(len(orders_chunks))]


#ZEND
#https://github.com/bfortuner/ml-study/blob/master/multitasking_python.ipynb
