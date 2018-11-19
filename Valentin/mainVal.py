from game2048_Val.grid_2048 import *
from game2048_Val.display_grid_2048 import *
from game2048_Val.textual_2048 import *


from tkinter import *


SIZE = 1000
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = {   2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", \
                            32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", \
                            512:"#edc850", 1024:"#edc53f", 2048:"#edc22e" }
CELL_COLOR_DICT = { 2:"#776e65", 4:"#776e65", 8:"#f9f6f2", 16:"#f9f6f2", \
                    32:"#f9f6f2", 64:"#f9f6f2", 128:"#f9f6f2", 256:"#f9f6f2", \
                    512:"#f9f6f2", 1024:"#f9f6f2", 2048:"#f9f6f2" }
FONT = ("Verdana", 40, "bold")


KEY_UP = "'z'"
KEY_DOWN = "'s'"
KEY_LEFT = "'q'"
KEY_RIGHT = "'d'"



"""grid_actual = init_grid(GRID_LEN)

init_interface(grid_actual)"""



root = Tk()

def callback(event):
    print("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()




