import tkinter as tk
from square import square
import random

cells = []
pos = [3, 3]

points = [0]

enemy_1 = [0, 0]

enemy_2 = [0, 6]

enemy_3 = [6, 3]

crystal = [0, 3]

enemy_all = (enemy_1, enemy_2, enemy_3)

units_all = (enemy_1, enemy_2, enemy_3, pos)

def enemy_collision():
    for enemy in enemy_all:
        if pos[0] == enemy[0] and pos[1] == enemy[1]:
            exit()

def crystal_collision(points):    
    for unit in units_all:
        if crystal[0] == unit[0] and crystal[1] == unit[1]:
            if unit == pos:
                points[0] += 1
            x = random.randint(0, 6)
            y = random.randint(0, 6)
            while [x, y] in units_all:
                x = random.randint(0, 6)
                y = random.randint(0, 6)
            cells[x][y].set_crystal()
            break


def move_right(direction): 
    move_enemy(enemy_all)   
    cells[pos[0]][pos[1]].set_empty()
    if pos[1] == 6:
        pos[1] = 0
    else:
        pos[1] += 1
    cells[pos[0]][pos[1]].set_player()
    crystal_collision(points)
    enemy_collision()

def move_left(direction):   
    move_enemy(enemy_all) 
    cells[pos[0]][pos[1]].set_empty()
    if pos[1] == 0:
        pos[1] =6
    else:
        pos[1] -= 1
    cells[pos[0]][pos[1]].set_player()
    crystal_collision(points)
    enemy_collision()

def move_up(direction):   
    move_enemy(enemy_all) 
    cells[pos[0]][pos[1]].set_empty()
    if pos[0] == 0:
        pos[0] = 6
    else:
        pos[0] -= 1
    cells[pos[0]][pos[1]].set_player()
    crystal_collision(points)
    enemy_collision()

def move_down(direction):
    move_enemy(enemy_all) 
    cells[pos[0]][pos[1]].set_empty()
    if pos[0] == 6:
        pos[0] = 0
    else:
        pos[0] += 1
    cells[pos[0]][pos[1]].set_player()
    crystal_collision(points)
    enemy_collision()

def move_enemy(enemies):
    for enemy in enemies:
        direction = random.randint(0, 3)
        cells[enemy[0]][enemy[1]].set_empty()
        if direction == 0: #left
            if enemy[1] == 0:
                enemy[1] = 6
            else:
                enemy[1] -= 1
        elif direction == 1: #right
            if enemy[1] == 6:
                enemy[1] = 0
            else:
                enemy[1] += 1
        elif direction == 2: #up
            if enemy[0] == 0:
                enemy[0] = 6
            else:
                enemy[0] -= 1
        elif direction == 3: #down
            if enemy[0] == 6:
                enemy[0] = 0 
            else:
                enemy[0] += 1   
        cells[enemy[0]][enemy[1]].set_enemy()

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

    for row in range(7):
        cells.append([])
        for col in range(7):
            cell = square(root, row, col)
            if row==col==3:
                 cell.set_player()
            elif (row == 0 and col == 0) or (row == 0 and col == 6) or (row == 6 and col == 3):
                cell.set_enemy()
            elif (row == 0 and col ==3):
                cell.set_crystal()
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