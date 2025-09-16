class Node:
    def __init__(self, val: str, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next
       
class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)  # Start at homepage
        

    def visit(self, url: str) -> None:
        # Create new node and delete forward history
        new_node = Node(url, pre=self.current)
        self.current.next = new_node
        self.current = new_node
        

    def back(self, steps: int) -> str:
        while self.current.pre and steps > 0:
            self.current = self.current.pre
            steps -= 1
        return self.current.val


    def forward(self, steps: int) -> str:
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1
        return self.current.val


# Example usage
obj = BrowserHistory("homepage.com")
obj.visit("page1.com")
obj.visit("page2.com")
print(obj.back(1))      # Goes back to page1.com
print(obj.forward(1))   # Goes forward to page2.com
