class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return f"Pushed: {item}"

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: Nothing to peek.")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# ------------ Test Cases / Edge Cases ---------------

stack = Stack()

print("Initial stack empty?:", stack.is_empty())

# Push operations
print(stack.push(10))
print(stack.push(20))
print(stack.push(30))

# Peek top element
print("Peek:", stack.peek())

# Pop operations
print("Pop:", stack.pop())
print("Pop:", stack.pop())

# Edge case: Pop from empty stack
try:
    stack.pop()
except Exception as e:
    print("Error:", e)

# Edge case: Peek from empty stack
try:
    stack.peek()
except Exception as e:
    print("Error:", e)
