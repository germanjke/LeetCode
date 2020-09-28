class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.entry = []
        self.exit = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.entry.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.exit) == 0:
            self.items_from_entry_to_exit()
        return self.exit.pop(-1)
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.exit) == 0:
            self.items_from_entry_to_exit()
        return self.exit[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.exit) == 0:
            self.items_from_entry_to_exit()
        return len(self.exit) == 0
    
    def items_from_entry_to_exit(self) -> None:
        """
        Push all items from entry to exit.
        """
        for i in range(len(self.entry)):
            self.exit.append(self.entry.pop(-1))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
