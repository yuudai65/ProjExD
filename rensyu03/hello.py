import tkinter as tk
import tkinter.messagebox as tkm
def key_down(event):
    global jid
    if jid != None:
        root.after_cancel(jid)
        jid = None
        return 
    key = event.keysym
    tkm.showinfo("キー押下", f"{key}が押されました")
    jid = root.after(0, count_up)

def count_up():
    global tmr, jid
    tmr = tmr+1
    label["text"] = tmr
    jid = root.after(1000, count_up)

if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(root,font =  ("Times New Roman",80))
    label.pack()
    tmr = 0 #1000ms後にcount_up関数が自動で実行されるroot.after(1000, count_up)
    jid = None
    #root.after(1000, count_up)
    root.bind("<KeyPress>", key_down) 
    label.pack()     #何かのキーが押されたらkey_down関数が実行される
    root.mainloop()
