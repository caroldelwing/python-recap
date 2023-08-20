def create_queue():
    return []
def enqueue(queue, item):
    queue.append(item)

def find_frequency(queue, num):
    return queue.count(num)

'''def find_frequency(queue, num):
    frequency = 0
    for item in queue:
        if item == num:
            frequency += 1
    return frequency'''

# Example usage:
queue = create_queue()

# Insert N integers into the queue
N = int(input("Enter the number of elements to insert: "))
for i in range(N):
    element = int(input("Enter element: "))
    enqueue(queue, element)

# Find the frequency of M integers
M = int(input("Enter the number of queries to find frequency: "))
for i in range(M):
    num = int(input("Enter number to find frequency: "))
    frequency = find_frequency(queue, num)
    print(f"The frequency of {num} is {frequency}")