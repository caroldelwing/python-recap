def create_stack():
    return []

def push(stack, item):
    stack.append(item)

def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        raise IndexError("pop from an empty stack")

def top(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        raise IndexError("top from an empty stack")

def is_empty(stack):
    return len(stack) == 0

def size(stack):
    return len(stack)

# Example usage:
stack = create_stack()

print("Is the stack empty?", is_empty(stack))  # Output: Is the stack empty? True

push(stack, 10)
push(stack, 20)
push(stack, 30)

print("Stack size:", size(stack))  # Output: Stack size: 3
print("Top element:", top(stack))  # Output: Top element: 30

popped_item = pop(stack)
print("Popped item:", popped_item)   # Output: Popped item: 30

print("Is the stack empty?", is_empty(stack))  # Output: Is the stack empty? False
print("Stack size:", size(stack))  # Output: Stack size: 2