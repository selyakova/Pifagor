import tkinter as tk
def calculate():
    birthday = entry.get()
    day_month_sum = sum(int(digit) for digit in birthday[:5] if digit.isdigit())
    year_sum = sum(int(digit) for digit in birthday[6:] if digit.isdigit())
    step_3 = day_month_sum + year_sum
    step_4 = sum(int(digit) for digit in str(step_3))
    step_5 = step_3 - (2 * int(birthday[0]))
    step_6 = sum(int(digit) for digit in str(step_5))
    row_1 = birthday.replace(".", "")
    row_2 = str(step_3) + str(step_4) + str(step_5) + str(step_6)
    digits_counts = [0] * 10
    for digit in row_1 + row_2:
        digits_counts[int(digit)] += 1
    row1_label.config(text="Первый ряд чисел: " + row_1)
    row2_label.config(text="Второй ряд чисел: " + row_2)
    table.delete("1.0", "end")
    for i in range(10):
        row = ""
        for j in range(digits_counts[i]):
            row += str(i)
        table.insert("end", row + "\n")

root = tk.Tk()
root.title("Praktiline töö Numeroloogia Pythagorase ruut")
#canvas = tk.Canvas(root, bg="#bcebc8")
#canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

entry_label = tk.Label(root, text="Введите дату рождения в формате DD.MM.YYYY:",bg="#ace8e3",font=("Arial", 20))
entry_label.grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

button = tk.Button(root, text="Вычислить", command=calculate, bg="#ace8e3",font=("Arial", 20))
button.grid(row=1, column=0, padx=5, pady=5)

row1_label = tk.Label(root, text="",font=("Arial", 20))
row1_label.grid(row=2, column=0, padx=5, pady=5)
row2_label = tk.Label(root, text="",font=("Arial", 20))
row2_label.grid(row=3, column=0, padx=5, pady=5)

table_label = tk.Label(root, text="Подсчитав, сколько каких цифр в обоих рядах составляем таблицу:",bg="#ace8e3",font=("Arial", 20))
table_label.grid(row=4, column=0, padx=5, pady=5)
table = tk.Text(root, height=10)
table.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()



