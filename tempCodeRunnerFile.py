from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def _init_(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Record")
        
        #=========variables==============
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()       
        
        
        
        
        #first Image
        img=Image.open(r"C:\Users\Ashish Shiv\OneDrive\Desktop\FACEEEEEEE\college_images\Header.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk 
        PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second Image
        img1=Image.open(r"C:\Users\Ashish Shiv\OneDrive\Desktop\FACEEEEEEE\college_images\Header.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #third Image
        img2=Image.open(r"C:\Users\Ashish Shiv\OneDrive\Desktop\FACEEEEEEE\college_images\Header.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
        #bg image
        img3=Image.open(r"C:\Users\Ashish Shiv\OneDrive\Desktop\FACEEEEEEE\college_images\bg.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="Student Registration",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=55,width=1450,height=600)
        
        #left label frame
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=600)
        
        img_left=Image.open(r"C:\Users\Ashish Shiv\OneDrive\Desktop\FACEEEEEEE\college_images\Header.jpg")
        img_left=img_left.resize((500,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=50,y=220,width=720,height=100)
        
        #current course

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=110,width=730,height=150)
        
        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read only")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        
        #course
        course_label=Label(current_course_frame,text="  Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only")
        course_combo["values"]=("Select Course","FE","SE","TE","FE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only")
        year_combo["values"]=("Select Course","FE","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="read only")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        # Class Student information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=260,width=730,height=250)
        
        #student id
        studentId_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)
        
        studentID_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_id,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

            #student name
        studentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
            
        studentName_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
            
        #class division
        class_div_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
            
        # class_div_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_class,font=("times new roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",16,"bold"),state="read only")
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
            
        #Roll No
        roll_no_label=Label(class_Student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
            
        roll_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #gender
        
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)
        
        #Dob
         
        dob_label=Label(class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
            
        #Email
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
            
        email_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_email,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
            
            #phone
        phone_label=Label(class_Student_frame,text="Phone no:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
            
        phone_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_phone,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
            
            #Address
        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
            
        address_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_address,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        
            
            
            #teacher
        teacher_label=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
            
        teacher_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
            
            #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
            
    
        
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)
            
            #buttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=725,height=50)
            
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman",12,"bold"))
        save_btn.grid(row=0,column=0)
            
        update_btn=Button(btn_frame,text="Update",command=self.update_data,cwidth=19,font=("times new roman",12,"bold"))
        update_btn.grid(row=0,column=1)
            
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=19,font=("times new roman",12,"bold"))
        delete_btn.grid(row=0,column=2)
            
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"))
        reset_btn.grid(row=0,column=3)
            
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=19,font=("times new roman",12,"bold"))
        take_photo_btn.grid(row=1,column=0)
            
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=19,font=("times new roman",12,"bold"))
        update_photo_btn.grid(row=1,column=1)
            
            
            
            
            
            
        #Right label frame
            
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=660,height=580)
            
        img_right=Image.open(r"C:\Users\Ashish Shiv\OneDrive\Desktop\FACEEEEEEE\college_images\Header.jpg")
        img_right=img_right.resize((500,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
            
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=100)
            
            #==========Search System==========
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=130,width=700,height=70)
            
        search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
            
        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="read only")
        search_combo["values"]=("Select","Roll_No","Phone_NO")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
            
        search_entry=ttk.Entry(Search_frame,width=13,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
            
        search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",12,"bold"))
        search_btn.grid(row=0,column=3)
            
        showAll_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",12,"bold"))
        showAll_btn.grid(row=0,column=4)
            
            #==============table frame===============
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=640,height=300)
            
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
            
        self.student_table=ttk.Treeview(table_frame,column=("Department","Course","Year","Sem","Id","Name","Div","Roll","Gender","Dob","Email","Gender","Phone","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

            
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
            
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Id",text="StudentId")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("Dob",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSampleSatatus")
        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.student_table.pack(fill=BOTH,expand=1)
        self.fetch_data( )



#=====================Function Declaration================

        
def add_data(self):
    if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":messagebox.showerror("Error","All Fields are required",parent=self.root)
    else:
        try:
            conn=mysql.connector.connect(host="local",username="root",password="1234",database="face recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("inset into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_id.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get()
                                    
                                                                                                        ))



