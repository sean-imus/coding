import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Zahl erraten")
        self.root.geometry("300x200")
        
        self.random_num = random.randint(0, 100)
        
        self.label = tk.Label(root, text="Wähle eine Zahl zwischen 0 und 100:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.check_guess)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
        
        self.button = tk.Button(root, text="Überprüfen", command=self.check_guess)
        self.button.pack(pady=5)
        
        self.new_game_button = tk.Button(root, text="Neues Spiel", command=self.new_game)
        self.new_game_button.pack(pady=5)
        self.new_game_button.pack_forget()
    
    def check_guess(self, event=None):
        try:
            num = int(self.entry.get())
            if num > self.random_num:
                self.result_label.config(text="Zu hoch, versuche es erneut!", fg="red")
            elif num == self.random_num:
                self.result_label.config(text="Genau richtig!", fg="green")
                messagebox.showinfo("Gewonnen!", f"Du hast die Zahl {self.random_num} erraten!")
                self.button.pack_forget()
                self.new_game_button.pack(pady=5)
            else:
                self.result_label.config(text="Zu niedrig, versuche es erneut!", fg="red")
        except ValueError:
            self.result_label.config(text="Bitte eine gültige Zahl eingeben!", fg="red")
    
    def new_game(self):
        self.random_num = random.randint(0, 100)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.new_game_button.pack_forget()
        self.button.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()
