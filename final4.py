import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import numpy as np
import csv

st.title("Dexcom Students System")
######### Global variables  ##########
names = ['Admin','Teacher']
usernames = ['admin','teacher']
passwords = ['123','456']

admin_csv = "admin_data.csv"
student_csv = "student_data.csv"
teacher_csv = "teacher_data.csv"
subject_csv = "subject_data.csv"
##################################
hashed_passwords = stauth.Hasher(passwords).generate()
authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)

name, authentication_status, username = authenticator.login('Login','main')


if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write('## Welcome *%s*' % (name))
    st.write("### What is Dataset you want?")
    select_item = st.radio("Please select Dataset",
                  ("Add Admin", "Add Teacher", "Add Student","Add Subject"))
#######################   add admin file 1,2  ###############################################
    if select_item == "Add Admin":      ### add admin
        file1 = open(admin_csv)
        df_admins = pd.DataFrame(file1)  
        file1.close()
        
        admin_id = st.sidebar.text_input("Admin ID")
        admin_name = st.sidebar.text_input("Admin Name")
        admin_phone = st.sidebar.text_input("Admin Phone Number")
        
        
        @st.cache(allow_output_mutation=True)
        def get_data_admin():
            return []
            
        
        df_admins = pd.DataFrame(get_data_admin())
        
        if st.sidebar.button("Add Admin"):
            get_data_admin().append({"Admin_ID": admin_id, 
                           "Admin_Name": admin_name, 
                           "Admin_Phone": admin_phone})
#             st.write("## Show Admin Dataset")
#             st.write(df_admins)
#             st.write(df_admins.shape)
            
        if st.button("Show Dataset") :
            st.write("## Show Admin Dataset")
            st.write(df_admins)
        
            
        
        
       #####convert df to csv and save it    ###
        def convert_df(df_admins):
            return df_admins.to_csv().encode('utf-8')
        
        
        csv1 = convert_df(df_admins)
        #st.write(csv1)
        
        file2 = open(admin_csv)
        df_admins.to_csv (r'admin_data.csv', index = False, header=True)
        file2.close()
        
  ###################################### add teacher file 3,4 ###############################################
    elif select_item == "Add Teacher":  ### add teacher
        file1 = open(teacher_csv)
        df_admins = pd.DataFrame(file1)  
        file1.close()
        
        teacher_id = st.sidebar.text_input("Teacher ID")
        teacher_name = st.sidebar.text_input("Teacher Name")
        teacher_phone = st.sidebar.text_input("Teacher Phone Number")
        teacher_Class_Name = st.sidebar.text_input("Teacher Class Name")
        teacher_Subject    = st.sidebar.text_input("Teacher Subject")
        
        @st.cache(allow_output_mutation=True)
        def get_data_teacher():
            return []
            
        
        df_teachers = pd.DataFrame(get_data_teacher())
        
        if st.sidebar.button("Add Teacher"):
            get_data_teacher().append({"Teacher_ID": teacher_id, 
                           "Teacher_Name": teacher_name, 
                           "Teacher_Phone": teacher_phone,
                           "Teacher_Class_Name":teacher_Class_Name,
                           "Teacher_Subject":teacher_Subject})
#             st.write("## Show Teacher Dataset")
#             st.write(df_teachers)
#             st.write(df_teachers.shape)
            
        if st.button("Show Dataset") :
            st.write("## Show Teacher Dataset")
            st.write(df_teachers)
            
        
        
       #####convert df to csv and save it    ###
        def convert_df(df_teachers):
            return df_teachers.to_csv().encode('utf-8')
        
        
        csv1 = convert_df(df_teachers)
        #st.write(csv1)
        
        file2 = open(teacher_csv)
        df_teachers.to_csv (r'teacher_data.csv', index = False, header=True)
        file2.close()
  ################################## add student file 5,6#####################################################
    elif select_item == "Add Student":    ### add student
        file5 = open("student_data.csv")
        df_students = pd.DataFrame(file5)  
        file5.close()
        
        student_id = st.sidebar.text_input("Student ID")
        student_name = st.sidebar.text_input("Student Name")
        student_phone = st.sidebar.text_input("Student Phone Number")
        student_email = st.sidebar.text_input("Student Email")
        student_class_name = st.sidebar.text_input("Student Class Name")
        student_subject = st.sidebar.text_input("Student Subject")
        
        @st.cache(allow_output_mutation=True)
        def get_data_student():
            return []
            
        
        df_students = pd.DataFrame(get_data_student())
        
        if st.sidebar.button("Add Student"):
            get_data_student().append({"Student_ID": student_id, 
                           "Student_Name": student_name, 
                           "Student_Phone": student_phone,
                           "Student_Email": student_email,
                           "Student_Class_Name": student_class_name,
                           "Student_Subject": student_subject})
#             st.write("## Show Student Dataset")
#             st.write(df_students)
#             st.write(df_students.shape) 
            
        if st.button("Show Dataset") :
            st.write("## Show Student Dataset")
            st.write(df_students)
            
            
           
       
       #####convert df to csv and save it    ###
        def convert_df(df_students):
            return df_students.to_csv().encode('utf-8')
        
        
        csv1 = convert_df(df_students)
        #st.write(csv1)
        
        file6 = open('student_data.csv')
        df_students.to_csv (r'student_data.csv', index = False, header=True)
        file6.close()
       
   ############################# add subjectfile 7,8#######################################################
    elif select_item == "Add Subject":      ### add subject
        file7 = open(subject_csv)
        df_subjects = pd.DataFrame(file7)  
        file7.close()
        
        subject_id = st.sidebar.text_input("Subject ID")
        subject_name = st.sidebar.text_input("Subject Name")
        subject_date_time = st.sidebar.text_input("Subject Date Time")
        subject_Att_Grad = st.sidebar.text_input("Subject Attendance Grad")
        subject_home_work = st.sidebar.text_input("Subject Home Work Grad")
        subject_exam = st.sidebar.text_input("Subject Exam Grad")
        subject_Contribution = st.sidebar.text_input("Subject Contribution")
        
        @st.cache(allow_output_mutation=True)
        def get_data_subject():
            return []
            
        
        df_sunbjects = pd.DataFrame(get_data_subject())
        
        if st.button("Show Dataset") :
            st.write("## Show Subject Dataset")
            st.write(df_sunbjects)
        if st.sidebar.button("Add Subject"):
            get_data_subject().append({"Subject_ID":subject_id, 
                           "Subject_Name":subject_name, 
                           "Subject_Date_Time":subject_date_time,
                           "Subject_Attendance_Grad":subject_Att_Grad,
                           "Subject_HomWork_Grad":subject_home_work,
                           "Subject_Exam_Grad":subject_exam,
                           "Subject_Contribution":subject_Contribution})
#             st.write("## Show Subject Dataset")
#             st.write(df_subjects)
#             st.write(df_subjects.shape)
            
        
            
            
        
        
       #####convert df to csv and save it    ###
        def convert_df(df_subjects):
            return df_subjects.to_csv().encode('utf-8')
        
        
        csv1 = convert_df(df_subjects)
        #st.write(csv1)
        
        file8 = open(subject_csv)
        df_subjects.to_csv (r'subject_data.csv', index = False, header=True)
        file8.close()
##########################################################################################
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
