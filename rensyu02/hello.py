print("hello world")

import tkinter as tk
import tkinter.messagebox as tkm
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")
    #tkm.showwarning("警告", "ボタン押したらダメっていったじゃん")

root = tk.Tk()
root.title("おためしか")
root.geometry("500x200")

label = tk.Label(root, text = "らべるを書いてみた剣", font = ("Ricty Diminished", 20))
label.pack()
button = tk.Button(root, text= "押すな", command = button_click)
button.bind("<1>", button_click)
button.pack()

entry = tk.Entry(width = 30)
entry.insert(tk.END,"fugapiyo")
entry.pack()

root.mainloop()