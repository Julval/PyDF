# BE AWARE OF POTENTIAL EYE CANCER AHEAD
# This is my first time dealing with tkinter so some of this code might horrible to look at


import tkinter as tk
import tkinter.filedialog
from tkinter import ttk, messagebox
from PyPDF2 import PdfFileWriter, PdfFileReader

#Setup of secondary window 
def removepages_button():
    global entry_pages
    popup = tk.Toplevel()
    popup.title('Remove pages')

    label_browse = ttk.Label(master=popup,textvariable=file_path)
    label_browse.grid(row=0, column=0)
    button_browse = ttk.Button(master=popup,text="Choose file", command=browse_button)
    button_browse.grid(row=1, column=0)
    label_pages = ttk.Label(master=popup,text='Which pages would you like to keep?')
    label_pages.grid(row=2, column=0)
    label_explain = ttk.Label(master=popup,text='Format: 1,2,3')
    label_explain.grid(row=3, column=0)
    entry_pages = ttk.Entry(popup)
    entry_pages.grid(row=4,column=0)
    button_remove = ttk.Button(master=popup,text="Remove pages", command=remove_button)
    button_remove.grid(row=5, column=0)
    button_close = ttk.Button(master=popup,text="Close", command=popup.destroy)
    button_close.grid(row=6, column=0)
    popup.mainloop()

#Setup of secondary window 
def mergefiles_button():
    popup = tk.Toplevel()
    popup.title('Merge files')

    label_browse = ttk.Label(master=popup,text='Select your files:')
    label_browse.grid(row=0, column=0)

    label_browse = ttk.Label(master=popup,textvariable=file_path)
    label_browse.grid(row=1, column=0)
    button_browse = ttk.Button(master=popup,text="Choose first file", command=browse_button)
    button_browse.grid(row=2, column=0)


    label_space = ttk.Label(master=popup,text='    ')
    label_space.grid(row=3, column=0)
    label_browse = ttk.Label(master=popup,textvariable=file_path2)
    label_browse.grid(row=4, column=0)
    button_browse2 = ttk.Button(master=popup,text="Choose second file", command=browse_button2)
    button_browse2.grid(row=5, column=0)
    
    label_space2 = ttk.Label(master=popup,text='    ')
    label_space2.grid(row=6, column=0)
    button_merge = ttk.Button(master=popup,text="Merge", command=mergefiles)
    button_merge.grid(row=7, column=0)

    button_close = ttk.Button(master=popup,text="Close", command=popup.destroy)
    button_close.grid(row=10, column=0)
    popup.mainloop()

def mergefiles():
    #Creating paths and getting the number of pages in the different files
    infile = PdfFileReader(filename,'rb')
    numberofpages = infile.getNumPages()
    infile2 = PdfFileReader(filename2,'rb')
    numberofpages2 = infile2.getNumPages()
    output = PdfFileWriter()
    outpath = tk.filedialog.asksaveasfile(mode='wb',defaultextension='.pdf',title='Save New File')

    #adding first set of pages
    for i in range(numberofpages):
        output.addPage(infile.getPage(i))
    #adding second set of pages
    for j in range(numberofpages2):
        output.addPage(infile2.getPage(j))
    #writing final file
    with outpath as f:
        output.write(f)
        tk.messagebox.showinfo('Info','Files merged successfully')

    outpath.close()

#Function to select path of a file
def browse_button():
    global file_path, filename
    filename = tk.filedialog.askopenfilename()
    file_path.set(filename)

#Function to select path of a second file
def browse_button2():
    global file_path2, filename2
    filename2 = tk.filedialog.askopenfilename()
    file_path2.set(filename2)

# Function that removes chosen pages
def remove_button():
    #Checks if a file has been selected
    try:
        filename
    except NameError:
        tk.messagebox.showerror('Error', 'Please select a file to manage first')
    else:
        #Makes list from entry
        num_pages_keep = entry_pages.get()
        #Creating new lists with list comprehension
        list_pages_keep = [int(k) for k in num_pages_keep.split(',')]
        new_list_pages_keep = [x-1 for x in list_pages_keep]

        # Defining paths
        infile = PdfFileReader(filename,'rb')
        output = PdfFileWriter()
        outpath = tk.filedialog.asksaveasfile(mode='wb',defaultextension='.pdf',title='Save New File')

        #adds selected pages to new file
        for i in new_list_pages_keep:
            p = infile.getPage(i)
            output.addPage(p)
        #Writes new file
        with outpath as f:
            output.write(f)
            tk.messagebox.showinfo('Info','Pages removed successfully')


#Main window
root = tk.Tk()
root.title('PyDF')

label_start = ttk.Label(master=root,text='What do you want to do?')
label_start.grid(row=0, column=0)
button_removepages = ttk.Button(text="Remove pages", command=removepages_button)
button_removepages.grid(row=1, column=0)
button_merge = ttk.Button(root,text="Merge files",command=mergefiles_button)
button_merge.grid(row=2,column=0)
button_quit = ttk.Button(root,text="Quit",command=root.destroy)
button_quit.grid(row=10,column=0)

file_path = tk.StringVar()
file_path2 = tk.StringVar()

tk.mainloop()