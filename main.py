"""
This is the main file for running the video opening gui.

author: Adrian Salihi
date: 30th January 2024
"""
import tkinter as tk
import os
import supplemental_functions as sup

if __name__ == '__main__':
    os.chdir('/Users/adrianschmidt/repos/video_gui/videos')
    module_list = os.listdir()
    root = tk.Tk()

    for module in module_list:
        collection = tk.Button(root, text=module, command=lambda module=module : sup.module_window(root, module)).pack()

    os.chdir('/Users/adrianschmidt/repos/video_gui/videos')
    root.mainloop()
