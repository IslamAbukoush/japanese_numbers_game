from random import randint
numbers = {
    0: ["rei", "maru", "zero"],
    1: ["ichi"],
    2: ["ni"],
    3: ["san"],
    4: ["shi", "yon"],
    5: ["go"],
    6: ["roku"],
    7: ["shichi", "nana"],
    8: ["hachi"],
    9: ["ku", "kyuu"],
    10: ["juu"],
    100: ["hyaku", "byaku"],
    600: ["roppyaku"],
    800: ["happyaku"],
    1000: ["sen", "issen", "zen"],
    8000: ["hassen"],
}
zeros = ["rei", "maru", "zero"]
nums = ["ichi","ni","san","shi", "yon","go","roku","shichi", "nana","hachi","ku","kyuu"]
nums_for_tens = ["ni","san","yon","go","roku","nana","hachi","kyuu"]
nums_for_hundreds = ["_","_","ni","san","yon","go","nana","kyuu"]
nums_for_thausands = ["ni","san","yon","go","roku","nana","kyuu"]

def index_exists(index, listo):
    try:
        listo[index]
    except:
        return False
    return True

def word_to_number(word):
    for key in numbers:
            if word in numbers[key]:
                return key
    return "No such number"

def ones_place(words):
    if len(words) == 0:
        return "No words have been provided"
    else:
        if words[-1] in zeros:
            if len(words) == 1:
                return 0
            else:
                return "A number can't have zero inside"
        elif words[-1] in nums:
            ones_result = word_to_number(words[-1])
            if isinstance(ones_result, str):
                return ones_result
            tens_result = tens_place(words[:-1])
            if isinstance(tens_result, str):
                return tens_result 
            return ones_result + tens_result
        else:
            tens_result = tens_place(words)
            if isinstance(tens_result, str):
                return tens_result
            return tens_place(words)

def tens_place(words):
    if len(words) == 0:
        return 0
    else:
        if words[-1] == "juu":
            if index_exists(-2, words):
                if words[-2] in nums_for_tens:
                    tens_result = word_to_number(words[-2])
                    if isinstance(tens_result, str):
                        return tens_result
                    hundreds_result = hundreds_place(words[:-2])
                    if isinstance(hundreds_result, str):
                        return hundreds_result
                    return 10*tens_result + hundreds_result
                elif words[-2] in ["shi", "shichi", "ku"]:
                    return "You cant have " + words[-2] + " before juu"
                else:
                    hundreds_result = hundreds_place(words[:-1])
                    if isinstance(hundreds_result, str):
                        return hundreds_result
                    return 10 + hundreds_result
            else:
                return 10
        else:
            return hundreds_place(words)

def hundreds_place(words):
    if len(words) == 0:
        return 0
    else:
        if words[-1] == "hyaku":
            if index_exists(-2, words):
                if words[-2] in nums_for_hundreds:
                    if words[-2] == "san":
                        return "'san' should be followed by byaku and not hyaku..."
                    hundreds_result = word_to_number(words[-2])
                    if isinstance(hundreds_result, str):
                        return hundreds_result
                    thausands_result = thausands_place(words[:-2])
                    if isinstance(thausands_result, str):
                        return thausands_result
                    return 100*hundreds_result + thausands_result
                else:
                    thausands_result = thausands_place(words[:-1])
                    if isinstance(thausands_result, str):
                        return thausands_result
                    return 100 +  thausands_result
            else:
                return 100
        elif words[-1] == "byaku":
            if index_exists(-2, words) and words[-2] == "san":
                thausands_result = thausands_place(words[:-2])
                if isinstance(thausands_result, str):
                        return thausands_result
                return 300 + thausands_result
            else:
                return "Byaku gotta have 'san' before it..."
        elif words[-1] == "sanbyaku":
            thausands_result = thausands_place(words[:-1])
            if isinstance(thausands_result, str):
                return thausands_result
            return 300 + thausands_result
        elif words[-1] == "roppyaku":
            thausands_result = thausands_place(words[:-1])
            if isinstance(thausands_result, str):
                return thausands_result
            return 600 + thausands_result
        elif words[-1] == "happyaku":
            thausands_result = thausands_place(words[:-1])
            if isinstance(thausands_result, str):
                return thausands_result
            return 800 + thausands_result
        else:
            return thausands_place(words)

def thausands_place(words):
    if len(words) == 0:
        return 0
    elif len(words) == 1:
        if words[0] in ["issen", "sen"]:
            return 1000
        elif words[0] == "hassen":
            return 8000
        else:
            return "Invalid input..."
    elif len(words) == 2:
        if words[-1] == "sen":
            if words[-2] in nums_for_thausands:
                if words[-2] == "san":
                    return "'san' should be followed by zen and not sen..."
                num_res = word_to_number(words[-2])
                if isinstance(num_res, str):
                    return num_res
                return 1000*num_res
            else:
                return "'" + words[-2] + " sen' is not a correct number."
        elif words[-1] == "zen":
            if words[-2] == "san":
                return 3000
            else:
                return "Zen gotta have 'san' before it..."
        else:
            return "Invalid input..."
    else:
        return "invalid input...."

def text_to_number(text):
    words = text.strip().split()
    words = [x.lower() for x in words]
    return ones_place(words)

