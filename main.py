from algorithms import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.ttk import Progressbar

class gui:
    def __init__(self):
        self.window = Tk()
        self.window.title("SORTING ALGORITHMS")
        self.window.geometry("300x100")
        self.frame1 = Frame(self.window)
        self.frame1.pack()
        self.sortingAlgorithm = IntVar()
        self.selectionSort = Radiobutton(
            self.frame1, text="Selection Sort", variable=self.sortingAlgorithm, value=1)
        self.bubbleSort = Radiobutton(
            self.frame1, text="Bubble Sort", variable=self.sortingAlgorithm, value=2)
        self.insertionSort = Radiobutton(
            self.frame1, text="Insetion Sort", variable=self.sortingAlgorithm, value=3)
        self.mergeSort = Radiobutton(
            self.frame1, text="Merge Sort", variable=self.sortingAlgorithm, value=4)
        self.selectionSort.grid(row=1, column=1)
        self.bubbleSort.grid(row=1, column=2)
        self.insertionSort.grid(row=2, column=1)
        self.mergeSort.grid(row=2, column=2)
        self.progress = Progressbar(self.window, orient=HORIZONTAL,
                                    length=250, mode="determinate", takefocus=True, maximum=100)
        self.progress.pack()
        self.frame2 = Frame(self.window)
        self.frame2.pack()
        self.generate = Button(
            self.frame2, text="Genrate Graph", command=self.callSorter)
        self.showImage = Button(
            self.frame2, text="Show Graph", command=self.showGraph)
        self.showImage["state"] = "disabled"
        self.generate.grid(row=2, column=1)
        self.showImage.grid(row=2, column=2)
        self.window.mainloop()

    def callSorter(self):
        if not self.sortingAlgorithm.get():
            messagebox.showerror("ERROR", "Please Select An Option")
            return
        self.generate["state"] = "disabled"
        flag = getData(getNumbers(),self.sortingAlgorithm.get())
        if flag:
            for i in range(100):                
                self.progress.step()            
                self.window.update()
            self.showImage["state"] = "normal" 
            
    def showGraph(self):
        popup = Toplevel()
        popup.title("Graph")
        graph = ImageTk.PhotoImage(Image.open("graph.png"))
        canvas = Canvas(popup, width=660, height=500, bg='white')
        canvas.image = graph
        canvas.pack()
        canvas.create_image(10, 10, image=graph, anchor=NW)
        self.showImage["state"] = "disabled"
        self.generate["state"] = "normal"


gui()
