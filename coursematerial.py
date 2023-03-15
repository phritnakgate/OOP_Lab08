class CourseMaterial():
    def __init__(self, chap_mat, chap_title, course_prog, chap_test):
        self.__chap_mat = chap_mat
        self.__chap_title = chap_title
        self.__course_prog = course_prog
        self.__chap_test = chap_test


class Course_Progression():
    def __init__(self, is_exam_passed, learning_percentage, user):
        self.__is_exam_passed = is_exam_passed
        self.__learning_percentage = learning_percentage
        self.__user = user