def number_to_text(num):
    ones_dict = {
        0: ["rei", "maru", "zero"],
        1: ["ichi"],
        2: ["ni"],
        3: ["san"],
        4: ["shi", "yon"],
        5: ["go"],
        6: ["roku"],
        7: ["shichi", "nana"],
        8: ["hachi"],
        9: ["ku", "kyuu"],
    }
    tens_dict = {
        0: "",
        1: "juu",
        2: "ni juu",
        3: "san juu",
        4: "yon juu",
        5: "go juu",
        6: "roku juu",
        7: "nana juu",
        8: "hachi juu",
        9: "kyuu juu",
    }
    hunds_dict = {
        0: "",
        1: "hyaku",
        2: "ni hyaku",
        3: "san byaku",
        4: "yon hyaku",
        5: "go hyaku",
        6: "roppyaku",
        7: "nana hyaku",
        8: "happyaku",
        9: "kyuu hyaku",
    }
    thaus_dict = {
        0: [""],
        1: ["sen", "issen"],
        2: ["ni sen"],
        3: ["san zen"],
        4: ["yon sen"],
        5: ["go sen"],
        6: ["roku sen"],
        7: ["nana sen"],
        8: ["hassen"],
        9: ["kyuu sen"],
    }
    if num < 0 or num > 9999:
        return "The given number is outside the supported range"
    digits = list(str(num))
    leng = len(digits)
    if leng == 1 and digits[0] == 0:
        return ones_dict[0]
    ones = ones_dict[int(digits[-1])]
    tens = ""
    hunds = ""
    thaus = []
    if leng > 1:
        tens = tens_dict[int(digits[-2])]
    if leng > 2:
        hunds = hunds_dict[int(digits[-3])]
    if leng > 3:
        thaus = thaus_dict[int(digits[-4])]

    result = []
    for one in ones:
        for thau in thaus:
            raw = (thau + " " + hunds + " " + tens + " " + one).strip()
            raw = " ".join(raw.split())
            result.append(raw)
    return result
    
        




import tkinter as tk
from tkinter import messagebox
import random

class RandomNumberGame:
    def __init__(self, master):
        self.master = master
        master.title("Random Number Game")

        # Set window size
        master.geometry("500x450")

        # Allow widgets to grow and shrink with the window
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
        master.grid_columnconfigure(0, weight=1)

        self.score = 0
        self.random_number = self.generate_random_number()

        self.label = tk.Label(master, text=f"Enter the number: {self.random_number}", font=("Helvetica", 30))
        self.label.grid(row=0, column=0, pady=10, sticky="nsew")

        self.entry = tk.Entry(master, font=("Helvetica", 30), justify="center")
        self.entry.grid(row=1, column=0, pady=10, sticky="nsew")

        self.submit_button = tk.Button(master, text="Submit", command=self.check_input, font=("Helvetica", 25))
        self.submit_button.grid(row=2, column=0, pady=10, sticky="nsew")

        self.reveal_button = tk.Button(master, text="Reveal Answer", command=self.reveal_answer, font=("Helvetica", 25))
        self.reveal_button.grid(row=3, column=0, pady=10, sticky="nsew")

        # Bind the <Return> event to the check_input method
        self.master.bind('<Return>', lambda event=None: self.check_input())

        self.score_label = tk.Label(master, text=f"Score: {self.score}", font=("Helvetica", 20))
        self.score_label.grid(row=4, column=0, pady=10, sticky="nsew")

    def generate_random_number(self):
        choice = randint(1, 7)
        if 1 <= choice <= 1:
            return randint(0, 9)
        elif 2 <= choice <= 3:
            return randint(10, 99)
        elif 4 <= choice <= 5:
            return randint(100, 999)
        elif 6 <= choice <= 7:
            return randint(1000, 9999)

    def check_input(self):
        # Disable both the buttons and the <Return> event to prevent spamming
        self.submit_button.config(state=tk.DISABLED)
        self.reveal_button.config(state=tk.DISABLED)
        self.master.unbind('<Return>')

        user_input = self.entry.get()
        try:
            user_input = text_to_number(user_input)
            if user_input == self.random_number:
                self.label.config(text="Correct!")
                self.score += 1
                self.master.after(1500, self.reset_game)
            else:
                if isinstance(user_input, str):
                    messagebox.showinfo("Incorrect", user_input)
                else:
                    messagebox.showinfo("Incorrect", "Incorrect, try again...")
                # Re-enable the buttons and <Return> event for the next attempt
                self.submit_button.config(state=tk.NORMAL)
                self.reveal_button.config(state=tk.NORMAL)
                self.master.bind('<Return>', lambda event=None: self.check_input())
        except ValueError:
            messagebox.showinfo("Invalid Input", "Please enter a valid number.")
            # Re-enable the buttons and <Return> event for the next attempt
            self.submit_button.config(state=tk.NORMAL)
            self.reveal_button.config(state=tk.NORMAL)
            self.master.bind('<Return>', lambda event=None: self.check_input())

    def reset_game(self):
        self.random_number = self.generate_random_number()
        self.label.config(text=f"Enter the number: {self.random_number}")
        self.entry.delete(0, 'end')
        # Re-enable the buttons and <Return> event for the next attempt
        self.submit_button.config(state=tk.NORMAL)
        self.reveal_button.config(state=tk.NORMAL)
        self.master.bind('<Return>', lambda event=None: self.check_input())
        # Update the score label
        self.score_label.config(text=f"Score: {self.score}")

    def reveal_answer(self):
        result = "\n"
        answers = number_to_text(self.random_number)
        for answer in answers:
            result += answer + '\n'
        messagebox.showinfo("Reveal Answer", f"Possible answers are: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNumberGame(root)
    root.mainloop()
