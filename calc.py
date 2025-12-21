import tkinter as tk


class Calculator:
    def __init__(self):
        self.window =tk.Tk()
        self.window.geometry("375x667") #resolution of iphone 8
        self.window.resizable(0,0) #disable resizing
        self.window.title("Calculator") #adds title to calculator

    def run(self):
        self.window.mainloop() #helps run calculator

if __name__ == "__main__":
    calc = Calculator() #runs only when calc.py is run as script from terminal
    calc.run()
