import random

choice = ["batu", "gunting", "kertas"]
comp = random.choice(choice)

while True:
    def func (n):
        user_choice = input("Masukkan pilihan anda (batu/gunting/kertas): ").lower()
        if user_choice in choice:
            if user_choice == comp:
                print(f"computer memilih: {comp}\ndan anda memilih: {user_choice}\nanda SERI!")
            elif (user_choice == "batu" and comp == "gunting") or \
                (user_choice == "gunting" and comp == "kertas") or \
                (user_choice == "kertas" and comp == "batu"):
                print(f"computer memilih: {comp}\ndan anda memilih: {user_choice}\nanda MENANG!")
            else:
                print(f"computer memilih: {comp}\ndan anda memilih: {user_choice}\nanda KALAH!")
        else:
            print("tidak ada di pilihan.")
            
    func(comp)