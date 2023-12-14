import tkinter as tk
from tkinter import messagebox
from queue import Queue

class QueueMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Queueing Machine")
        self.root.geometry("600x600")
        self.root.configure(bg="#FFF3E7")

        self.queue = Queue()
        self.used_tickets = set()
        self.ticket_counter = 0
        self.current_ticket = tk.StringVar(value="No ticket yet")
        self.queue_display = tk.StringVar(value="Preparing Ticket: No tickets yet\nQueue: Empty")

        self.label_info = tk.Label(root, text="Welcome to our Food Stall", font=("Comic Sans MS", 20), bg="#FFF3E7",fg="#79503E")
        self.label_instruction = tk.Label(root, text="Take a ticket and enjoy your meal", font=("Comic Sans MS", 14),bg="#FFF3E7", fg="#79503E")
        self.frame_current_ticket = tk.Frame(root, bg="#FFF3E7")
        self.label_current_ticket_text = tk.Label(self.frame_current_ticket, text="Current Ticket:", font=("Comic Sans MS", 14), bg="#FFF3E7",fg="#79503E")
        self.label_current_ticket = tk.Label(self.frame_current_ticket, textvariable=self.current_ticket,font=("Comic Sans MS", 30), bg="#FFF3E7", fg="#644C41")
        self.label_queue_display = tk.Label(root, textvariable=self.queue_display, font=("Comic Sans MS", 12),bg="#FFF3E7", fg="#79503E")
        self.button_take_ticket = tk.Button(root, text="Take Ticket", command=self.take_ticket,font=("Comic Sans MS", 12), bg="#FFBEA3", fg="#8D6655",
                                            bd=0, relief=tk.FLAT, padx=20, pady=10, borderwidth=1,highlightthickness=0, highlightbackground="#B6D8E6")
        self.button_dequeue = tk.Button(root, text="Dequeue", command=self.dequeue, font=("Comic Sans MS", 12),bg="#FFE784", fg="#8D6655",
                                        bd=0, relief=tk.FLAT, padx=20, pady=10, borderwidth=1,highlightthickness=0, highlightbackground="#B6D8E6")
        self.button_clear_queue = tk.Button(root, text="Clear Queue", command=self.clear_queue,
                                            font=("Comic Sans MS", 12), bg="#AFBBEF", fg="#8D6655",
                                            bd=0, relief=tk.FLAT, padx=20, pady=10, borderwidth=1,
                                            highlightthickness=0, highlightbackground="#B6D8E6")


        self.label_info.pack(padx=10, pady=10)
        self.label_instruction.pack(pady=2)
        self.frame_current_ticket.pack(pady=20)
        self.label_current_ticket_text.pack(side="top")
        self.label_current_ticket.pack(pady=5)
        self.label_queue_display.pack(pady=10)
        self.button_take_ticket.pack(pady=5)
        self.button_dequeue.pack(pady=5)
        self.button_clear_queue.pack(pady=5)

    def take_ticket(self):
        self.ticket_counter += 1

        ticket_number = self.ticket_counter
        self.queue.put(ticket_number)
        self.used_tickets.add(ticket_number)
        self.current_ticket.set(f"{ticket_number}")
        self.update_queue_display()

    def dequeue(self):
        if not self.queue.empty():
            completed_ticket = self.queue.get()
            self.used_tickets.remove(completed_ticket)
            self.update_queue_display()
        else:
            messagebox.showinfo("Queue Empty", "The queue is already empty.")

    def clear_queue(self):
        self.queue = Queue()
        self.used_tickets = set()
        self.ticket_counter = 0  # Reset the ticket counter
        self.current_ticket.set("No ticket yet")
        self.update_queue_display()

    def update_queue_display(self):
        if not self.queue.empty():
            queue_list = list(self.queue.queue)
            preparing_ticket = queue_list[0] if queue_list else "No tickets yet"
            self.queue_display.set(f"Preparing Ticket: {preparing_ticket}\nQueue: {', '.join(map(str, queue_list))}")
        else:
            self.queue_display.set("Preparing Ticket: No tickets yet\nQueue: Empty")

if __name__ == "__main__":
    root = tk.Tk()
    app = QueueMachine(root)
    root.mainloop()