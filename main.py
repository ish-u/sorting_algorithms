from algorithms import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.ttk import Progressbar,Treeview


class gui:
    def __init__(self):
        self.window = Tk()
        self.window.title("SORTING ALGORITHMS")
        self.window.geometry("300x160")
        p = 10
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
        self.selectionSort.grid(row=1, column=1, padx=(p,p), pady=(p,p))
        self.bubbleSort.grid(row=1, column=2, padx=(p,p), pady=(p,p))
        self.insertionSort.grid(row=2, column=1, padx=(p,p), pady=(p,p))
        self.mergeSort.grid(row=2, column=2, padx=(p,p), pady=(p,p))
        self.numberOfTestCases = IntVar()
        self.progress = Progressbar(self.window, orient=HORIZONTAL,length=250, mode="determinate", takefocus=True, maximum=100, variable = self.numberOfTestCases)
        self.progress.pack()
        self.frame2 = Frame(self.window)
        self.frame2.pack()
        self.generate = Button(self.frame2, text="Genrate Graph", command=self.callSorter)
        self.showImage = Button(self.frame2, text="Show Graph", command=self.showGraph)
        self.showImage["state"] = "disabled"
        self.generate.grid(row=2, column=1, padx=(p,p), pady=(p,p))
        self.showImage.grid(row=2, column=2, padx=(p,p), pady=(p,p))
        self.window.mainloop()

    def callSorter(self):
        if not self.sortingAlgorithm.get():
            messagebox.showerror("ERROR", "Please Select An Option")
            return
        self.generate["state"] = "disabled"
        flag = self.getData(getNumbers(),self.sortingAlgorithm.get())
        if flag:
            self.showImage["state"] = "normal" 
            
    def showGraph(self):
        self.numberOfTestCases.set(0)
        popup = Toplevel()
        popup.title("Graph")
        graph = ImageTk.PhotoImage(Image.open("graph.png"))
        canvas = Canvas(popup, width=660, height=500, bg='white')
        canvas.image = graph
        canvas.pack()
        canvas.create_image(0, 0, image=graph, anchor=NW)
        Button(popup, text="View Comparions", command=self.showCSV).pack(padx=(10,10), pady=(10,10))
        self.showImage["state"] = "disabled"
        self.generate["state"] = "normal"
    
    def showCSV(self):
        csv = Toplevel(width=400,height=300)
        csv.title("Comaprisons")
        scrollbar = Scrollbar(csv, orient=VERTICAL)
        table = Treeview(csv, columns=("Input Size", "Average", "Best", "Worst"), height=300, selectmode="extended", yscrollcommand = scrollbar.set)
        scrollbar.config(command=csv.winfo_height())
        scrollbar.pack(side=RIGHT, fill=Y)
        table.heading('Input Size', text="Input Size", anchor=W)
        table.heading('Average', text="Average", anchor=W)
        table.heading('Best', text="Best", anchor=W)
        table.heading('Worst', text="Worst", anchor=W)
        table.column('#0', stretch=NO, minwidth=0, width=0)
        table.column('#1', stretch=NO, minwidth=0, width=100)
        table.column('#2', stretch=NO, minwidth=0, width=100)
        table.column('#3', stretch=NO, minwidth=0, width=100)
        table.column('#4', stretch=NO, minwidth=0, width=100)
        table.pack()

        # Filling the CSV Treeview with the Data
        comparisions = pd.read_csv('comparisions.csv')
        comparisions = comparisions.sort_values("SIZE")
        for index,comparision in comparisions.iterrows():
            table.insert("", index='end', values=(comparision["SIZE"], comparision["AVERAGE"], comparision["BEST"],comparision["WORST"]))

        
    # getData
    def getData(self,numbers,algo):
        data = []
        testCases = []
        sampleSpaceSize = 1
        while self.numberOfTestCases.get() != 100:
            random.shuffle(numbers)
            sampleSpaceSize = random.randint(1,1000)
            if sampleSpaceSize not in testCases:
                testCases.append(sampleSpaceSize)
                startIndex = random.randint(0,len(numbers)-sampleSpaceSize)
                sampleSpace = numbers[startIndex:startIndex+sampleSpaceSize]
                if algo == 1:
                    avg = selectionSort(sampleSpace)
                    best = selectionSort(sampleSpace)
                    sampleSpace.reverse()
                    worst = selectionSort(sampleSpace)
                elif algo == 2:
                    avg = bubbleSort(sampleSpace)
                    best = bubbleSort(sampleSpace)
                    sampleSpace.reverse()
                    worst = bubbleSort(sampleSpace)
                elif algo == 3:
                    avg = insertionSort(sampleSpace)
                    best = insertionSort(sampleSpace)
                    sampleSpace.reverse()
                    worst = insertionSort(sampleSpace)
                elif algo == 4:
                    avg = mergeSort(sampleSpace)
                    best = mergeSort(sampleSpace)
                    sampleSpace.reverse()
                    worst = mergeSort(sampleSpace)
                data.append(timeComplexity(avg,best,worst))
                self.numberOfTestCases.set(self.numberOfTestCases.get() + 1)             
                self.window.update()
                
        
        getComparisonCSV(data)
        getGraph()

        return 1

gui()

