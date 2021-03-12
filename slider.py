# slider implementation

import tkinter as tk
import tkinter.ttk as ttk

def callback(event):
    pass



class Slider(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.geometry('400x40')
        self.pack(expand=1, fill='both')
        self.columnconfigure(2, weight=99)

        self.label = tk.Label(self, text='Value')
        self.label.grid(row=1, column=1, padx=(10, 0), pady=10)
        self.label.config(width=10)
        self.scaleVar = tk.IntVar()
        self._scale = ttk.Scale(self, from_=50, to=75, variable=self.scaleVar)
        self._scale.grid(row=1, column=2, padx=(5, 5), sticky='nsew')
        self._scale.config(command=self._callback)

    def _callback(self, event):
        v = self.scaleVar.get()
        self.label.config(text=v)


if __name__ == '__main__':
    root = tk.Tk()
    slider = Slider(root)
    root.mainloop()
