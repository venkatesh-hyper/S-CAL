from tkinter import Tk, Entry, Button, Frame, StringVar, ttk, messagebox, Label
from math import sin, cos, log, exp, pow, sqrt

import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Variables
        self.current_input = StringVar()

        # Entry
        self.entry = Entry(master, textvariable=self.current_input, width=20, font=('Helvetica', 16), bd=10, insertwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Notebook (Tabs)
        self.notebook = ttk.Notebook(master)
        self.notebook.grid(row=1, column=0, columnspan=4)

        # Simple Calculator Tab
        self.simple_frame = Frame(self.notebook)
        self.notebook.add(self.simple_frame, text="Simple")

        # Scientific Calculator Tab
        self.scientific_frame = Frame(self.notebook)
        self.notebook.add(self.scientific_frame, text="Scientific")

        # CGPA Calculator Tab
        self.cgpa_frame = Frame(self.notebook)
        self.notebook.add(self.cgpa_frame, text="CGPA")

        # GST Calculator Tab
        self.gst_frame = Frame(self.notebook)
        self.notebook.add(self.gst_frame, text="GST")

        # Create and place buttons on the Simple Calculator tab
        simple_buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        self.create_buttons(simple_buttons, self.simple_frame)

        # Create and place buttons on the Scientific Calculator tab
        scientific_buttons = [
            'sqrt', 'pow', '(', ')',
            'sin', 'cos', 'tan',
            'log', 'exp', 'pi',
            '1/x', 'x^2', 'x^3',
            '!', 'log2', 'ln'
            
        ]

        self.create_buttons(scientific_buttons, self.scientific_frame, row_start=0, col_start=0)

        # Create and place numpad on the Scientific Calculator tab
        numpad_buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', 'C'
        ]

        self.create_buttons(numpad_buttons, self.scientific_frame, row_start=5, col_start=0)

        # Labels and Entry for CGPA Calculator
        Label(self.cgpa_frame, text="Enter Marks for Subject 1:").grid(row=1, column=0, columnspan=2, pady=10)
        self.subject1_entry = Entry(self.cgpa_frame, width=10)
        self.subject1_entry.grid(row=1, column=2)

        Label(self.cgpa_frame, text="Enter Marks for Subject 2:").grid(row=2, column=0, columnspan=2, pady=10)
        self.subject2_entry = Entry(self.cgpa_frame, width=10)
        self.subject2_entry.grid(row=2, column=2)

        Label(self.cgpa_frame, text="Enter Marks for Subject 3:").grid(row=3, column=0, columnspan=2, pady=10)
        self.subject3_entry = Entry(self.cgpa_frame, width=10)
        self.subject3_entry.grid(row=3, column=2)

        Label(self.cgpa_frame, text="Enter Marks for Subject 4:").grid(row=4, column=0, columnspan=2, pady=10)
        self.subject4_entry = Entry(self.cgpa_frame, width=10)
        self.subject4_entry.grid(row=4, column=2)

        Label(self.cgpa_frame, text="Enter Marks for Subject 5:").grid(row=5, column=0, columnspan=2, pady=10)
        self.subject5_entry = Entry(self.cgpa_frame, width=10)
        self.subject5_entry.grid(row=5, column=2)

        Button(self.cgpa_frame, text="Calculate CGPA", command=self.calculate_cgpa).grid(row=6, column=0, columnspan=3, pady=10)

        # Labels and Entry for GST Calculator
        Label(self.gst_frame, text="Enter Amount:").grid(row=1, column=0, columnspan=2, pady=10)
        self.amount_entry = Entry(self.gst_frame, width=10)
        self.amount_entry.grid(row=1, column=2)

        Label(self.gst_frame, text="Enter GST Rate (%):").grid(row=2, column=0, columnspan=2, pady=10)
        self.gst_rate_entry = Entry(self.gst_frame, width=10)
        self.gst_rate_entry.grid(row=2, column=2)

        Button(self.gst_frame, text="Calculate GST", command=self.calculate_gst).grid(row=3, column=0, columnspan=3, pady=10)

        # Bind the tab change event
        self.notebook.bind('<<NotebookTabChanged>>', self.on_tab_change)

    def create_buttons(self, button_list, frame, row_start=1, col_start=0):
        r, c = row_start, col_start
        for button in button_list:
            Button(frame, text=button, width=5, height=2, command=lambda b=button: self.on_button_click(b)).grid(row=r, column=c, padx=5, pady=5)
            c += 1
            if c > col_start + 3:
                c = col_start
                r += 1

    def on_button_click(self, button):
        if button == '=':
            try:
                result = eval(self.current_input.get())
                self.current_input.set(result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid expression: {e}")
        elif button == 'C':
            self.current_input.set('')
        elif button == 'sqrt':
            self.current_input.set(self.current_input.get() + '**0.5')
        elif button == 'pow':
            self.current_input.set(self.current_input.get() + '**')
        elif button == 'sin':
            self.current_input.set('sin(' + self.current_input.get() + ')')
        elif button == 'cos':
            self.current_input.set('cos(' + self.current_input.get() + ')')
        elif button == 'tan':
            self.current_input.set('tan(' + self.current_input.get() + ')')
        elif button == 'log':
            self.current_input.set('log(' + self.current_input.get() + ')')
        elif button == 'exp':
            self.current_input.set('exp(' + self.current_input.get() + ')')
        elif button == 'pi':
            self.current_input.set(math.pow(math.pi, float(self.current_input.get())))
        elif button == '1/x':
            self.current_input.set('1/' + self.current_input.get())
        elif button == 'x^2':
            self.current_input.set('(' + self.current_input.get() + ')**2')
        elif button == 'x^3':
            self.current_input.set('(' + self.current_input.get() + ')**3')
        elif button == '!':
            self.current_input.set('factorial(' + self.current_input.get() + ')')
        elif button == 'log2':
            self.current_input.set('log(' + self.current_input.get() + ',2' + ')')
        elif button == 'ln':
            self.current_input.set('log(' + self.current_input.get() + ',math.e' + ')')
        else:
            self.current_input.set(self.current_input.get() + button)

    def calculate_cgpa(self):
        try:
            marks_subject1 = float(self.subject1_entry.get())
            marks_subject2 = float(self.subject2_entry.get())
            marks_subject3 = float(self.subject3_entry.get())
            marks_subject4 = float(self.subject4_entry.get())
            marks_subject5 = float(self.subject5_entry.get())

            total_marks = marks_subject1 + marks_subject2 + marks_subject3 + marks_subject4 + marks_subject5
            cgpa = total_marks / 50  # Assuming total marks for all subjects is 50
            messagebox.showinfo("CGPA Result", f"Your CGPA is: {cgpa:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid marks for all subjects.")

    def calculate_gst(self):
        try:
            amount = float(self.amount_entry.get())
            gst_rate = float(self.gst_rate_entry.get())

            gst = (gst_rate / 100) * amount
            total_amount = amount + gst

            messagebox.showinfo("GST Result", f"GST Amount: {gst:.2f}\nTotal Amount (including GST): {total_amount:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid values for amount and GST rate.")

    def on_tab_change(self, event):
        # Check which tab is currently selected
        current_tab = self.notebook.index(self.notebook.select())

        # Adjust the size of the calculator based on the selected tab
        if current_tab == 1:  # Scientific Calculator tab
            self.master.geometry("400x700")
        else:
            self.master.geometry("400x500")


if __name__ == "__main__":
    root = Tk()
    app = Calculator(root)
    root.mainloop()
