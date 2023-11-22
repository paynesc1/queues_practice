class SLNode():
    def __init__(self,val):
        self.val = val
        self.next = None

class SLQueue():
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,val):
        new_node = SLNode(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def front(self):
        return self.head.val

    def all_vals(self):
        runner = self.head
        while runner:
            print(runner.val)
            runner = runner.next



my_queue = SLQueue()
my_queue.enqueue(3)
my_queue.enqueue(2)
my_queue.enqueue(1)
print(my_queue.front())
print(my_queue.all_vals())
# Create SLQueue method enqueue(val) to add the given value to the end of our queue. Remember, SLQueue uses a singly linked list (not an array).

