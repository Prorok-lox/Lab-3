# import tkinter as tk
# from tkinter import messagebox
# from sqrEq import sqrEquation


# def close():
#     window.destroy()


# def calc():
#     A = float(arg_A.get())
#     B = float(arg_B.get())
#     C = float(arg_C.get())
#     if A == 0.0:
#         tk.messagebox.showwarning('Error', 'Division by zero!')
#     else:
#         lbl_result.configure(text=sqrEquation(A, B, C))


# window = tk.Tk()
# window.geometry('576x360')
# bg_img = tk.PhotoImage(file='bg_pic.png')

# lbl_bg = tk.Label(window, image=bg_img)
# lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

# frame = tk.Frame(window)
# frame.place(relx=0.5, rely=0.5, anchor='center')

# lbl_A = tk.Label(frame, text='A', font=('Arial', 30), bg='blue', fg='white')
# lbl_A.grid(column=0, row=0, padx=10, pady=15)
# arg_A = tk.Entry(frame, width=10)
# arg_A.insert(0, '1')
# arg_A.grid(column=0, row=1, padx=10, pady=15)

# lbl_B = tk.Label(frame, text='B', font=('Arial', 30))
# lbl_B.grid(column=1, row=0, padx=10, pady=15)
# arg_B = tk.Entry(frame, width=10)
# arg_B.insert(0, '0')
# arg_B.grid(column=1, row=1, padx=10, pady=15)

# lbl_C = tk.Label(frame, text='C', font=('Arial', 30))
# lbl_C.grid(column=2, row=0, padx=10, pady=15)
# arg_C = tk.Entry(frame, width=10)
# arg_C.insert(0, '0')
# arg_C.grid(column=2, row=1, padx=10, pady=15)

# lbl_roots = tk.Label(frame, text='Result:')
# lbl_roots.grid(column=1, row=2)
# lbl_result = tk.Label(frame, text='None yet.', font=('Arial', 10))
# lbl_result.grid(column=2, row=2)

# btn_calc = tk.Button(frame, text='Calculate', command=calc)
# btn_calc.grid(column=0, row=3, padx=10, pady=15)
# btn_exit = tk.Button(frame, text='Cancel', command=close)
# btn_exit.grid(column=2, row=3, padx=10, pady=15)


# window.mainloop()


# import tkinter as tk
# from tkinter import messagebox

# # Функция генерации ключа
# def generate_key(serial_part):
#     try:
#         dec_value = int(serial_part, 16)
#         key_part_1 = dec_value // 1000
#         key_part_2 = (dec_value % 1000) % 100
#         key_part_3 = (dec_value % 100) % 10
#         return f'{key_part_1:03d}-{key_part_2:03d}-{key_part_3:03d}'
#     except ValueError:
#         return 'Invalid HEX input'

# # Функция для обработки события кнопки "Generate"
# def generate_key_action():
#     serial_part = entry_serial.get()
#     generated_key = generate_key(serial_part)
#     label_result.config(text=generated_key)

# # Создание главного окна
# window = tk.Tk()
# window.title("Snake Game Keygen")
# window.geometry('500x300')

# # Загрузка изображения для фона
# bg_img = tk.PhotoImage(file='snake_bg.png')

# # Метка для фона
# label_bg = tk.Label(window, image=bg_img)
# label_bg.place(x=0, y=0, relwidth=1, relheight=1)

# # Рамка для элементов интерфейса
# frame = tk.Frame(window, bg='white', bd=5)
# frame.place(relx=0.5, rely=0.5, anchor='center')

# # Метка с инструкциями
# label_instructions = tk.Label(frame, text='Enter HEX Serial Part (5 digits):', font=('Arial', 12), bg='white')
# label_instructions.grid(row=0, column=0, columnspan=2, pady=10)

# # Поле ввода для серийной части ключа
# entry_serial = tk.Entry(frame, width=10)
# entry_serial.grid(row=1, column=0, pady=10)

# # Кнопка для генерации ключа
# btn_generate = tk.Button(frame, text='Generate', command=generate_key_action)
# btn_generate.grid(row=1, column=1, pady=10)

# # Метка для отображения сгенерированного ключа
# label_result = tk.Label(frame, text='', font=('Arial', 12), bg='white')
# label_result.grid(row=2, column=0, columnspan=2, pady=10)

# # Запуск основного цикла
# window.mainloop()



import tkinter as tk
from tkinter import messagebox
import pygame
from PIL import Image, ImageTk

def generate_key(serial_part):
    try:
        dec_value = int(serial_part, 16)
        key_part_1 = dec_value // 1000
        key_part_2 = (dec_value % 1000) % 100
        key_part_3 = (dec_value % 100) % 10
        return f'{key_part_1:03d}-{key_part_2:03d}-{key_part_3:03d}'
    except ValueError:
        return 'Invalid HEX input'

def generate_key_action():
    serial_part = entry_serial.get()
    generated_key = generate_key(serial_part)
    label_result.config(text=generated_key)

def play_music():
    pygame.mixer.music.load("8bit_music.mp3")
    pygame.mixer.music.play(-1)

def animate_bg():
    global bg_img_animation
    next_bg = next(bg_img_animation)
    label_bg.configure(image=next_bg)
    label_bg.image = next_bg
    window.after(50, animate_bg)

# Открываем изображение с использованием Pillow
image_path = 'frame1.jpg'
img_pil = Image.open(image_path)

# Преобразуем изображение в PhotoImage
bg_img = ImageTk.PhotoImage(img_pil)

window = tk.Tk()
window.title("Snake Game Keygen")
window.geometry('500x300')

label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window, bg='white', bd=5)
frame.place(relx=0.5, rely=0.5, anchor='center')

label_instructions = tk.Label(frame, text='Enter HEX Serial Part (5 digits):', font=('Arial', 12), bg='white')
label_instructions.grid(row=0, column=0, columnspan=2, pady=10)

entry_serial = tk.Entry(frame, width=10)
entry_serial.grid(row=1, column=0, pady=10)

btn_generate = tk.Button(frame, text='Generate', command=generate_key_action)
btn_generate.grid(row=1, column=1, pady=10)

label_result = tk.Label(frame, text='', font=('Arial', 12), bg='white')
label_result.grid(row=2, column=0, columnspan=2, pady=10)

btn_music = tk.Button(frame, text='Play Music', command=play_music)
btn_music.grid(row=3, column=0, columnspan=2, pady=10)

pygame.mixer.init()
play_music()
bg_img_animation = cycle([ImageTk.PhotoImage(Image.open(f'snake_animation/frame{i}.png')) for i in range(1, 11)])
animate_bg()

window.mainloop()

