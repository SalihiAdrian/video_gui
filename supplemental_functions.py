import tkinter as tk
import os

def module_window(window, module_name):
    new_window = tk.Toplevel(window)
    new_window.geometry("200x1000")
    new_window.title(module_name)
    os.chdir('/Users/adrianschmidt/repos/video_gui/videos/' + module_name)
    video_list = os.listdir()
    for video in video_list:
        close_all = tk.Button(new_window, text=video, command=lambda video=video : run_video(module_name, video)).pack()

def run_video(module_name, video):
    os.chdir('/Users/adrianschmidt/repos/video_gui/videos/' + module_name)
    os.system('open ' + video)

