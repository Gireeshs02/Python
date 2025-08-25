import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.input_text = tk.StringVar()

        self.display = tk.Entry(root, textvariable=self.input_text, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
        self.display.pack(fill="both", ipadx=8, ipady=8, pady=10, padx=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "3", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "C", "+"],
            ["=",]
        ]
            
        for row in buttons:
            frame = tk.Frame(self.root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(frame, text=char, font=("Arial", 16), relief='ridge',
                                    command=lambda c=char: self.on_button_click(c))
                btn.pack(side="left", expand=True, fill="both")
        
    def on_button_click(self, char):
        if char == 'C':
            self.input_text.set("")
        elif char == "=":
            try:
                expression = self.input_text.get()
                result = str(eval(expression))
                self.input_text.set(result)
            except Exception:
                self.input_text.set("Error")
        else:
            current = self.input_text.get()
            self.input_text.set(current + char)

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()