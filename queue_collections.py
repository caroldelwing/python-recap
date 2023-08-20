from collections import deque

# Create an empty queue (deque)
queue = deque()

# Enqueue (add) elements
queue.append(10)
queue.append(20)
queue.append(30)

# Dequeue (remove) elements
removed_element = queue.popleft()

queue.en

print("Removed element:", removed_element)
print("Remaining queue:", queue)