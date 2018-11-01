"""
"""

from tkinter import *
import tkinter.filedialog
from tkinter.filedialog import askopenfilename
root = Tk()
root.title("Scanner")
#root.geometry("500x500")
root.resizable(width=True,height=True)
img = PhotoImage(file="btn.png") ##import
##img = img.zoom(3)
##img = img.subsample(12)
cnv = PhotoImage(file="convert.png")
##cnv = cnv.subsample(5)
output_file = 'reg.txt'

def read_out():
    file_object = open(output_file)
    file_content = file_object.read()
    file_object.close()
    my_text.replace("1.0","end-1c",file_content)
    root.after(40,read_out) ##get output_file
    

    
def ask_open_file(event):
    filename = askopenfilename(parent=root,filetypes=[("Text files","*.txt")])
    input_f = open(filename,'r')
    input_list = input_f.readlines()
    input_lines = ''.join(input_list)
    entry.replace("1.0","end-1c",input_lines)
    input_f.close()
    

def read_Entry(event):
    
    lines = entry.get("1.0","end-1c")
    if(lines!=''):
        lines_list = lines.split('\n')
        #to lower
        # for i,ln in enumerate(lines_list):
        #     ln = ln.lower()
        #     lines_list[i]=ln
        
        for i,line in enumerate(lines_list) :
            if(line!=''):
                #our work here
                pass
        
        fob = open(output_file,'w')
        for line in lines_list:
            fob.write(line+'\n')
        fob.close
        read_out()##get_output_file
    
def changeCursor(event):
    event.widget.config(cursor="hand2")

##Front End
left_half = Frame(root,padx=10)
upper_part = Frame(left_half,padx=10,pady=10)
Label(upper_part,text = "write your code ",font=("Courier",13)).pack(side=LEFT,fill=Y,expand=1)#pack
ask_open = Button(upper_part,text = 'or import from file ..',image=img)
ask_open["border"]="0"
ask_open.pack(side=LEFT,fill=Y)#pack
ask_open.bind("<Motion>",changeCursor)
ask_open.bind("<Button-1>",ask_open_file)
upper_part.pack(expand=1)
#upper_part_done
mid_part = Frame(left_half)
entry = Text(mid_part,width=40,height=15,background="#d9fcf1")##height
entry.pack(side=LEFT, fill = Y,expand=1) #pack
entry.config(undo=True)
scroll = Scrollbar(mid_part,command=entry.yview)
entry['yscrollcommand'] = scroll.set
scroll.pack(side =LEFT, fill = Y,expand=1)#pack
mid_part.pack(expand=1,fill=Y)
#mid_part_is_over
lower_part = Frame(left_half)
add = Button(lower_part,text = "CONVERT!",image=cnv)
add["border"]="0"
add.pack(fill=Y)#pack
add.bind("<Motion>",changeCursor)
add.bind("<Button-1>",read_Entry)
lower_part.pack(expand=1,fill=Y,pady=10)
### left part over
left_half.pack(side="left",fill=Y,expand=1)
##output_file
right_half = Frame(root)
my_reg_frame = Frame(right_half, bd=2, relief=SUNKEN)
Label(my_reg_frame,text = "Output File Contents",font=("Courier",13),pady = 10).pack()#pack
#text widget and associated Scrollbar widget
my_text=Text(my_reg_frame, height=15, width =40,pady = 10)

my_text.pack(side=LEFT, fill=Y, padx=5)

#add scrollbar widget to the text widget
my_scrollbar = Scrollbar(my_reg_frame, orient=VERTICAL, command=my_text.yview)
my_scrollbar.pack(fill=Y,expand=1,side=LEFT)
my_text.configure(yscrollcommand=my_scrollbar.set)
my_reg_frame.pack(pady=10,fill=Y,expand=1,side=LEFT) #reg frame
right_half.pack(side="left",expand=1,fill=Y,pady=5)#right half


root.mainloop()
