with open('students.txt','r') as st_file:
    sts = st_file.read().split('\n')
    with open('students2.txt','w+') as st_2_file:
     for student in sts:
        srt = student.split()
        name = srt[0]
        f_name = srt[1]
        email_n = srt[2]
        number = srt[3]
        print(name[0].upper()+name[1:len(name)],f_name[0].upper()+f_name[1:len(f_name)],email_n,'301-'+number)
        
        st_2_file.write(name[0].upper()+name[1:len(name)]+' ')    
        st_2_file.write(f_name[0].upper()+f_name[1:len(f_name)]+' ')
        st_2_file.write(email_n+' ')
        st_2_file.write('301-'+number+'\n')