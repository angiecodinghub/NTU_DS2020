class node:
    # this class infor testing
    # Do Not Modify
    def __init__(self, value):
        self.value = value
        self.right = self
        self.left = self
        
    def __repr__(self):
        return 'Node{}'.format(self.value).strip()


class stack:
    def __init__(self):
        self.num_element = 0
        self.root = node(None)
    
    def pop(self):
        if self.num_element == 0:
            raise ValueError('Can not execute pop() on an empty stack')
        else:
            # todo:
            # Connect the second last element >> root
            # Connect root >> the second last element
            self.root.left.left.right = self.root
            self.root.left = self.root.left.left
            self.num_element -= 1

    def push(self, node):
        # todo:
        # Connect the last element >> inserted node
        # Connect the inserted node >> root
        node.left = self.root.left
        self.root.left.right = node
        node.right = self.root
        self.root.left = node
        self.num_element += 1        

    def __repr__(self):
        ret = ''
        node = self.root.right
        while node != self.root:
            ret  = ret + '>>' + str(node)
            node = node.right
        return ret

class queue:
    def __init__(self):
        self.num_element = 0
        self.root = node(None)

    def pop(self):
        if self.num_element == 0:
            raise ValueError('Can not execute pop() on an empty queue')
        else:
            # todo:
            # Connect the second element >> root
            # Connect root >> the second element 
            self.root.right.right.left = self.root
            self.root.right = self.root.right.right
            self.num_element -= 1
    
    def push(self, node):
        # todo:
        # Connect the root >> inserted node
        # Connect the inserted node >> first element
        node.left = self.root.left
        self.root.left.right = node
        node.right = self.root
        self.root.left = node 
        self.num_element += 1

    def __repr__(self):
        ret = ''
        node = self.root.right
        while node != self.root:
            ret  = ret + '>>' + str(node)
            node = node.right
        return ret