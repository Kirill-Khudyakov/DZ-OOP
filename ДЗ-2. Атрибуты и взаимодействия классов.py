# В квизе к предыдущей лекции мы реализовали возможность выставлять студентам
# оценки за домашние задания. Теперь это могут делать только Reviewer (реализуйте такой метод)!
# А что могут делать лекторы? Получать оценки за лекции от студентов :)
# Реализуйте метод выставления оценок лекторам у класса Student
# (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer,
# в котором ключи – названия курсов, а значения – списки оценок).
# Лектор при этом должен быть закреплен за тем курсом, на который записан студент.

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []      # Прилагаемые курсы
        self.grades_dict_lecturer = {}  # Cловарь с оценками лекторам от студентов


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []   # Текущие курсы
        self.grades_dict_student = {}

    # Метод для добавленя пройденных курсов:

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    # Метод выставления оценок студентами лекторам:

    def add_grades_lecturer(self, lecturer, course, grades):
        # Если лектор - экземпляр класса Lecturer , курс входит в список курсов ,которые
        # ведёт лектор и курс входит в список текущих курсов студента :
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_dict_lecturer:
                lecturer.grades_dict_lecturer[course] += [grades]
            else:
                lecturer.grades_dict_lecturer[course] = [grades]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    def add_grades_student(self, student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_dict_student:
                student.grades_dict_student[course] += [grades]
            else:
                student.grades_dict_student[course] = [grades]
        else:
            return 'Ошибка'

student_1 = Student('Кирилл', 'Худяков', 'мужчина')
student_1.courses_in_progress.append('Python')

reviewer_1 = Reviewer('Андрей', 'Иванов')
reviewer_1.courses_attached.append('Python')

reviewer_1.add_grades_student(student_1, 'Python', 8)
reviewer_1.add_grades_student(student_1, 'Python', 9)
reviewer_1.add_grades_student(student_1, 'Python', 10)

# Проверка:
# Студент_1:
print(student_1.name)
print(student_1.surname)
print(student_1.gender)
print(student_1.courses_in_progress)
print(student_1.grades_dict_student)

# Проверяющий_1:
print(reviewer_1.name)
print(reviewer_1.surname)
print(reviewer_1.courses_attached)


lecturer_1 = Lecturer('Николай', 'Новиков')
lecturer_1.courses_attached.append('Python')
lecturer_1.courses_attached.append('Java')

student_2 = Student('Ирина', 'Худякова', 'женщина')
student_2.courses_in_progress.append('Python')
student_3 = Student('Наталья', 'Ковязина', 'женщина')
student_3.courses_in_progress.append('Python')
student_4 = Student('Сергей', 'Скороход', 'мужчина')
student_4.courses_in_progress.append('Java')
student_5 = Student('Александр', 'Ковязин', 'мужчина')
student_5.courses_in_progress.append('Java')

# Выставление оценок лектору_1:
student_1.add_grades_lecturer(lecturer_1, 'Python', 8)
student_2.add_grades_lecturer(lecturer_1, 'Python', 8)
student_3.add_grades_lecturer(lecturer_1, 'Python', 9)
student_4.add_grades_lecturer(lecturer_1, 'Java', 10)
student_5.add_grades_lecturer(lecturer_1, 'Java', 7)

# Проверка:
print(lecturer_1.courses_attached)
print(lecturer_1.grades_dict_lecturer)