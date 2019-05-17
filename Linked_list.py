class node(object):
    def __init__(self,data):
        self.d=data;
        self.nxt=None;
class link_list(object):
    def __init__(self):
        self.head=None;
        self.size=0;
    def insert(self,data):                  #insert function
        newnode=node(data)
        if self.head is None:
            self.head=newnode;
        else:
            newnode.nxt=self.head
            self.head=newnode
    def travers(self):                      #traverse function
        actual=self.head;
        while actual is not None:
            print("%d" %actual.d)
            actual=actual.nxt
l=link_list()
l.insert(10)
l.insert(20)
l.insert(33)
l.travers()