conn.commit() 
self.fetch_data()
conn.close()
messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
except Exception as es:
messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    #========================fetch Data===============
    
    def fetch_data(self):
         conn=mysql.connector.connect(host="local",username="root",password="1234",database="face recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            fro i in data:
                self.student_table.insert("",END,values=i)
                conn.cmmit()
            conn.close()
            
            
#====================get cursor====================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data= content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_.teacher(data[13]),
        self.var_radio1.set(data[14])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.  var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0: 
                    conn=mysql.connector.connect(host="local",username="root",password="1234",database="face recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                    self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.var_std_id.get(),
                                    self.var_std_name.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get(),
                                    self.var_teacher.get(),
                                    self.var_radio1.get(),
                                    self.va_std_id.get(),
                    ))
        
        else:
            if not Update:
                return 
        messagebox.showinfo("Success","Student details succesfully update completed",parent=self.root)
        conn.commit()
        self.fetch_data()
        conn.close()
    except Exception as es:
        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#Delete function
def delete_data(self):
    if self.va_id.get()=="":
        messagebox.showerror("Error","Student id must be required",parent=self.root)
    else:
        try:
            delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
            if delete>0:
                 conn=mysql.connector.connect(host="local",username="root",password="1234",database="face recognition")
                 my_cursor=conn.cursor()
                 sql="delete from student where Student_id=%s"
                 val=(self.var_std_id.get(),)
                 my_cursor.execute(sql,val)
            else:
                if not delete:
                    return
                
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Delete","Succesfully deleted student details",parent=self.root)
            except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        
        #reset
        
        def reset_data(self):
            self.var_dep.set("Select Department")
            self.var_course.set("Select Course")
            self.var_year.set("Select Year")
            self.var_semester.set("Select Semester")
            self.var_std_id.set("")
            self.var_std_name.set("")
            self.var_div.set("Select Division")
            self.var_roll.set("")
            self.var_gender.set("")
            self.var_dob.set("")
            self.var_email.set("")
            self.var_phone.set("")
            self.var_address.set("")
            self.var_teacher.set("")
            self.var_radio1.set("")
        
    
    #==================General data set Take Photo Samples================
    
    def generate_dataset(self):
           if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0: 
                    conn=mysql.connector.connect(host="local",username="root",password="1234",database="face recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                        id+=1
                     my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                    self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.var_std_id.get(),
                                    self.var_std_name.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get(),
                                    self.var_teacher.get(),
                                    self.var_radio1.get(),
                                    self.va_std_id.get()==id+1
                    
                    
                    
                                   ))
       conn.commit()
       self.fetch_data()
       self.reset_data()
       conn.close()     
       
    #=========Load predifined data on face==================
        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        
        def face_cropped(img):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=face_classifier.detectMultiScale(gray,1.3,5)
            #scaling factor=1.3
            #Minimum Neighbor=5
            
            for(x,y,w,h) in faces:
                face_cropped=img[y:y+h,x:x+w]
                return face_cropped
            
            cap=cv2.VideoCapture(0)
            img_id=0
            while True:
                ret,my_frame=cap.read()
                if face_cropped(my_frame) is not None:
                    img_id+=1
                    face=cv2.resize(face_cropped(my_frame),(450,450))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path)
                    cv2.PutText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255,0),2)
                    cv2.imshow("Crooped Face",face)
                
                if cv2.waitKey(1)==13 or int(img_id)==100:
                    break 
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Generating data set completed!!!")
             except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)        
        
            
        
    if _name== "main_":
        root=Tk()
        obj=student(root)
        root.mainloop()