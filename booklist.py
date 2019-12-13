import colorsys
import database
import time
from tkinter import *

def getPopularity(back_time = -1):
    """This function reads the logfile and counts how many times a book has been taken out.

Parameters:
    back_time; integer (default = -1): This is how many seconds into the past it
        will check for, for example if it was 500, it would only count the books
        taken out in the last 5 minutes. Leaving it empty or providing a
        negative value will make it count every withdraw transaction.

Returns:
    getPopularity(...); dictionary: A dictionary with the keys as the title and
        author of the book, and the value of how many times it has been taken
        out.

"""
    log_data = database.read_logfile()

    if back_time > 0:
        time_comparison = round(time.time()) - back_time
    else:
        time_comparison = 0
    
    count_dict = {}
    for i in log_data:
        if i[0] == "-" and int(i[3]) > time_comparison:
            book = database.find_by_bookID(i[1])
            label = book[1] + " | " + book[2] # sets the key to '<title> | <key>'
            if label in count_dict:
                count_dict[label] += 1
            else:
                count_dict[label] = 1
    return count_dict

def barChart(canvas,data,max_items=10):
    """This function plots a bar chart inside the provided tkinter canvas.

Parameters:
    canvas; tkinter widget: This is the canvas widget that this function will
        plot the bar chart to. Be careful as this function will clear the
        canvas before drawing.
    data; 2D list: This is the data to be plotted to the chart, in the format
        of each sublist being the label then the value.
    max_items; integer(default = 10): Maximum amount of items to plot to the
        bar chart, otherwise it will just take the first <max_items> amount
        Note: will start to overlap bars at larger values relative to canvas
        size, use at your own risk.
        

This function does not return a value.
        

"""
    # Settings
    y_offset = 10
    x_offset = 20
    gap = 25
    # End of Settings
    
    data = data[:min(max_items,len(data))]
    n = len(data)

    if n == 0:
        print("no data provided")
        return
    
    maxval = 0
    for i in data:
        maxval = max(maxval,i[1])

    canvas.delete("all")
    canvas.update()
    height = canvas.winfo_height()
    width = canvas.winfo_width()
    #print(height)
    canvas.create_line(x_offset,y_offset,x_offset,height-y_offset)

    usable_height = height - 2 * y_offset
    bar_width = round((usable_height - ((n+1) * gap)) / n)

    bar_length_mul = (width - (2 * x_offset)) / maxval # Allows the bar chart to span the full canvas area

    for i in range(0,n):
        label = data[i][0]
        value = data[i][1]
        x1 = x_offset
        y1 = gap + (i * (gap + bar_width))
        x2 = x1 + (bar_length_mul * value)
        y2 = y1 + bar_width
        colour = colorsys.hsv_to_rgb((1/n) * i,0.6,1)
        
        canvas.create_rectangle(x1,y1,x2,y2,fill="#%02x%02x%02x"%(round(colour[0] * 255),round(colour[1] * 255),round(colour[2] * 255)))
        label = "%s : %d"%(label,round(value))
        temp = canvas.create_text(0,(y1+y2)/2,text=label)
        points = canvas.bbox(temp)
        text_width = points[2] - points[0]
        if text_width < ((bar_length_mul * value) - x_offset): # makes sure the text always fits inside bar or goes on outside
            delta_x = (x_offset*2) + (text_width / 2)
        else:
            delta_x = x2 + (text_width / 2) + x_offset
        canvas.move(temp,delta_x,0)

if __name__ == "__main__": # Testing and example/demonstration:
    data = [["python",10],["C#",20],["java1",5],["java2",4],["java3",3],["java4",1],["java5",2]]
    print(getPopularity())
    
    root = Tk()
    root.title("booklist.py")
    root.geometry("1280x1080")
    root.configure(bg="lime")
    Label(root,text="Content test").pack()
    chart_canvas = Canvas(root,bg="bisque")
    chart_canvas.pack(side="left",expand = True, fill = "both")
    barChart(chart_canvas,data,500)

    
