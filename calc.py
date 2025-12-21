import tkinter as tk


LIGHT_GRAY = "#8E8E8E"
DARK_GRAY = "#1D1D1D"
LABEL_COLOUR = "#FFFFFF"
SMALL_FONT_STYLE = ("Calibri",16)
LARGE_FONT_STYLE = ("Calibri",40,"bold")
class Calculator:
    def __init__(self):
        self.window =tk.Tk()
        self.window.geometry("375x667") #resolution of iphone 8
        self.window.resizable(0,0) #disable resizing
        self.window.title("Calculator") #adds title to calculator
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_expression = "0"
        self.current_expression = "0"
        self.total_label, self.current_label = self.create_display_labels()
        self.digits = {7: (1, 1), 8: (1, 2), 9: (1, 3),
                       4: (2, 1), 5: (2, 2), 6: (2, 3),
                       1: (3, 1), 2: (3, 2), 3: (3, 3),
                       0: (4, 2), '.': (4, 1)}  #dictionary for button positions
        self.buttons_frame = self.create_digit_buttons()



    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text =self.total_expression, anchor=tk.E, bg=DARK_GRAY, fg=LABEL_COLOUR, padx=24, font=SMALL_FONT_STYLE) #East side of frame
        current_label = tk.Label(self.display_frame, text =self.current_expression, anchor=tk.E, bg=DARK_GRAY, fg=LABEL_COLOUR, padx=24, font=LARGE_FONT_STYLE)
        total_label.pack(expand=True, fill="both")
        current_label.pack(expand=True, fill="both")
        return total_label, current_label
    
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=200,bg=DARK_GRAY) #height of window and bg colour
        frame.pack(expand=True, fill="both") #packs frame to main window, expands to fill available space, both directions
        return frame

    def create_digit_buttons(self): #digit buttons
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=LIGHT_GRAY, fg=LABEL_COLOUR, font=LARGE_FONT_STYLE)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW) #sticky for sticking buttons to North South East West

    def create_buttons_frame(self): #button frame
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop() #helps run calculator

if __name__ == "__main__":
    calc = Calculator() #runs only when calc.py is run as script from terminal
    calc.run()
