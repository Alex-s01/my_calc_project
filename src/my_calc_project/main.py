from my_calc_project.GUI import Gui
import tkinter as tk


def main():
    window = tk.Tk()
    app = Gui(window)
    window.mainloop()

if __name__ == "__main__":
    main()
