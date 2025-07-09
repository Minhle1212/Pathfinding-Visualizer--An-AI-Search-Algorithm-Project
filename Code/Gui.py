import tkinter as tk
import sys


def draw_map(city_map, path, start, goal):
    root = tk.Tk()
    root.title("Pathfinding Visualization")

    rows = len(city_map)
    cols = len(city_map[0])

    canvas = tk.Canvas(root, width=cols * 40, height=rows * 40)
    canvas.pack()

    colors = {
        'empty': 'white',
        'wall': 'black',
        'start': 'red',
        'goal': 'green',
        'path': 'blue'
    }

    for row in range(rows):
        for col in range(cols):
            x1, y1 = col * 40, row * 40
            x2, y2 = x1 + 40, y1 + 40
            color = colors['empty']
            if city_map[row][col] == 1:
                color = colors['wall']
            if (row, col) in path:
                color = colors['path']
 
            if (row, col) == start:
                color = colors['start']
            if (row, col) == goal:
                color = colors['goal']

            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    root.mainloop()

def main():
    if len(sys.argv) != 2:
        print("Usage: python gui.py <datafile>")
        return

    datafile = sys.argv[1]
    

    with open(datafile, 'r') as f:
        lines = f.readlines()

  
    rows, cols = eval(lines[0].strip())
    city_map = []

    for i in range(1, rows + 1):
        city_map.append([int(x) for x in lines[i].strip().split()])


    start = eval(lines[rows + 1].strip())
    goal = eval(lines[rows + 2].strip())

 
    path = [eval(p.strip()) for p in lines[rows + 3:]]

    draw_map(city_map, path, start, goal)

if __name__ == "__main__":
    main()
