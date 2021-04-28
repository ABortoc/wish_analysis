import tkinter as tk
import data_process as dp
import image_grab as ig
import clean_up as clean
import threading


def start_thread():
    t1 = threading.Thread(target=ig.clipboard_listen)
    t1.start()


window = tk.Tk()

btn_listen = tk.Button(
    text='Listen',
    width=15,
    height=5,
    bg='grey',
    fg='white',
    command=start_thread
)
btn_listen.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

btn_process = tk.Button(
    text='Process',
    width=15,
    height=5,
    bg='grey',
    fg='white',
    command=dp.wish_data_process
)
btn_process.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

btn_graph_four = tk.Button(
    text='4 Stars',
    width=15,
    height=5,
    bg='grey',
    fg='white',
    command=dp.bar_graph_four_create
)
btn_graph_four.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

btn_graph_five = tk.Button(
    text='5 Stars',
    width=15,
    height=5,
    bg='grey',
    fg='white',
    command=dp.bar_graph_five_create
)
btn_graph_five.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

btn_clean = tk.Button(
    text='Clean Up',
    width=15,
    height=5,
    bg='grey',
    fg='white',
    command=clean.screenshot_cleaning
)
btn_clean.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()
