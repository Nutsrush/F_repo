import tkinter as tk


def main():
    root = tk.Tk()
    calculate = Calculate(root)
    root.mainloop()


class Calculate:
    def __init__(self, master):
        self.label_input = tk.Label(master, width=20, height=2, bg='grey', fg='black')
        self.label_output = tk.Label(master, width=20, height=2, bg='dark blue', fg='white')
        self.button_plus = tk.Button(master, text='+', width=20, height=2)
        self.button_minus = tk.Button(master, text='-', width=20, height=2)
        self.button_multiplicate = tk.Button(master, text='*', width=20, height=2)
        self.button_division = tk.Button(master, text='/', width=20, height=2)

        self.label_input.pack()
        self.label_output.pack()
        self.button_plus.pack()
        self.button_minus.pack()
        self.button_multiplicate.pack()
        self.button_division.pack()


if __name__ == "__main__":
    main()
