from tkinter import *
import bookcheckout

def checkout_button_pressed():
    print("checkout_button pressed")

    print(bookcheckout.checkout2(checkout_bookID_textbox.get(),checkout_memberID_textbox.get()))

def deposit_button_pressed():
    print("deposit_button pressed")

def search_button_pressed():
    print("search_button pressed")


root = Tk()
root.title("Model Definition")
root.geometry("{}x{}".format(1280, 720))
root.configure(bg="lime")

control_frame = Frame(root,bg = "azure",width = 420)
control_frame.pack(side = LEFT, fill=Y)
control_frame.pack_propagate(0)

display_frame = Frame(root, bg="purple", width=860, height=720)
display_frame.pack(side=LEFT,fill=Y)

#================

checkout_frame = LabelFrame(control_frame, bg="cyan",width=420, height=180,text = "Checkout")
checkout_frame.pack(in_=control_frame,fill=X)
checkout_frame.pack_propagate(0)

checkout_bookID_frame = Frame(checkout_frame, bg="salmon",width=420,height = 30)
checkout_bookID_frame.pack()
checkout_bookID_frame.pack_propagate(0)

checkout_bookID_label = Label(checkout_bookID_frame,text = "Book ID:")
checkout_bookID_label.pack(side=LEFT)
checkout_bookID_textbox = Entry(checkout_bookID_frame)
checkout_bookID_textbox.pack(side=LEFT)

checkout_memberID_frame = Frame(checkout_frame, bg="purple",width=420,height = 30)
checkout_memberID_frame.pack()
checkout_memberID_frame.pack_propagate(0)

checkout_memberID_label = Label(checkout_memberID_frame,text = "Member ID:")
checkout_memberID_label.pack(side=LEFT)
checkout_memberID_textbox = Entry(checkout_memberID_frame)
checkout_memberID_textbox.pack(side=LEFT)

checkout_button_frame = Frame(checkout_frame, bg="thistle",width=420,height = 30)
checkout_button_frame.pack()
checkout_button_frame.pack_propagate(0)

checkout_button = Button(checkout_button_frame,text = "Checkout",command = checkout_button_pressed)
checkout_button.pack(side=LEFT)

#================

deposit_frame = LabelFrame(control_frame, bg="orange", width=420, height=180,text = "Return")
deposit_frame.pack(in_=control_frame,fill=X)
deposit_frame.pack_propagate(0)

deposit_bookID_frame = Frame(deposit_frame, bg="purple",width=420,height = 30)
deposit_bookID_frame.pack()
deposit_bookID_frame.pack_propagate(0)

deposit_bookID_label = Label(deposit_bookID_frame,text = "Book ID:")
deposit_bookID_label.pack(side=LEFT)
deposit_bookID_textbox = Entry(deposit_bookID_frame)
deposit_bookID_textbox.pack(side=LEFT)

deposit_button_frame = Frame(deposit_frame, bg="thistle",width=420,height = 30)
deposit_button_frame.pack()
deposit_button_frame.pack_propagate(0)

deposit_button = Button(deposit_button_frame,text = "Return",command = deposit_button_pressed)
deposit_button.pack(side=LEFT)

#================

search_frame = LabelFrame(control_frame, bg="yellow", width=420, height=360,text = "View")
search_frame.pack(in_=control_frame,fill=X)
search_frame.pack_propagate(0)

search_title_frame = Frame(search_frame, bg="deep pink",width=420,height = 30)
search_title_frame.pack()
search_title_frame.pack_propagate(0)

search_title_label = Label(search_title_frame,text = "Book Title:")
search_title_label.pack(side=LEFT)
search_title_textbox = Entry(search_title_frame)
search_title_textbox.pack(side=LEFT)

search_button_frame = Frame(search_frame, bg="thistle",width=420,height = 30)
search_button_frame.pack()
search_button_frame.pack_propagate(0)

search_button = Button(search_button_frame,text = "Search",command = search_button_pressed)
search_button.pack(side=LEFT)

#checkout_label = Label(checkout_frame,text="Checkout Label")
#checkout_label.pack()


"""
control_frame = Frame(root, bg="cyan", width=420, height=720, pady=3)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

control_frame.grid(row=0, sticky="ew")"""

"""Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()"""
root.mainloop()
