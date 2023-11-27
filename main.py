import tkinter as tk
from tkinter import messagebox
import pygame
from PIL import Image, ImageTk
from itertools import cycle

def generate_key(serial_part):
    try:
        dec_value = int(serial_part, 16)
        key_part_1 = dec_value // 100000
        key_part_2 = (dec_value % 100000) % 10000
        key_part_3 = (dec_value % 10000) % 1000
        key_part_4 = (dec_value % 1000) % 100
        key_part_5 = (dec_value % 100) % 10
        return f'{key_part_1:05d}-{key_part_2:05d}-{key_part_3:05d}'
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
    window.after(3000, animate_bg)


window = tk.Tk()
window.title("Forza Game Key")
window.geometry('500x300')

# Открываем изображение с использованием Pillow
image_path = r"C:\Users\il_vl\OneDrive\Рабочий стол\ITMO\Питон\Lab-3\Forza_animation\frame1.jpg"
img_pil = Image.open(image_path)

# Преобразуем изображение в PhotoImage
bg_img = ImageTk.PhotoImage(img_pil)

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
bg_img_animation = cycle([ImageTk.PhotoImage(Image.open(f'Forza_animation/frame{i}.jpg')) for i in range(1, 11)])
animate_bg()

window.mainloop()

