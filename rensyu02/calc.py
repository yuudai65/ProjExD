import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x450")
    for i in range(0, 10):
        suji = tk.Button(root, text= i, font = ("Times New Roman", 30))
        suji.pack()
    root.mainloop()