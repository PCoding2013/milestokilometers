#Import these using PIP
import tkinter as tk
import ttkbootstrap as ttk
# You can make these variables become anything
def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

window = ttk.Window(themename='darkly')
window.title('Demo')
window.geometry('300x150')

title_label = ttk.Label(window, text="Miles to kilometers", font='Calibri 24 bold')
title_label.pack()

input_frame = ttk.Frame(window)
entry_int = tk.IntVar()
entry = ttk.Entry(input_frame, textvariable = entry_int)
button = ttk.Button(input_frame, text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

output_string = tk.StringVar()
output_label = ttk.Label(window, text='Output', font='Calibri 24', textvariable=output_string)
output_label.pack(pady=5)

window.mainloop()
