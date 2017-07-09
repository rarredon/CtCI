# Chapter 3 of CtCI

class Stack:
    """Implements a simple Stack"""
    def __init__(self, initdata=None):
        """Initialize the stack"""
        if initdata:
            self.top = StackItem(initdata, _next=None)
        else:
            self.top = None

    def __str__(self):
        """Prints out a visual of stack with stack data items"""
        if self.top is None:
            return
        else:
            vals = []
            current_item = self.top
            while current_item:
                vals.append(current_item.data)
                current_item = current_item._next
            maxwidth = max(map(lambda x: len(str(x)), vals))
            formatstr = 'Stack: \n'
            for val in vals:
                formatstr += '\t| %0*d |\n' % (maxwidth, val)
            formatstr += '\t'
            formatstr += '-' * (maxwidth + 4)
            return formatstr

    def __repr__(self):
        """Representation of the stack showing the top item"""
        if self.top is None:
            raise Exception("No items in an empty stack")
        return "<Stack object: top=%s>" % str(self.top.data)

    def peek(self):
        """Check the data at the top"""
        if self.top is None:
            raise Exception("No items in an empty stack")
        return self.top.data

    def pop(self):
        """Get and remove the data at the top"""
        if self.top is None:
            raise Exception("No items in an empty stack")
        popped = self.top.data
        self.top = self.top._next
        return popped

    def push(self, data):
        """Insert new item at the top with specified data"""
        self.top = StackItem(data, _next=self.top)

    def isEmpty(self):
        """True if stack is Empty, else False"""
        return self.top is None

class StackItem:
    """A single item in a stack. Helps implement Stack class."""
    def __init__(self, data, _next=None):
        self.data = data
        self._next = _next

def problem5(stack):
    """Sort stack with smallest on top, can only use a second stack"""
    if stack.isEmpty():
        return stack

    sortedstack = Stack(initdata=stack.pop())
    while not stack.isEmpty():
        temp = stack.pop()
        while not sortedstack.isEmpty() and temp > sortedstack.peek():
            # Push temp down by popping smaller data to original stack
            stack.push(sortedstack.pop())

        # Hit bottom or bigger data; push temp
        sortedstack.push(temp)

    return sortedstack
    

## Tests ## -------------------------------------------------------------------
import random

def gen_test_stack(n=50):
    """Randomly generated stack with n items"""
    s = Stack()
    for _ in range(n):
        s.push(random.randint(1, n))
    return s

def problem5_test():
    """Test problem 5"""
    s = gen_test_stack(10)
    print('Before sorting:')
    print(s)
    print()
    s = problem5(s)
    print('After sorting:')
    print(s)
