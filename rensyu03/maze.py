import tkinter as tk
import maze_maker as mm

def Key_down(event):
    global key
    key = event.keysym

def Key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, key
    if key == "Up":
        cy -= 20

    elif key == "Down":
        cy += 20

    elif key == "Right":
        cx += 20

    elif key == "Left":
        cx -= 20

    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるコウカトン")
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()

    tori = tk.PhotoImage(file = "fig/8.png")
    cx, cy = 300, 400
    key = ""
    root.bind("<KeyPress>", Key_down)
    root.bind("<KeyRelease>", Key_up)
    maze_bg = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_bg)
    canvas.create_image(cx, cy, image = tori, tag = "tori")
    root.after(100, main_proc)
    root.mainloop()