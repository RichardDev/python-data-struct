from collections import deque   

queue = deque()


# Enqueue elements
queue.append(1)
queue.append(2)
queue.append(3)

print("Queue after enqueuing elements:", queue)

first = queue.popleft()
print("Dequeued element:", first)
print("Queue after dequeuing an element:", queue)
second = queue.popleft()
print("Dequeued element:", second)  
print("Queue after dequeuing an element:", queue)