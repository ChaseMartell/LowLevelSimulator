from view import View
import tkinter as tk

"""William Martell,Tanner Erekson, Derrek Buttars, Matthew Palmer.
    This is a simulator project that we had to create for our Software Engineering course from scratch.
    When running the program, the help button contains a lot of the information on how to properly run the simulator."""


def main():
    """Initiates program and GUI to begin running"""

    memory = ["+0000"] * 100
    accumulator = 0
    instruction_counter = 0
    instruction_register = ""
    operation_code = 0
    operand = 0

    big_storage = [0] * 100

    window = tk.Tk()
    window.title("BasicML Low-Level Simulator.")
    window.geometry("1000x600")
    v = View(
        window,
        memory,
        instruction_counter,
        instruction_register,
        operation_code,
        operand,
        accumulator,
        big_storage,
    )

    window.mainloop()


if __name__ == "__main__":
    main()