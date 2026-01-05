import tkinter as tk


LIGHT_GRAY = "#8E8E8E"
DARK_GRAY = "#1D1D1D"
LABEL_COLOUR = "#FFFFFF"
LIGHT_RED = "#FF6666"
SMALL_FONT_STYLE = ("Calibri",16)
LARGE_FONT_STYLE = ("Calibri",40,"bold")
DEFAULT_FONT_STYLE = ("Calibri",20)
class Calculator:
    def __init__(self):
        self.window =tk.Tk()
        self.window.geometry("375x667") #resolution of iphone 8
        self.window.resizable(0,0) #disable resizing
        self.window.title("Calculator") #adds title to calculator
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_expression = ""
        self.current_expression = ""
        self.total_label, self.current_label = self.create_display_labels()
        self.digits = {7: (1, 1), 8: (1, 2), 9: (1, 3),
                       4: (2, 1), 5: (2, 2), 6: (2, 3),
                       1: (3, 1), 2: (3, 2), 3: (3, 3),
                       0: (4, 2), '.': (4, 1)}  #dictionary for button positions
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"} #unicode for division and multiplication symbols
        self.buttons_frame.rowconfigure(0, weight=1) #makes rows and columns expand equally
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1) #makes rows and columns expand equally
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.create_clear_button()
        self.create_equals_button()

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=DARK_GRAY, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1
    
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=DARK_GRAY, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, columnspan=3,sticky=tk.NSEW)
    
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()
        return self.clear
    
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_RED, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2,sticky=tk.NSEW)
        return button
    
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()
            self.total_expression = ""

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
    
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()   

    def create_digit_buttons(self): #digit buttons
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=DARK_GRAY, fg=LABEL_COLOUR, font=LARGE_FONT_STYLE, command = lambda x=digit: self.add_to_expression(x), borderwidth=0)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW) #sticky for sticking buttons to North South East West

    def create_buttons_frame(self): #button frame
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=self.total_expression)
    def update_label(self):
        self.current_label.config(text=self.current_expression)
    def run(self):
        self.window.mainloop() #helps run calculator

if __name__ == "__main__":
    calc = Calculator() #runs only when calc.py is run as script from terminal
    calc.run()
