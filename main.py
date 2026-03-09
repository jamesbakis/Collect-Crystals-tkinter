import tkinter as tk
from square import square

cells = []
player_pos = [3, 3]

def move_right(direction):
    player_row = player_pos[0]
    player_col = player_pos[1]    
    cells[player_row][player_col].set_empty()
    print("right")

def move_left(direction):
    player_row = player_pos[0]
    player_col = player_pos[1]    
    cells[player_row][player_col].set_empty()
    print("left")

def move_up(direction):
    player_row = player_pos[0]
    player_col = player_pos[1]    
    cells[player_row][player_col].set_empty()
    print("up")

def move_down(direction):
    player_row = player_pos[0]
    player_col = player_pos[1]    
    cells[player_row][player_col].set_empty()
    print("down")

def main():
    print("hello")
    root = tk.Tk()
    root.title("Collect Crystals")
    root.configure(background="red")
    root.geometry("700x700+300+0")
    # root.minsize(720, 480)
    # root.maxsize(720, 480)
    
    # label1 = tk.Label(root, text="Collect crystals!")
    # label2 = tk.Label(root, text="Avoid enemies!")
    
    # label1.pack()
    # label2.pack()
    

    for row in range(7):
        cells.append([])
        for col in range(7):
            cell = square(root, row, col)
            if row==col==3:
                 cell.set_player()
            else:
                cell.set_empty()
            cells[row].append(cell)
    root.bind("<Right>", move_right)
    root.bind("<Left>", move_left)
    root.bind("<Up>", move_up)
    root.bind("<Down>", move_down)

    root.mainloop()

if __name__ == "__main__":
    main()