import tkinter as tk
from square import square
# from pynput.keyboard import Key, Listener
import keyboard

cells = []
player_pos = [3, 3]

def main():
    print("hello")
    root = tk.Tk()
    root.title("Collect Crystals")
    root.configure(background="red")
    # root.minsize(720, 480)
    # root.maxsize(720, 480)
    root.geometry("700x700+300+0")
    
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
    root.bind("<Right>", movement)

    root.mainloop()

def movement(direction):
    player_row = player_pos[0]
    player_col = player_pos[1]
    if direction.keysym == "Right":
        print(player_row)
        print(player_col)
        cells[player_row][player_col].set_empty()
        print("Right")


if __name__ == "__main__":
    main()