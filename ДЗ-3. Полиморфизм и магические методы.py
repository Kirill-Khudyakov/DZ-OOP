# Перегрузите магический метод __str__ у всех классов.
# У проверяющих он должен выводить информацию в следующем виде:
# print(some_reviewer)
# Имя: Some
# Фамилия: Buddy

# У лекторов:
# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9

# У студентов :
# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование

# 2) Реализуйте возможность сравнивать (через операторы сравнения)
# между собой лекторов по средней оценке за лекции и студентов по
# средней оценке за домашние задания.

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []      # Прилагаемые курсы
        self.grades_dict_lecturer = {}  # Cловарь с оценками лекторам от студентов
        self.average_grade = 0          # Средняя оценка за лекции


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []   # Текущие курсы
        self.grades_dict_student = {}   # Cловарь с оценками студентов от проверяющих
        self.average_grade = 0          # Средняя оценка за ДЗ


# Метод для добавления пройденных курсов:
    def add_courses (self, course_name):
        self.finished_courses.append(course_name)


# Метод вычисления средней оценки за ДЗ:
    def average_grade_student(self):
        grade_list = []
        for val in self.grades_dict_student.values():
            grade_list.extend(val)
        sum_ = sum(grade_list)                               # Подсчет суммы оценок
        self.average_grade = round(sum_/len(grade_list),2)   # Подсчет среднего значения всех оценок
        return self.average_grade
    

# Метод выставления оценок студентами лекторам:
    def add_grades_lecturer(self, lecturer, course, grades):
        # Если лектор - экземпляр класса Lecturer, курс входит в список курсов, которые
        # ведёт лектор и курс входит в список текущих курсов студента:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_dict_lecturer:
                lecturer.grades_dict_lecturer[course] += [grades]
            else:
                lecturer.grades_dict_lecturer[course] = [grades]
        else:
            return 'Ошибка'
        

# Метод __str__ для Student:
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя '\
              f'оценка за домашние задания: {self.average_grade_student()}\n'\
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'\
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res
    

 # Метод сравнения средних оценок студентов: 
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade < other.average_grade 


# Дочерние для класса Mentor классы Lecturer (лекторы) и Reviewer(проверяющие):
class Lecturer(Mentor):

# Метод вычисления средней оценки за лекции:  
    def average_grade_lectures(self):
        grade_list = []
        for val in self.grades_dict_lecturer.values():
            grade_list.extend(val)
        sum_ = sum(grade_list)                              # Подсчет суммы оценок:
        self.average_grade = round(sum_/len(grade_list),2)  # Подсчет среднего значения всех оценок  
        return self.average_grade


# Метод сравнения средних оценок лекторов:
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_grade < other.average_grade


# Метод __str__ для Lecturer:
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя ' \
              f'оценка за лекции: {self.average_grade_lectures()}'
        return res


