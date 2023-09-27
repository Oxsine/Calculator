# Библиотеки
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys
import math

# создание окна, названия, иконки, размера
root = Tk()
root.title('бульбулятор')
root.geometry('352x286')
root.resizable(False, False)

# Список кнопок
btns_list = [
"1", "2", "3", "+", "*",
"4", "5", "6", "-", "/",
"7", "8", "9",  "=", "xⁿ",
"0", ".", "±",  "C",
"Exit", "π", "sin", "cos",
"(", ")","n!","√2"
]

# Построение сетки кнопок по списку
r = 1
c = 0
for i in btns_list:
    rel = ''
    cmd = lambda x = i: calc(x)
    ttk.Button(root, text = i, command= cmd, width = 10).grid(row = r, column = c, ipady = 10)
    c += 1
    if c > 4:
        c = 0
        r += 1

# создание ввода
calc_entry = Entry(root, width= 46)
calc_entry.grid(row = 0, column = 0, columnspan = 4, sticky = 'e')

# логика калькултора
def calc(key):
    if key == '=':
        # проверка написания цифр
        str1 = "-+0123456789.*/)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, 'Ошибка')
            messagebox.showerror('Error!', 'Вы не ввели значение')
        # вывод ошибки
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, '=' + str(result))
        except:
            calc_entry.insert(END, 'Error!')
            messagebox.showerror('Error!', 'Проверь ввод данных')
    elif key == 'C':
        calc_entry.delete(0, END)
    elif key == '±':
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == '-':
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, '-')
        except IndexError:
            pass
    elif key == 'π':
        calc_entry.insert(END, math.pi)
    elif key == 'Exit':
        root.after(1, root.destroy)
        sys.exit()
    elif key == 'xⁿ':
        calc_entry.insert(END, '**')
    elif key == 'sin':
        calc_entry.insert(END, '=' + str(math.sin(int(calc_entry.get()))))
    elif key == 'cos':
        calc_entry.insert(END, '=' + str(math.cos(int(calc_entry.get()))))
    elif key == '(':
        calc_entry.insert(END, '(')
    elif key == ')':
        calc_entry.insert(END, ')')
    elif key == 'n!':
        calc_entry.insert(END, '=' + str(math.factorial(int(calc_entry.get()))))
    else:
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

# обновление состояния окна
root.mainloop()