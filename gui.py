from pairing_heaps import *
from tkinter import *
from tkinter import messagebox

inst = PairingHeap()

class gui:

    def __init__(self):
        self.count = 0
        self.dict = {}
        self.lst = []
        self.root = Tk()
        self.root.title("Pairing Heaps")
        self.root.geometry("600x600+400+50")
        self.root.configure(background="#F0F3F4")

        title = Label(self.root, text='Pairing Heaps', bg='#003333', fg='#3498DB', font='Impact 18 ', justify='center')
        title.place(x=215, y=0)

        func = Label(self.root, text='OPERATIONS', bg='#003333', fg='#F4F6F7', height = 2, font='ArialBlack 14 bold')
        func.place(x=220, y=280)

        heap = "* Pairing heaps is a modified form of Fibonacci heaps.\n\n\n* It consist of the properties of " \
               "heap data structure along with self\n   adjusting structure.\n\n\n* The advantage of pairing heaps is that " \
               "they have fast amortized running\n   time for their operations which makes it suitable for shortest path algorithms   "

        text = Text(self.root, height=10, width=63, fg="#F4F6F7", bg='#003333', font='TimesNewRoman 12 ', relief = GROOVE)
        text.insert(INSERT, heap)
        text.place(x=10, y=50)


        def ins_opt():
            self.int_Insert()


        def del_opt():
            self.int_Delete()


        def min_opt():
            self.int_findmin()


        def disp_opt():
            self.int_Print()

        def create_opt():
            self.obj()

        def merge_opt():
            self.int_merge()


        n_obj = Button(self.root, text="Create new heap", bg='#003333', fg='#F4F6F7', font='Bookman 12 bold', relief=RAISED,
                     command=create_opt)
        n_obj.config(height="2", width="14")
        n_obj.place(x=5, y=370)


        ins = Button(self.root, text="Insert", bg='#003333', fg='#F4F6F7', font='Bookman 12 bold', relief=RAISED,
                     command=ins_opt)
        ins.config(height="2", width="10")
        ins.place(x=175, y=370)

        minnum = Button(self.root, text="Minimum item", bg='#003333', fg='#F4F6F7', font='Bookman 12 bold', relief=RAISED,
                        command=min_opt)
        minnum.config(height="2", width="11")
        minnum.place(x=310, y=370)

        dlt = Button(self.root, text="Delete", bg='#003333', fg='#F4F6F7', font='Bookman 12 bold', relief=RAISED,
                     command=del_opt)
        dlt.config(height="2", width="10")
        dlt.place(x=450, y=370)

        mrg = Button(self.root, text="Merge", bg='#003333', fg='#F4F6F7', font='Bookman 12 bold', relief=RAISED,
                     command=merge_opt)
        mrg.config(height="2", width="10")
        mrg.place(x=165, y=435)

        dsp = Button(self.root, text="Display", bg='#003333', fg='#F4F6F7', font='Bookman 12 bold', relief=RAISED,
                     command=disp_opt)
        dsp.config(height="2", width="10")
        dsp.place(x=335, y=435)


        self.root.mainloop()


    def obj(self):
        root = Tk()
        root.title("Pairing Heaps")
        root.geometry("600x600+400+50")
        root.configure(background="#003333")

        title = Label(root, text='CREATE A NEW HEAP', bg='#003333', fg='#F4F6F7', font='Impact 16 ', justify='center')
        title.place(x=230, y=0)

        insert = "* Creates a new object of the class"

        text = Text(root, height=3, width=63, fg="#F4F6F7", bg='#003333', font='TimesNewRoman 12 ', relief=GROOVE)
        text.insert(INSERT, insert)
        text.place(x=10, y=50)

        def create():
            n = "heap"
            x = self.count
            self.count = self.count + 1
            x = str(x)
            y = n + x
            self.lst.append(y)
            self.dict[y] = PairingHeap()

            info = Label(root, text='A new heap has been successfully created', bg='#003333', fg='#F4F6F7',
                         font='Bookman 12 bold',
                         justify='center')
            info.place(x=0, y=300)
            info.after(1300, lambda: info.destroy())


        def exit():
            root.destroy()

        button = Button(root, text="Create a new heap", command=create)
        button.place(x=50, y=200)


        button2 = Button(root, text="Main Menu", command=exit)
        button2.place(x=250, y=550)

        root.mainloop()


    def int_Insert(self):
        root = Tk()
        root.title("Pairing Heaps")
        root.geometry("600x600+400+50")
        root.configure(background="#003333")

        if len(self.lst) == 0:
            messagebox.showerror("Error", "Create a new heap first")
            root.destroy()
            return

        title = Label(root, text='INSERT', bg='#003333', fg='#F4F6F7', font='Impact 16 ', justify='center')
        title.place(x=250, y=0)

        insert = "* The insert operation uses the meld operation to insert a new element.\n\n\n* In a meld operation two min " \
                 " pairing heaps may be melded into a single\n  min pairing heap by performing a compare-link operation. " \
                 "In a compare-link, the\n  roots of the two min trees are compared and the min tree that has the " \
                 "larger root\n  is made the leftmost subtree of the other tree. \n\n\n* To insert an element x into a pairing heap p," \
                 " we ﬁrst create a pairing heap q with \n  the single element x, and then meld the two pairing heaps p and q"

        text = Text(root, height=13, width=63, fg="#F4F6F7", bg='#003333', font='TimesNewRoman 12 ', relief=GROOVE)
        text.insert(INSERT, insert)
        text.place(x=10, y=50)



        var_title = Label(root, text='Select a heap', bg='#003333', fg='#F4F6F7', font='ArialBlack 12 bold', justify='center')
        var_title.place(x=0, y=350)
        lst = StringVar(root)
        lst.set(self.lst[0])
        var = OptionMenu(root, lst, *self.lst)
        var.place(x=150, y=350)


        numtitle = Label(root, text='Enter a number', bg='#003333', fg='#F4F6F7', font='ArialBlack 12 bold', justify='center')
        numtitle.place(x=300, y=350)
        num = Entry(root, bd=5)
        num.place(x=450, y=350)

        def ins():
            heap = lst.get()
            item = num.get()
            try:
                item = int(item)
            except ValueError:
                messagebox.showerror("Error", "Please enter an integer")
                root.destroy()
                return
            self.dict[heap].Insert(item)
            num.delete(0, 'end')
            info = Label(root, text='The number has been successfully added', bg='#003333', fg='#F4F6F7',font='Bookman 12 bold',
                         justify='center')
            info.place(x=0, y=475)
            info.after(1300, lambda: info.destroy())


        def exit():
            root.destroy()

        button = Button(root, text="Submit", command=ins)
        button.place(x=425, y=400)

        button = Button(root, text="Main Menu", command=exit)
        button.place(x=250, y=550)

        root.mainloop()


    def int_Delete(self):
        root = Tk()
        root.title("Pairing Heaps")
        root.geometry("600x600+400+50")
        root.configure(background="#003333")

        if len(self.lst) == 0:
            messagebox.showerror("Error", "Create a new heap first")
            root.destroy()
            return

        title = Label(root, text='DELETE', bg='#003333', fg='#F4F6F7', font='Impact 16 ', justify='center')
        title.place(x=250, y=0)

        delete = "*  Deletion in a pairing heap always happens at the root node. The root node\n   consist of a minimum" \
                 " element so every time delete function is called a minimum\n   element is deleted\n\n\n" \
                 "*  To delete the min-elemnet, detach the " \
                 "sub tree that is rooted at node n. Then,\n   delete n from the tree and merge its sub trees into " \
                 "one sub tree using a two-pass\n   method. " \
                 "Merge the detached sub tree with the sub tree resulting from the two-pass"


        text = Text(root, height=10, width=64, fg="#F4F6F7", bg='#003333', font='TimesNewRoman 12 ', relief=GROOVE)
        text.insert(INSERT, delete)
        text.place(x=10, y=50)

        var_title = Label(root, text='Select a heap', bg='#003333', fg='#F4F6F7', font='ArialBlack 12 bold', justify='center')
        var_title.place(x=0, y=350)
        lst = StringVar(root)
        lst.set(self.lst[0])
        var = OptionMenu(root, lst, *self.lst)
        var.place(x=150, y=350)

        def delval():
            heap = lst.get()
            item = self.dict[heap].Delete()
            if item == -1:
                messagebox.showerror("Error", "Heap is Empty")
                root.destroy()
            else:
                message = "Minimum value "+ str(item)+" has been deleted"

                info = Label(root, text=message, bg='#003333', fg='#F4F6F7',
                             font='Bookman 12 bold',justify='center')
                info.place(x=0, y=475)
                info.after(1300, lambda: info.destroy())


        def exit():
            root.destroy()


        button = Button(root, text="Delete Minimum Value",  command=delval)
        button.place(x=230, y=410)

        button = Button(root, text="Main Menu", command=exit)
        button.place(x=250, y=530)

        root.mainloop()


    def int_findmin(self):
        root = Tk()
        root.title("Pairing Heaps")
        root.geometry("600x600+400+50")
        root.configure(background="#003333")

        if len(self.lst) == 0:
            messagebox.showerror("Error", "Create a new heap first")
            root.destroy()
            return

        title = Label(root, text='FIND MINIMUM VALUE', bg='#003333', fg='#F4F6F7', font='Impact 16 ', justify='center')
        title.place(x=200, y=0)

        minitem = "*   This operation just returns the value at the root of the heap."

        text = Text(root, height=8, width=63, fg="#F4F6F7", bg='#003333', font='TimesNewRoman 12 ', relief=GROOVE)
        text.insert(INSERT, minitem)
        text.place(x=10, y=50)

        var_title = Label(root, text='Select a heap', bg='#003333', fg='#F4F6F7', font='ArialBlack 12 bold', justify='center')
        var_title.place(x=0, y=320)
        lst = StringVar(root)
        lst.set(self.lst[0])
        var = OptionMenu(root, lst, *self.lst)
        var.place(x=150, y=320)

        def minval():
            heap = lst.get()
            item = self.dict[heap].findmin()
            if item == -1:
                messagebox.showerror("Error", "Heap is Empty")
                root.destroy()
            else:
                message = "Minimum value in this heap is " + str(item)
                info = Label(root, text=message, bg='#003333', fg='#F4F6F7',
                             font='Bookman 12 bold', justify='center')
                info.place(x=0, y=475)
                info.after(1300, lambda: info.destroy())



        def exit():
            root.destroy()


        button = Button(root, text="Find Minimum Value",  command=minval)
        button.place(x=230, y=410)

        button = Button(root, text="Main Menu", command=exit)
        button.place(x=250, y=530)

        root.mainloop()


    def int_Print(self):
        root = Tk()
        root.title("Pairing Heaps")
        root.geometry("600x600+400+50")
        root.configure(background="#003333")

        if len(self.lst) == 0:
            messagebox.showerror("Error", "Create a new heap first")
            root.destroy()
            return

        title = Label(root, text='PRINT', bg='#003333', fg='#F4F6F7', font='Impact 16 ', justify='center')
        title.place(x=250, y=0)

        dsp = "*   This operation displays the root node and the children of the root node." \
              "\n\n\n  Note:- The child nodes displayed here are the real children of root node, it is\n    possible that " \
              "these children may have further child nodes (i.e. more sub heaps)\n    which are not displayed here"

        text = Text(root, height=6, width=63, fg="#F4F6F7", bg='#003333', font='TimesNewRoman 12 ', relief=GROOVE)
        text.insert(INSERT, dsp)
        text.place(x=10, y=33)

        var_title = Label(root, text='Select a heap', bg='#003333', fg='#F4F6F7', font='ArialBlack 12 bold', justify='center')
        var_title.place(x=0, y=170)
        lst = StringVar(root)
        lst.set(self.lst[0])
        var = OptionMenu(root, lst, *self.lst)
        var.place(x=150, y=167)



        prntframe = Frame(root, bg="#87ceeb", width=580, height=350)
        prntframe.place(x=10, y=210)


        def prnt():
            heap = lst.get()
            item = self.dict[heap].Print()
            if len(item) == 0:
                messagebox.showerror("Error", "Heap is Empty")
                root.destroy()
            else:
                rt_val = item[0]
                rt_pointer = Label(prntframe, text="Root Pointer :  ", bg='#87ceeb', fg='#808080', font='TimesNewRoman 16 bold',
                                   justify='center')
                rt_pointer.place(x=50, y=10)
                rt_pointer = Label(prntframe, text=rt_val, bg='#87ceeb', fg= '#808080', font='TimesNewRoman 16 bold',
                                   justify='center')
                rt_pointer.place(x=250, y=10)
                item.pop(0)
                ch_pointer = Label(prntframe, text="Child Nodes :  ", bg='#87ceeb', fg='#808080', font='TimesNewRoman 16 bold',
                                   justify='center')
                ch_pointer.place(x=50, y=50)
                y = 90
                for nd in range(len(item)):
                    val = item[nd]
                    nd_pointer = Label(prntframe, text=val, bg='#87ceeb', fg='#808080', font='TimesNewRoman 16 bold',
                                       justify='center')
                    nd_pointer.place(x=100, y=y)
                    y = y + 40



        button = Button(root, text="Print Heap",  command=prnt)
        button.place(x=350, y=170)

        def exit():
            root.destroy()

        button1 = Button(root, text="Main Menu", command=exit)
        button1.place(x=250, y=570)

        root.mainloop()


    def int_merge(self):
        root = Tk()
        root.title("Pairing Heaps")
        root.geometry("600x600+400+50")
        root.configure(background="#003333")

        if len(self.lst) < 2:
            messagebox.showerror("Error", "Merge function requires at least two heaps. Create a new heap first")
            root.destroy()
            return


        title = Label(root, text='MERGE TWO HEAPS', bg='#003333', fg='#F4F6F7', font='Impact 16 ', justify='center')
        title.place(x=250, y=0)

        dsp = "*   In a merge operation two min pairing heaps may be melded into a single\n  min pairing heap by " \
              "performing a compare-link operation.\n\n\n*   In a compare-link, the  roots of the two min trees are compared " \
              "and the min tree\n   that has the larger root is made the leftmost subtree of the other tree."

        text = Text(root, height=6, width=63, fg="#F4F6F7", bg='#003333', font='TimesNewRoman 12 ', relief=GROOVE)
        text.insert(INSERT, dsp)
        text.place(x=10, y=33)

        title = Label(root, text='Select two heaps to be merged', bg='#003333', fg='#F4F6F7', font='TimesNewRoman 12 bold',
                          justify='center')
        title.place(x=160, y=300)

        var_title = Label(root, text='Select first heap', bg='#003333', fg='#F4F6F7', font='ArialBlack 13',
                          justify='center')
        var_title.place(x=0, y=350)
        lst = StringVar(root)
        lst.set(self.lst[0])
        var = OptionMenu(root, lst, *self.lst)
        var.place(x=180, y=350)


        var_title1 = Label(root, text='Select second heap', bg='#003333', fg='#F4F6F7', font='ArialBlack 13',
                          justify='center')
        var_title1.place(x=310, y=350)
        lst1 = StringVar(root)
        lst1.set(self.lst[0])
        var1 = OptionMenu(root, lst1, *self.lst)
        var1.place(x=500, y=350)


        def mrg():
            heap = lst.get()
            heap2 = lst1.get()
            if heap == heap2:
                messagebox.showerror("Error", "Cannot merge two same heaps")
                root.destroy()
                return

            self.dict[heap].Join(self.dict[heap2].root)

            info = Label(root, text="Both heaps have been successfully merged", bg='#003333', fg='#F4F6F7',
                         font='Bookman 12 bold', justify='center')
            info.place(x=0, y=475)
            info.after(1300, lambda: info.destroy())



        button = Button(root, text="Merge Heap", command=mrg)
        button.place(x=250, y=400)

        def exit():
            root.destroy()

        button1 = Button(root, text="Main Menu", command=exit)
        button1.place(x=250, y=570)




        root.mainloop()




o = gui()

