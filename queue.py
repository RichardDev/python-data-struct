
queue = []

# Enqueue elements
queue.append(1)
queue.append(2)
queue.append(3)

print("Queue after enqueuing 1, 2, 3:", queue)

# Dequeue elements
first = queue.pop(0)
print("Dequeued element:", first)
print("Queue after dequeuing an element:", queue)
second = queue.pop(0)
print("Dequeued element:", second)
print("Queue after dequeuing an element:", queue)

