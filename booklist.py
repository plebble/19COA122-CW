import colorsys
import database
import time

def getPopularity(back_time = -1):
    #return [["python",10],["C#",20],["java",5],["java",5],["java",5],["java",5]]
    log_data = database.read_logfile()

    if back_time != -1:
        time_comparison = round(time.time()) - backtime
    else:
        time_comparison = 0
    
    count_dict = {}
    for i in log_data:
        if i[0] == "-" and int(i[3]) > time_comparison:
            book = database.find_by_bookID(i[1])
            label = book[1] + " | " + book[2]
            if label in count_dict:
                count_dict[label] += 1
            else:
                count_dict[label] = 1
    return count_dict

def barChart(canvas,data):
    max_items = 10
    y_offset = 10
    x_offset = 20
    gap = 25
    
    data = data[:min(max_items,len(data))]
    n = len(data)
    maxval = 0
    for i in data:
        maxval = max(maxval,i[1])

    canvas.delete("all")
    canvas.update()
    height = canvas.winfo_height()
    width = canvas.winfo_width()
    print(height)
    canvas.create_line(x_offset,y_offset,x_offset,height-y_offset)

    usable_height = height - 2 * y_offset
    bar_width = round((usable_height - ((n+1) * gap)) / n)

    bar_length_mul = (width - (2 * x_offset)) / maxval

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
        if text_width < (bar_length_mul * value):
            delta_x = (x_offset*2) + (text_width / 2)
        else:
            print(x2,label)
            delta_x = x2 + + (text_width / 2) + x_offset
        canvas.move(temp,delta_x,0)

if __name__ == "__main__":
    popularity = getPopularity()
    popularity = sorted(popularity.items() , reverse=True, key=lambda x: x[1])

    print(popularity)
