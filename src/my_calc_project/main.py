import tkinter as tk

from my_calc_project.GUI import Gui


def main():
    window = tk.Tk()
    app = Gui(window)
    window.mainloop()

if __name__ == "__main__":
    main()
