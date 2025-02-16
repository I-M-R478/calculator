import tkinter as tk
from calculator import Calculator

# Define the main application class
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.cal = Calculator()
        self.result = tk.StringVar()
        self.result.set("")
        self.create_widget()

    # Function to create the calculator UI widgets
    def create_widget(self):
        # Create the display for showing results
        self.result_display = tk.Entry(self.root, textvariable=self.result, font=("Arial", 24), width=15, borderwidth=2, relief="solid")
        self.result_display.grid(row=0, column=0, columnspan=4)

        # Define the buttons for the calculator
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+',
            'sin', 'cos', 'tan', 'sqrt',
            'log', 'exp', 'fact', 'x^y'
        ]

        # Create and place the buttons in the grid layout
        row, col = 1, 0
        for button in buttons:
            b = tk.Button(self.root, text=button, width=5, height=3, font=("Arial", 18), command=lambda btn=button: self.on_click(btn))
            b.grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    # Function to handle button clicks
    def on_click(self, button):
        current_text = self.result.get()

        if button == "C":
            # Clear the display
            self.result.set("")
        elif button == '=':
            try:
                # Calculate the result
                result = self.cal.calculate(current_text)
                self.result.set(result)
            except Exception as e:
                self.result.set("Error")
        elif button == 'sqrt':
            try:
                # Calculate the square root
                result = self.cal.square_root(float(current_text))
                self.result.set(result)
            except ValueError:
                self.result.set("Error")
        elif button == 'log':
            try:
                # Calculate the logarithm
                result = self.cal.logarithm(float(current_text))
                self.result.set(result)
            except ValueError:
                self.result.set("Error")
        elif button == 'fact':
            try:
                # Calculate the factorial
                result = self.cal.factorial(int(current_text))
                self.result.set(result)
            except ValueError:
                self.result.set("Error")
        elif button == 'x^y':
            # Prepare for exponentiation input
            self.result.set(current_text + "**")
        elif button in ['sin', 'cos', 'tan']:
            try:
                # Calculate the trigonometric function
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

# Main entry point of the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
