from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"E:\Face\Images\B.jpg")
        # bg=bg.resize((220,220),ImageTk.LANCZOS)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=510, y=130, width=340, height=450)

        img1 = Image.open(
            r"E:\Face\Images\user-avatar-red-icon-vector-882530.jpg")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black")
        lblimg1.place(x=630, y=135, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 16, "bold"), fg="white", bg="black")
        get_str.place(x=110, y=100)

        # label
        username = lbl = Label(frame, text="Username", font=(
            "times new roman", 12, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 12, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = lbl = Label(frame, text="Password", font=(
            "times new roman", 12, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 12, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        # ======== Icon Images ========== #

        img2 = Image.open(r"E:\Face\Images\D.jpg")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage1, bg="black")
        lblimg2.place(x=550, y=280, width=25, height=25)

        img3 = Image.open(
            r"E:\Face\Images\evolution-of-the-https-lock-icon-infographi.jpg")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black")
        lblimg3.place(x=550, y=350, width=25, height=25)

        # ====== Login Button =============

        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 14, "bold"), bd=3,
                          relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # ========= Register Button =========

        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 10, "bold"),
                             borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=20, y=360, width=160)

        # ========= forgot Button ======

        forgotbtn = Button(frame, text="Forget Password", font=("times new roman", 10, "bold"),
                           borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgotbtn.place(x=14, y=390, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All field required")
        elif self.txtuser.get() == "kundan" and self.txtpass.get() == "kund":
            messagebox.showinfo("Success", "Welcome....")
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="mysqlisbest@#1", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("Select * from register where email=%s and password=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                open_main = messagebox.askyesno("YesNO", "Access only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.new_window)
                    # self.app=


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
    main()
