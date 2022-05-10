import tkinter as tk
import maze_maker as mm

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



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるコウカトン")
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()

    tori = tk.PhotoImage(file = "fig/8.png")
    mx, my = 1,1
    cx, cy = 100*mx+50, 100*my+50
    key = ""
    root.bind("<KeyPress>", Key_down)
    root.bind("<KeyRelease>", Key_up)
    maze_bg = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_bg)
    canvas.create_image(cx, cy, image = tori, tag = "tori")
    root.after(100, main_proc)
    root.mainloop()