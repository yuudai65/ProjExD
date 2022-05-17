import tkinter as tk
import maze_maker as mm
import random
import tkinter.messagebox as tkm

def pic():#ランダムでこうかとんの画像の名前を返す
    a = random.randint(0, 10)
    img_lst = [(f"fig/{i}.png") for i in range(10)] #内包表記  
    return img_lst[a]

        

def Key_down(event):
    global key
    key = event.keysym

def Key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, key, mx, my, key
    cx = 100 * mx + 50
    cy = 100 * my + 50
    if key == "Up" and maze_bg[my-1][mx] == 0:
        my -= 1
        

    if key == "Down" and maze_bg[my+1][mx] == 0:
        my += 1


    if key == "Left" and maze_bg[my][mx-1] == 0:
        mx -= 1

    if key == "Right" and maze_bg[my][mx+1] == 0:
        mx += 1

    cx = 100 * mx + 50
    cy = 100 * my + 50


    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)

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
    root.title("迷えるコウカトン")
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()

    mx, my = 1,1
    cx, cy = 100*mx+50, 100*my+50
    key = ""
    root.bind("<KeyPress>", Key_down)
    root.bind("<KeyRelease>", Key_up)
    maze_bg = mm.make_maze(15, 9)
    pic()
    tori = tk.PhotoImage(file = pic())
    mm.show_maze(canvas, maze_bg)
    canvas.create_image(cx, cy, image = tori, tag = "tori")
    root.after(100, main_proc)

    root = tk.Tk()
    label = tk.Label(root,font =  ("Times New Roman",80))
    label.pack()
    tmr = 0 #1000ms後にcount_up関数が自動で実行されるroot.after(1000, count_up)
    jid = None
    #root.after(1000, count_up)
    root.bind("<KeyPress>", key_down) 
    label.pack()     #何かのキーが押されたらkey_down関数が実行される
    root.mainloop()
   

    