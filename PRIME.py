import tkinter as tk
from tkinter import messagebox

# Sprawdza, czy liczba jest pierwsza
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Funkcja sprawdzająca liczbę
def check_prime(event=None):
    try:
        num = int(entry.get())
        if is_prime(num):
            result_label.config(text=f"{num} jest liczbą pierwszą!!!", fg="green", wraplength=600)
        else:
            result_label.config(text=f"{num} nie jest liczbą pierwszą.", fg="red", wraplength=600)
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawną liczbę całkowitą.")

# Funkcja zamykająca program
def quit_program():
    root.quit()

# Funkcja walidująca wprowadzaną liczbę
def validate_input(new_value):
    if new_value.isdigit() and len(new_value) <= 50:
        return True
    elif new_value == "":  # Pozwól na puste pole
        return True
    else:
        return False

# Okno główne
root = tk.Tk()
root.title("PRIME-Checker by DebugDuck")
root.geometry("650x300")

font_large = ("Arial", 16)
root.resizable(False, False)

# Etykieta instrukcji
instruction_label = tk.Label(root, text="Wprowadź liczbę:", font=font_large)
instruction_label.pack(pady=10)

# Walidator długości liczby
vcmd = (root.register(validate_input), '%P')

# Pole wejścia
entry = tk.Entry(root, font=font_large, width=30, validate="key", validatecommand=vcmd)
entry.pack(pady=10)

# Obsługa Enter
entry.bind("<Return>", check_prime)

# Etykieta wyniku
result_label = tk.Label(root, text="", font=font_large)
result_label.pack(pady=20)

# Przycisk sprawdzania
check_button = tk.Button(root, text="Sprawdź", font=font_large, width=15, command=check_prime)
check_button.pack(pady=10)

# Przycisk zakończenia
quit_button = tk.Button(root, text="Zakończ", font=font_large, width=15, command=quit_program)
quit_button.pack(pady=10)

root.mainloop()