class Reviewer(Mentor):
    # Метод, который позволяет проверяющему добавить оценку в словарь студента по названию курса:
    def add_grades_student(self, student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_dict_student:
                student.grades_dict_student[course] += [grades]
            else:
                student.grades_dict_student[course] = [grades]
        return 'Ошибка'


# Метод __str__ для Reviewer: 
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res      

# Проверка метода __str__ для проверяющих:
some_reviewer_1 = Reviewer('Some','Buddy')
print(some_reviewer_1)

# Инициализация лекторов:
some_lecturer_1 = Lecturer('Some', 'Buddy')
some_lecturer_1.courses_attached.append('Python')
some_lecturer_2 = Lecturer('Some', 'Buddy')
some_lecturer_2.courses_attached.append('Python')

# Инициализация студентов:
some_student_1 = Student('Ruoy', 'Eman', 'мужчина')
some_student_1.courses_in_progress.append('Python')
some_student_2 = Student('Some', 'Buddy', 'мужчина')
some_student_2.courses_in_progress.append('Python')
some_student_3 = Student('Some', 'Buddy', 'мужчина')
some_student_3.courses_in_progress.append('Python')    
some_student_4 = Student('Some', 'Buddy', 'мужчина')
some_student_4.courses_in_progress.append('Python')
some_student_5 = Student('Some', 'Buddy', 'мужчина')
some_student_5.courses_in_progress.append('Python')
some_student_6 = Student('Some', 'Buddy', 'мужчина')
some_student_6.courses_in_progress.append('Python')
some_student_7 = Student('Some', 'Buddy', 'мужчина')
some_student_7.courses_in_progress.append('Python')
some_student_8 = Student('Some', 'Buddy', 'мужчина')
some_student_8.courses_in_progress.append('Python')
some_student_9 = Student('Some', 'Buddy', 'мужчина')
some_student_9.courses_in_progress.append('Python')
some_student_10 = Student('Some', 'Buddy', 'мужчина')
some_student_10.courses_in_progress.append('Python')

# Выставления оценок лектору_1:
some_student_1.add_grades_lecturer(some_lecturer_1, 'Python', 10) 
some_student_2.add_grades_lecturer(some_lecturer_1, 'Python', 10)
some_student_3.add_grades_lecturer(some_lecturer_1, 'Python', 10)
some_student_4.add_grades_lecturer(some_lecturer_1, 'Python', 10)
some_student_5.add_grades_lecturer(some_lecturer_1, 'Python', 10)
some_student_6.add_grades_lecturer(some_lecturer_1, 'Python', 10)
some_student_7.add_grades_lecturer(some_lecturer_1, 'Python', 10)
some_student_8.add_grades_lecturer(some_lecturer_1, 'Python', 10)
some_student_9.add_grades_lecturer(some_lecturer_1, 'Python', 10)
some_student_10.add_grades_lecturer(some_lecturer_1, 'Python', 9)

# Выставления оценок лектору_2:
some_student_1.add_grades_lecturer(some_lecturer_2, 'Python', 10) 
some_student_2.add_grades_lecturer(some_lecturer_2, 'Python', 10) 
some_student_3.add_grades_lecturer(some_lecturer_2, 'Python', 10) 
some_student_4.add_grades_lecturer(some_lecturer_2, 'Python', 10) 
some_student_5.add_grades_lecturer(some_lecturer_2, 'Python', 10) 
some_student_6.add_grades_lecturer(some_lecturer_2, 'Python', 8) 
some_student_7.add_grades_lecturer(some_lecturer_2, 'Python', 9) 
some_student_8.add_grades_lecturer(some_lecturer_2, 'Python', 9) 
some_student_9.add_grades_lecturer(some_lecturer_2, 'Python', 9) 
some_student_10.add_grades_lecturer(some_lecturer_2, 'Python', 10) 


#print(some_lecturer_1.grades_dict_lecturer)      # Проверка оценки лектора
#print(some_lecturer_1.average_grade_lectures())  # Вызов метода вычисления средней оценки лектора_1
print(some_lecturer_1)                            # Проверка переопределения метода __str__ для лектора_1:

# Инициализация проверяющих:
some_reviewer_1 = Reviewer('Some','Buddy')
some_reviewer_1.courses_attached.append('Python')  # Добавления курса 'Python' в список проверяемых курсов

# Выставление оценок проверяющими (reviewer) студентам соответствующих курсов:
some_reviewer_1.add_grades_student(some_student_1, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_1, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_1, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_1, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_1, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_1, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_1, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_1, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_1, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_1, 'Python', 9)
# print(f'Оценки для some_student_1 - {some_student_1.grades_dict_student}')

some_reviewer_1.add_grades_student(some_student_2, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_2, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_2, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_2, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_2, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_2, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_2, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_2, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_2, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_2, 'Python', 8)
# print(f'Оценки для some_student_2 - {some_student_2.grades_dict_student}')
# print(some_student_1.average_grade_student())   # 9.9

some_reviewer_1.add_grades_student(some_student_3, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 9)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 8)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 8)

some_student_1.courses_in_progress.append('Git')  # Добавление курса в список текущих курсов
# print(some_student_1.courses_in_progress)

some_student_1.finished_courses.append('Введение в программирование')
print(some_student_1)


# 2) Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов 
# по средней оценке за лекции и студентов по средней оценке за домашние задания.

# Проверка словарей с оценками у лекторов:
# print(some_lecturer_1.grades_dict_lecturer)
# print(some_lecturer_2.grades_dict_lecturer)

# Средние оценки лекторов 1 и 2:
some_lecturer_1.average_grade = some_lecturer_1.average_grade_lectures()
some_lecturer_2.average_grade = some_lecturer_2.average_grade_lectures()
# print(some_lecturer_1.average_grade, some_lecturer_2.average_grade)

# Cравнение лекторов по средним оценкам за лекции:
print(some_lecturer_1 < some_lecturer_2)
print(some_lecturer_1 > some_lecturer_2)

# Средние оценки студентов 1 - 3:
some_student_1.average_grade = some_student_1.average_grade_student()
some_student_2.average_grade = some_student_2.average_grade_student()
some_student_3.average_grade = some_student_3.average_grade_student()
# print(some_student_1.average_grade, some_student_2.average_grade, some_student_3.average_grade)

# Сравнение студентов по по средней оценки за домашние задания:
print(some_student_1 > some_student_2)
print(some_student_1 < some_student_3)