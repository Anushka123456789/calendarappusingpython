import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import Calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Calendar App")
        self.root.geometry("600x400")

        self.current_date = datetime.now().date()

        self.create_widgets()

    def create_widgets(self):
        # Calendar
        self.calendar = Calendar(self.root, selectmode="day", date_pattern="yyyy-mm-dd")
        self.calendar.pack(pady=20)

        # Event Entry
        self.event_entry = tk.Entry(self.root, width=30)
        self.event_entry.pack(pady=10)

        # Add Event Button
        add_event_btn = tk.Button(self.root, text="Add Event", command=self.add_event)
        add_event_btn.pack()

    def add_event(self):
        selected_date = self.calendar.get_date()
        event_description = self.event_entry.get()

        if not event_description:
            messagebox.showwarning("Warning", "Please enter event details.")
            return

        messagebox.showinfo("Event Added", f"Event on {selected_date}: {event_description}")

        # You can save the events to a file or a database here.
        # For simplicity, we are just displaying a message box.

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
