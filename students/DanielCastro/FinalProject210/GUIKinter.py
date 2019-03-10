import tkinter as tk


class App:
    def __init__(self, App_root):
        frame = tk.Frame(App_root)
        frame.pack()

        self.btn_prt_to_con = tk.Button(frame
                                        , text="print to console"
                                        , fg="blue"
                                        , command=self.print_to_con)  # No ()!
        self.btn_prt_to_con.pack(side=tk.LEFT)

        self.btn_quit = tk.Button(frame, text="Quit", fg="red", command=frame.quit)  # No ()!
        self.btn_quit.pack(side=tk.LEFT)

    def print_to_con(self):
        print("Test Message")


root = tk.Tk()  # Create a root node
app = App(root)  # Attach an App object to the note
root.mainloop()  # Start the UI looping (refreshing) until "quit" is called.
app.print_to_con()
