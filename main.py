from tkinter import *
import bookcheckout
import bookreturn
import database
import booksearch
import booklist
"""
Created by: Jacob Toller (B922435), ‎22 ‎November ‎2019, ‏‎11:35:04
"""

chart = False

def returnOutput(label,new_text,colour="SystemButtonFace"):
    label.configure(text=new_text,fg=colour)

def radio_button_pressed():
    global radio
    swapCanvas(radio.get())

def swapCanvas(mode):
    global display_canvas
    global display_scrollbar
    global chart_canvas
    if mode == "table":
        chart_canvas.pack_forget()
        display_canvas.pack(side="left",expand = True, fill = "both")
        display_scrollbar.pack(side="right",fill="y")
        chart = False
    elif mode == "chart":
        display_canvas.pack_forget()
        display_scrollbar.pack_forget()
        chart_canvas.pack(side="left",expand = True, fill = "both")
        popularity = booklist.getPopularity()
        popularity = sorted(popularity.items() , reverse=True, key=lambda x: x[1]) # sorts dictionary by value, converts to list of tuples
        booklist.barChart(chart_canvas,popularity)
        chart = True

def updateTable(filt=""):
    global grid_frame
    for i in grid_frame.winfo_children():
        i.destroy() # clears grid before redrawing it

    loadTable(filt)

def loadTable(filt=""):
    # Creating table headers
    Label(grid_frame,text="Book ID").grid(row=0,column=0,sticky="w",padx = 2,pady = 4)
    Label(grid_frame,text="Title").grid(row=0,column=1,sticky="w",padx = 2,pady = 4)
    Label(grid_frame,text="Author").grid(row=0,column=2,sticky="w",padx = 2,pady = 4)
    Label(grid_frame,text="Date Added").grid(row=0,column=3,sticky="w",padx = 2,pady = 4)
    Label(grid_frame,text="Member Status").grid(row=0,column=4,sticky="w",padx = 2,pady = 4)
    # displaying book data
    data = database.read_database()
    for i in range(1,len(data) + 1):
        entry = data[i - 1]
        if filt == "" or filt.lower() in entry[1].lower(): # will only display book if it matches the filter
            for j in range(0,len(entry)):
                temp = Label(grid_frame,text=entry[j]).grid(row=i,column=j,sticky="w",padx = 2,pady = 4)
       
def scroller(event): # function that manages table scrolling
    display_canvas.configure(scrollregion=display_canvas.bbox("all"),width=200,height=200)

def validate_memberID(memberID):
    return memberID.isdigit() and (len(str(int(memberID))) == 4) # checks that its a 4 digit number between 1000-9999

def validate_bookID(bookID):
    return bookID.isdigit()

def checkout_button_pressed():
    print("checkout_button pressed")
    returnOutput(checkout_output,"Running...")
    
    bookID_input = checkout_bookID_textbox.get()
    memberID_input = checkout_memberID_textbox.get()
    if validate_bookID(bookID_input) == False:
        print("invalid bookID input")
        returnOutput(checkout_output,"Error: Book ID input not valid","red")
    elif validate_memberID(memberID_input) == False:
        print("invalid memberID input")
        returnOutput(checkout_output,"Error: Member ID input not valid","red")
    else:
        bookID_input = str(int(bookID_input))# gets rid of any leading 0s; ie turns '0003' into '3'
        success = bookcheckout.checkout(bookID_input,memberID_input)

        if success:
            print("Book %s has been successfully checked out to member %s"%(bookID_input,memberID_input))
            returnOutput(checkout_output,"Success: Book %s has been successfully checked out to member %s"%(bookID_input,memberID_input),"green")
            updateTable() # redraw table with updated information
        else:
            print("checkout failure")
            returnOutput(checkout_output,"Error: Checkout failure, book not found or book already out","red")

def deposit_button_pressed():
    print("deposit_button pressed")
    returnOutput(deposit_output,"Running...")
    
    bookID_input = deposit_bookID_textbox.get()
    if validate_bookID(bookID_input) == False:
        print("invalid bookID input")
        returnOutput(deposit_output,"Error: Book ID input not valid","red")
    else:
        bookID_input = str(int(bookID_input))# gets rid of any leading 0s; ie turns '0003' into '3'
        success = bookreturn.deposit(bookID_input)

        if success:
            print("Book %s has been successfully returned"%(bookID_input))
            returnOutput(deposit_output,"Book %s has been successfully returned"%(bookID_input),"green")
            updateTable() # redraw table with updated information
        else:
            print("deposit failure")
            returnOutput(checkout_output,"Error: Deposit failure, book not found or book already in","red")

def search_button_pressed():
    print("search_button pressed")
    updateTable(search_title_textbox.get()) # updates table with filter of the textbox entry

def clear_search_button_pressed():
    print("search_button pressed")
    search_title_textbox.delete(0,END) # clears textbox, resets table
    updateTable()
    
# root definition and table display
root = Tk()
root.title("Dr Batmaz's amazing library")
root.geometry("1280x720")
root.configure(bg="SystemButtonFace")

control_frame = Frame(root,bg="SystemButtonFace",width = 420)
control_frame.pack(side = LEFT, fill=Y)
control_frame.pack_propagate(0)

display_frame = Frame(root, bg="SystemButtonFace", width=860, height=720)
display_frame.pack(side=LEFT,fill=Y)
display_frame.pack_propagate(0)

