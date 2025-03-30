import tkinter as tk

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase(event):
    """ Erases the blue rectangles that the eraser touches """
    eraser_x, eraser_y = event.x, event.y
    
    for rect in grid_cells:
        x1, y1, x2, y2 = canvas.coords(rect)
        # Check if the eraser overlaps with the grid cell
        if not (x2 < eraser_x or x1 > eraser_x + ERASER_SIZE or y2 < eraser_y or y1 > eraser_y + ERASER_SIZE):
            canvas.itemconfig(rect, fill='white')

def create_grid():
    """ Creates a grid of blue cells """
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            rect = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill='blue', outline='black')
            grid_cells.append(rect)

# Initialize Tkinter window
root = tk.Tk()
root.title("Eraser on Canvas")
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
canvas.pack()

grid_cells = []
create_grid()

# Bind mouse motion event to the erase function
canvas.bind('<B1-Motion>', erase)  # Erases when left mouse button is held and dragged

root.mainloop()
