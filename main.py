"""
This is the main file for running the video opening gui.

author: Adrian Salihi
date: 30th January 2024
"""
import tkinter as tk

def key_press(event):
    key = event.char
    print(key, 'is pressed')

def eye_opening():
    print("eye_opening!")

def open_new_window(window):
    new_window = tk.Toplevel(window)
    new_window.title("new")
    close_all = tk.Button(new_window, text="click_me_to_close", command=root.destroy).pack()

root = tk.Tk()
root.geometry('200x200')
eye_opening = tk.Button(root, text="eye_opening", command=lambda : open_new_window(root)).pack()

root.mainloop()