display_canvas=Canvas(display_frame,bg="dim gray")
display_subframe=Frame(display_canvas,bg="dim gray")
display_scrollbar=Scrollbar(display_frame,orient="vertical",command=display_canvas.yview)
display_canvas.configure(yscrollcommand=display_scrollbar.set)

display_scrollbar.pack(side="right",fill="y")
display_canvas.pack(side="left",expand = True, fill = "both")
display_canvas.create_window((0,0),window=display_subframe,anchor='nw')
display_subframe.bind("<Configure>",scroller)

chart_canvas = Canvas(display_frame,bg="bisque")

grid_frame=Frame(display_subframe,bg="SystemButtonFace",width=860, height=720)
grid_frame.pack(fill=X)
grid_frame.pack_propagate(0)
loadTable()

# checkout frame and contents

checkout_frame = LabelFrame(control_frame, bg="SystemButtonFace",width=420, height=180,text = "Checkout")
checkout_frame.pack(in_=control_frame,fill=X)
checkout_frame.pack_propagate(0)

checkout_bookID_frame = Frame(checkout_frame, bg="SystemButtonFace",width=420,height = 30)
checkout_bookID_frame.pack()
checkout_bookID_frame.pack_propagate(0)

checkout_bookID_label = Label(checkout_bookID_frame,text = "Book ID:")
checkout_bookID_label.pack(side=LEFT)
checkout_bookID_textbox = Entry(checkout_bookID_frame)
checkout_bookID_textbox.pack(side=LEFT)

checkout_memberID_frame = Frame(checkout_frame, bg="SystemButtonFace",width=420,height = 30)
checkout_memberID_frame.pack()
checkout_memberID_frame.pack_propagate(0)

checkout_memberID_label = Label(checkout_memberID_frame,text = "Member ID:")
checkout_memberID_label.pack(side=LEFT)
checkout_memberID_textbox = Entry(checkout_memberID_frame)
checkout_memberID_textbox.pack(side=LEFT)

checkout_button_frame = Frame(checkout_frame, bg="SystemButtonFace",width=420,height = 30)
checkout_button_frame.pack()
checkout_button_frame.pack_propagate(0)

checkout_button = Button(checkout_button_frame,text = "Checkout",command = checkout_button_pressed)
checkout_button.pack(side=LEFT)

checkout_output_frame = Frame(checkout_frame, bg="SystemButtonFace",width=420,height = 30)
checkout_output_frame.pack()
checkout_output_frame.pack_propagate(0)

checkout_output = Label(checkout_output_frame,text = "")
checkout_output.pack(side=LEFT)

# deposit frame and contents

deposit_frame = LabelFrame(control_frame, bg="SystemButtonFace", width=420, height=180,text = "Return")
deposit_frame.pack(in_=control_frame,fill=X)
deposit_frame.pack_propagate(0)

deposit_bookID_frame = Frame(deposit_frame, bg="SystemButtonFace",width=420,height = 30)
deposit_bookID_frame.pack()
deposit_bookID_frame.pack_propagate(0)

deposit_bookID_label = Label(deposit_bookID_frame,text = "Book ID:")
deposit_bookID_label.pack(side=LEFT)
deposit_bookID_textbox = Entry(deposit_bookID_frame)
deposit_bookID_textbox.pack(side=LEFT)

deposit_button_frame = Frame(deposit_frame, bg="SystemButtonFace",width=420,height = 30)
deposit_button_frame.pack()
deposit_button_frame.pack_propagate(0)

deposit_button = Button(deposit_button_frame,text = "Return",command = deposit_button_pressed)
deposit_button.pack(side=LEFT)

deposit_output_frame = Frame(deposit_frame, bg="SystemButtonFace",width=420,height = 30)
deposit_output_frame.pack()
deposit_output_frame.pack_propagate(0)

deposit_output = Label(deposit_output_frame,text = "")
deposit_output.pack(side=LEFT)

# search frame and contents

search_frame = LabelFrame(control_frame, bg="SystemButtonFace", width=420, height=360,text = "View")
search_frame.pack(in_=control_frame,fill=X)
search_frame.pack_propagate(0)

search_title_frame = Frame(search_frame, bg="SystemButtonFace",width=420,height = 30)
search_title_frame.pack()
search_title_frame.pack_propagate(0)

search_title_label = Label(search_title_frame,text = "Book Title:")
search_title_label.pack(side=LEFT)
search_title_textbox = Entry(search_title_frame)
search_title_textbox.pack(side=LEFT)

search_button_frame = Frame(search_frame, bg="SystemButtonFace",width=420,height = 30)
search_button_frame.pack()
search_button_frame.pack_propagate(0)

search_button = Button(search_button_frame,text = "Search",command = search_button_pressed)
search_button.pack(side=LEFT)

clear_search_button = Button(search_button_frame,text = "Clear",command = clear_search_button_pressed)
clear_search_button.pack(side=LEFT)

radio_frame = Frame(search_frame, bg="SystemButtonFace",width=420,height = 30)
radio_frame.pack()
radio_frame.pack_propagate(0)

radio = StringVar()
radio.set("table")
Radiobutton(radio_frame,text="Table View",variable=radio,value="table",command=radio_button_pressed).pack(side=LEFT)
Radiobutton(radio_frame,text="Chart View",variable=radio,value="chart",command=radio_button_pressed).pack(side=LEFT)

root.mainloop()
