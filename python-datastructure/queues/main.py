# Queues follow thet FIFO (First in First Out)
# 2 Key Function Enqueue (add at the end of the line) and Dequeue (remove from the front). Best suited for modeling anything you wait inline for,

# You can implement queues via # 
# list
queue_list = []
queue_list.append('a')
queue_list.append('b')
queue_list.append('c')
print("Initial queue")
print(queue_list)
print("\nElements dequeued from queue")
print(queue_list.pop(0))
print(queue_list.pop(0))
print(queue_list.pop(0))
print("\nQueue after removing elements")
print(queue_list)

# collection queue 
from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
 
print("\nQueue after removing elements")
print(q)
