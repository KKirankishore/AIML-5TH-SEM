import tkinter as tk
from tkinter import messagebox

class MultiStepForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Step Form")
        self.geometry("300x400")
        self.current_section = 0

        self.sections = [
            self.create_section1,
            self.create_section2,
            self.create_section3
        ]
        self.create_section1()

    def create_section1(self):
        self.clear_frame()

        tk.Label(self, text="Account Creation").pack(pady=10)

        tk.Label(self, text="First Name").pack()
        self.fname_entry = tk.Entry(self)
        self.fname_entry.pack()

        tk.Label(self, text="Last Name").pack()
        self.lname_entry = tk.Entry(self)
        self.lname_entry.pack()

        tk.Label(self, text="DOB").pack()
        self.dob_entry = tk.Entry(self)
        self.dob_entry.pack()

        tk.Label(self, text="Mobile Number").pack()
        self.mob_entry = tk.Entry(self)
        self.mob_entry.pack()

        tk.Button(self, text="Next", command=self.next_section).pack(pady=20)

    def create_section2(self):
        self.clear_frame()

        tk.Label(self, text="Verification").pack(pady=10)

        tk.Label(self, text="Email").pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        tk.Label(self, text="Enter 6 digit OTP").pack()
        self.email_otp_entry = tk.Entry(self)
        self.email_otp_entry.pack()

        tk.Label(self, text="Phone").pack()
        self.phone_otp_entry = tk.Entry(self)
        self.phone_otp_entry.pack()

        tk.Button(self, text="Next", command=self.next_section).pack(pady=20)

    def create_section3(self):
        self.clear_frame()

        tk.Label(self, text="Captcha Verification").pack(pady=10)

        tk.Label(self, text="Captcha").pack()
        tk.Label(self, text="Kem21").pack()

        tk.Label(self, text="Enter the above captcha").pack()
        self.captcha_entry = tk.Entry(self)
        self.captcha_entry.pack()

        tk.Button(self, text="Finish", command=self.finish).pack(pady=20)

    def next_section(self):
        self.current_section += 1
        if self.current_section < len(self.sections):
            self.sections[self.current_section]()
        else:
            self.finish()

    def finish(self):
        messagebox.showinfo("Info", "Form Submitted Successfully!")
        self.destroy()

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MultiStepForm()
    app.mainloop()
