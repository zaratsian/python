
from concurrent import futures
import random
import time

orders_chunks = [[1,2,3],[4,5,6],[7,8,9],[0,0,1]]

def execute_queries(orders):
    sum = 0
    for order in orders:
        sum += order
    return sum

ex = futures.ProcessPoolExecutor(max_workers=4)
#ex = futures.ThreadPoolExecutor(max_workers=4)

#'''

results = ex.map(execute_queries, orders_chunks)

for result in results:
    print result

'''

wait_for = [
    ex.submit(execute_queries, orders)
    for orders in orders_chunks
]

for f in futures.as_completed(wait_for):
    print('main: result: {}'.format(f.result()))

'''

#ZEND
