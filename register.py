from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

       # ========== variables ==============
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # =========== bg image ==========
        self.bg = ImageTk.PhotoImage(file=r"E:\Face\Images\Wallpapers\C.jpg")

        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # =========== left image =============
        self.bg1 = ImageTk.PhotoImage(
            file=r"E:\Face\Images\Wallpapers\agsvhvve4sx811.png")

        bg_lbl = Label(self.root, image=self.bg1)
        bg_lbl.place(x=50, y=100, width=410, height=480)

        # =========== main frame==========

        frame = Frame(self.root, bg="white")
        frame.place(x=440, y=100, width=800, height=480)

        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        # ============ Label and Entry =============

        # -------------- row1
        fname = Label(frame, text="First Name", font=(
            "times new roman", 12, "bold"), bg="white")
        fname.place(x=50, y=80)

        self.fname_entry = ttk.Entry(
            frame, textvariable=self.var_fname, font=("times new roman", 14, "bold"))
        self.fname_entry.place(x=50, y=110, width=250)

        l_name = Label(frame, text="Last Name", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=80)

        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", 12))
        self.txt_lname.place(x=370, y=110, width=250)

        # -------------- row2
        contact = Label(frame, text="Contact No", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        contact.place(x=50, y=150)

        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_contact, font=("times new roman", 12))
        self.txt_contact.place(x=50, y=180, width=250)

        email = Label(frame, text="Email", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        email.place(x=370, y=150)

        self.txt_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("times new roman", 12))
        self.txt_email.place(x=370, y=180, width=250)

        # ------------- row 3

        security_Q = Label(frame, text="Select Security Questions", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=220)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=(
            "times new roman", 12, "bold"), state="readonly")
        self.combo_security_Q["values"] = (
            "Select", "Your Birth Place", "Your Girlfreind Name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=250, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=220)

        self.txt_security = ttk.Entry(
            frame, textvariable=self.var_securityA, font=("times new roman", 12))
        self.txt_security.place(x=370, y=250, width=250)

        # ---------------- row 4
        pswd = Label(frame, text="Password", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=290)

        self.txt_pswd = ttk.Entry(
            frame, textvariable=self.var_pass, font=("times new roman", 12))
        self.txt_pswd.place(x=50, y=320, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=(
            "times new roman", 12, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=290)

        self.txt_confirm_pswd = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("times new roman", 12))
        self.txt_confirm_pswd.place(x=370, y=320, width=250)

        # ========= Check Button ==============
        self.var_check = IntVar()
        self.checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=(
            "times new roman", 10, "bold"), onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=360)

        # ============= Button ================
        img = Image.open(r"E:\Face\Images\bnnnh.jpg")
        img = img.resize((200, 50), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2", font=(
            "times new roman", 12, "bold"))
        b1.place(x=50, y=400, width=200)

        img1 = Image.open(r"E:\Face\Images\jhds.png")
        img1 = img1.resize((200, 50), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2", font=(
            "times new roman", 12, "bold"))
        b1.place(x=400, y=400, width=200)

        # =========== Function Declaration ==========

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "Password & Confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Please agree our terms & conditions")
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="mysqlisbest@#1", database="mydata")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get(),
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registered Successfully")


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
