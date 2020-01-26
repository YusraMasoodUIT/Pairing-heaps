class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.Sibling = None
        self.previous = None

class PairingHeap:
    def __init__(self):
        self.root = None

    def findmin(self):
        if self.root == None:
            return -1
        return self.root.value


    def meld(self, rt1, rt2):
        if rt1 == None:
            return rt2
        if rt2 == None:
            return rt1
        if rt2.value < rt1.value:
            rt2.previous = rt1.previous
            rt1.previous = rt2
            rt1.Sibling = rt2.leftChild
            if rt1.Sibling is not None:
                rt1.Sibling.previous = rt1
            rt2.leftChild = rt1
            return rt2
        else:
            rt2.previous = rt1
            rt1.Sibling = rt2.Sibling
            if rt1.Sibling != None:
                rt1.Sibling.previous = rt1
            rt2.Sibling = rt1.leftChild
            if rt2.Sibling != None:
                rt2.Sibling.previous = rt2
            rt1.leftChild = rt2
            return rt1

    def Insert(self, item):
        n = Node(item)
        if self.root == None:
            self.root = n
            print("Your item has been inserted successfully")
            return
        self.root = self.meld(self.root, n)
        print("Your item has been inserted successfully")
        return n


    def Print(self):
        lst = []
        if self.root is None:
            return lst
        y = self.root
        lst.append(y.value)
        y = y.leftChild
        while y != None:
            lst.append(y.value)
            y = y.Sibling

        return lst


    def Delete(self):
        if self.root == None:
            return -1
        minitem = self.findmin()
        self.__delete()
        return minitem

    def __delete(self):
        if self.root.leftChild == None:
            self.root = None
            return
        else:
            self.root = self.mergeSibling(self.root.leftChild)


    def mergeSibling(self, node):
        if node is None or node.Sibling is None:
            return node
        else:
            x = node
            y = node.Sibling
            newnode = node.Sibling.Sibling

            x.Sibling = None
            y.Sibling = None

            item = self.meld(self.meld(x, y) , self.mergeSibling(newnode))
            return item


    def Join(self, rt):
        self.root = self.meld(self.root, rt)
        return self.root


obj = PairingHeap()


def gui():
    print("\n")
    print("========================================================Pairing Heaps=========================================================")
    print("1 : Insert")
    print("2 : Delete minimum element")
    print("3 : Find minimum element")
    print("4 : Print")
    print("5 : Exit")
    user = input("Choose a number :")
    while user not in ['1', '2', '3', '4', '5']:
        print("Choose correct number!")
        user = input("Choose a number :")
    print("\n")
    if user == "5":
        return
    elif user == "1":
        item = int(input("Enter a number "))
        obj.Insert(item)
        gui()
        return
    elif user == "2":
        item = obj.Delete()
        if item == -1:
            print("Heap is empty")
        else:
            print("Deleted item is ",item)
        gui()
        return
    elif user == "3":
        num = obj.findmin()
        if num == -1:
            print("Heap is empty")
        else:
            print("Minimum element is ",num)
        gui()
        return
    else:
        x = obj.Print()
        if len(x) == 0:
            print("Heap is empty")
            gui()
            return
        print("Root node : ", x[0])
        x.pop(0)
        print("Child nodes : ")
        for node in x:
            print(node)
        gui()
        return

