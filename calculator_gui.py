import tkinter as tk
from calculator import Calculator

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.cal = Calculator()
        self.result = tk.StringVar()
        self.result.set("")
        self.create_widget()



    def create_widget(self):

        self.result_display = tk.Entry(self.root, textvariable=self.result, font=("Arial", 24), width=15, borderwidth=2, relief="solid")

        self.result_display.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+',
            'sin', 'cos', 'tan', 'sqrt',
            'log', 'exp', 'fact', 'x^y'
        ]

        row, col = 1, 0
        for button in buttons:
            b = tk.Button(self.root, text=button, width=5, height=3, font=("Arial", 18), command=lambda btn=button: self.on_click(btn))
            b.grid(row=row, column=col)
            col+=1
            if col > 3:
                col = 0
                row+=1


    def on_click(self, button):
        current_text = self.result.get()

        if button == "C":
            self.result.set("")
        elif button == '=':
            try:
                result = self.cal.calculate(current_text)
                self.result.set(result)
            except Exception as e:
                self.result.set("Error")

        elif button == 'sqrt':
            try:
                result = self.cal.square_root(float(current_text))
                self.result.set(result)
            except ValueError:
                self.result.set("Error")

        elif button == 'log':
            try:
                result = self.cal.logarithm(float(current_text))
                self.result.set(result)
            except ValueError:
                self.result.set("Error")
        elif button == 'fact':
            try:
                result = self.cal.factorial(int(current_text))
                self.result.set(result)
            except ValueError:
                self.result.set("Error")
        elif button == 'x^y':
            self.result.set(current_text + "**")  # Allow for exponentiation syntax
        elif button in ['sin', 'cos', 'tan']:
            try:
                angle = float(current_text)
                if button == 'sin':
                    result = self.cal.sin(angle)
                elif button == 'cos':
                    result = self.cal.cos(angle)
                elif button == 'tan':
                    result = self.cal.tan(angle)
                self.result.set(result)
            except ValueError:
                self.result.set("Error")
        else:
            # Handle all numeric and operator buttons
            self.result.set(current_text + button)                                


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

        