class User():
    def __init__(self, username, password, email, first_name, 
                last_name, gender, birth_date, education, country, province, login):
        self._username = username
        self._password = password
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._birth_date = birth_date
        self._education = education
        self._country = country
        self._province = province 
        self._login = login  # Composition of Login
    
class Admin(User):
    def __init__(self, course, course_recom, username, password, email, first_name,last_name, gender, birth_date, education, country, province, login):
        super().__init__(username, password, email, first_name,last_name, gender, birth_date, education, country, province, login)
        self.__course = course # Association of Courses 
        self.__course_recom = course_recom # Uni-di-Association of CourseRecom

class Student(User):
    def __init__(self, user, enroll, username, password, email, first_name,last_name, gender, birth_date, education, country, province, login):
        super().__init__(username, password, email, first_name,last_name, gender, birth_date, education, country, province, login)
        self.__enroll = enroll #  # Uni-di-Association of Enroll 

class Teacher(User):
    def __init__(self, teacher_dept, user, username, password, email, first_name,last_name, gender, birth_date, education, country, province, login):
        super().__init__(username, password, email, first_name,last_name, gender, birth_date, education, country, province, login)
        self.__teacher_dept = teacher_dept 