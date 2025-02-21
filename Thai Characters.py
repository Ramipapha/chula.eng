import tkinter as tk
import random

# List of Thai consonants with their names
thai_consonants = [
    ("ก", "Gor Gai (กอ ไก่)"),
    ("\u0E02", "Khor Khai (ขอ ไข่)"),
    ("\u0E04", "Kor Khuat (คอ ขวาด)"),
    ("\u0E06", "Khor Rakhang (ฆอ ระคัง)"),
    ("\u0E08", "Jor Jaan (จอ จาน)"),
    ("\u0E0A", "Chor Chang (ชอ ช้าง)")
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)
        
        self.label = tk.Label(self.frame, text="", font=("Arial", 60))
        self.label.pack()
        
        self.flip_label = tk.Label(self.frame, text="", font=("Arial", 20))
        self.flip_label.pack()
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()
        
        self.next_button = tk.Button(self.button_frame, text="Next", command=self.next_card)
        self.next_button.grid(row=0, column=0, padx=10)
        
        self.flip_button = tk.Button(self.button_frame, text="Flip", command=self.flip_card)
        self.flip_button.grid(row=0, column=1, padx=10)
        
        self.current_card = None
        self.next_card()
    
    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.label.config(text=self.current_card[0])
        self.flip_label.config(text="")
    
    def flip_card(self):
        if self.current_card:
            self.flip_label.config(text=self.current_card[1])

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
