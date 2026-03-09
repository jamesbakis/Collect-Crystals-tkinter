import tkinter as tk

class square:
    def __init__(self, root, row, col):
        self.root = root
        self.row = row
        self.col = col
        self.empty = tk.PhotoImage(file="game_square.png")
        self.enemy = tk.PhotoImage(file="enemy_square.png")
        self.player = tk.PhotoImage(file="player_square.png")
        self.crystal = tk.PhotoImage(file="crystal_square.png")
        self.label = tk.Label(root, image=self.empty, borderwidth=0)
        self.label.grid(row=self.row, column=self.col)
        
    
    def set_empty(self):
        self.label.config(image=self.empty)

    def set_enemy(self):
        self.label.config(image=self.enemy)

    def set_player(self):
        self.label.config(image=self.player)
    
    def set_crystal(self):
        print("set crystal")
        self.label.config(image=self.crystal)