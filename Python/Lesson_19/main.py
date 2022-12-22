""" Task 1 """


class Stack:

    def __init__(self, *args):
        self.stack = list(args)
    
    def push(self, elem):
        self.stack.append(elem)
    
    def pop(self):
        return self.stack.pop()
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def top(self):
        return self.stack[-1]
    
    def __str__(self):
        return str(self.stack)


my_stack = Stack(1, 2, 3, 4, 5, 6)
print(my_stack)
print(my_stack.push(10))
print(my_stack)
print(my_stack.pop())
print(my_stack)
print(my_stack.top())


""" Task 2 """


class Queue:

    def __init__(self, *args):
        self.queue = list(args)
    
    def push(self, elem):
        self.queue.append(elem)
    
    def get(self):
        if self.isempty():
            pass
        else:
            return self.queue.pop(0)
    
    def isempty(self):
        return len(self.queue) == 0
    
    def reverse(self, count):
        return self.queue[0:count][::-1] + self.queue[count:]


my_queue = Queue(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(my_queue.isempty())
print(my_queue.reverse(8))