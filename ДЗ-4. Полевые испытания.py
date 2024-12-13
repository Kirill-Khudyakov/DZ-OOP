# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а
# также реализуйте две функции:

# 1) для подсчета средней оценки за домашние задания по всем студентам в
# рамках конкретного курса (в качестве аргументов принимаем список
# студентов и название курса);
# 2) для подсчета средней оценки за лекции всех лекторов в рамках курса
# (в качестве аргумента принимаем список лекторов и название курса)

class Mentor:
    mentor_list = []
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []      # Прилагаемые курсы
        self.grades_dict_lecturer = {}  # Cловарь с оценками лекторам от студентов
        self.average_grade = 0          # Средняя оценка за лекции
        self.mentor_list.append(self)   # Добавление в список преподователей вновь созданный экземпляр


class Student:
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.student_list.append(self)  # Добавление в список студентов вновь созданный экземпляр
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
        self.average_grade = round(sum_/len(grade_list),1)   # Подсчет среднего значения всех оценок
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
        self.average_grade = round(sum_/len(grade_list),1)  # Подсчет среднего значения всех оценок  
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
some_student_4.courses_in_progress.append('Data Science')
some_student_5 = Student('Some', 'Buddy', 'мужчина')
some_student_5.courses_in_progress.append('Python')
some_student_5.courses_in_progress.append('Data Science')


# Выставления оценок лектору_1:
some_student_1.add_grades_lecturer(some_lecturer_1, 'Python', 10) 
some_student_2.add_grades_lecturer(some_lecturer_1, 'Python', 10)
some_student_3.add_grades_lecturer(some_lecturer_1, 'Python', 10)
some_student_4.add_grades_lecturer(some_lecturer_1, 'Python', 10)
some_student_5.add_grades_lecturer(some_lecturer_1, 'Python', 10)

# Выставления оценок лектору_2:
some_student_1.add_grades_lecturer(some_lecturer_2, 'Python', 10) 
some_student_2.add_grades_lecturer(some_lecturer_2, 'Python', 10) 
some_student_3.add_grades_lecturer(some_lecturer_2, 'Python', 10) 
some_student_4.add_grades_lecturer(some_lecturer_2, 'Python', 10) 
some_student_5.add_grades_lecturer(some_lecturer_2, 'Python', 10) 

print(some_lecturer_1.grades_dict_lecturer)      # Проверка оценки лектора_1
print(some_lecturer_2.grades_dict_lecturer)      # Проверка оценки лектора_2
print(some_lecturer_1.average_grade_lectures())  # Вызов метода вычисления средней оценки лектора_1
print(some_lecturer_1)                           # Проверка переопределения метода __str__ для лектора_1

# Инициализация проверяющих:
some_reviewer_1 = Reviewer ('Андрей','Семенов')
some_reviewer_1.courses_attached.append('Python')         # Добавления курса 'Python' в список проверяемых курсов
some_reviewer_1.courses_attached.append('Data Science')   # Добавления курса 'Data Science' в список проверяемых курсов

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
# print(some_student_1.average_grade_student())  

some_reviewer_1.add_grades_student(some_student_3, 'Python', 6)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 6)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 6)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 8)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 10)
some_reviewer_1.add_grades_student(some_student_3, 'Python', 8)
# print(f'Оценки для some_student_3 - {some_student_3.grades_dict_student}')

some_reviewer_1.add_grades_student(some_student_4, 'Data Science', 8)
some_reviewer_1.add_grades_student(some_student_4, 'Data Science', 9)
some_reviewer_1.add_grades_student(some_student_4, 'Data Science', 10)
some_reviewer_1.add_grades_student(some_student_4, 'Data Science', 8)
some_reviewer_1.add_grades_student(some_student_4, 'Data Science', 8)
some_reviewer_1.add_grades_student(some_student_4, 'Data Science', 8)
some_reviewer_1.add_grades_student(some_student_4, 'Data Science', 2)
some_reviewer_1.add_grades_student(some_student_4, 'Data Science', 8)
some_reviewer_1.add_grades_student(some_student_4, 'Data Science', 8)
some_reviewer_1.add_grades_student(some_student_4, 'Data Science', 6)
# print(f'Оценки для some_student_4 - {some_student_4.grades_dict_student}')

some_reviewer_1.add_grades_student(some_student_5, 'Data Science', 10)
some_reviewer_1.add_grades_student(some_student_5, 'Data Science', 9)
some_reviewer_1.add_grades_student(some_student_5, 'Data Science', 10)
some_reviewer_1.add_grades_student(some_student_5, 'Data Science', 8)
some_reviewer_1.add_grades_student(some_student_5, 'Data Science', 8)
some_reviewer_1.add_grades_student(some_student_5, 'Data Science', 8)
some_reviewer_1.add_grades_student(some_student_5, 'Data Science', 2)
some_reviewer_1.add_grades_student(some_student_5, 'Data Science', 8)
some_reviewer_1.add_grades_student(some_student_5, 'Data Science', 8)
some_reviewer_1.add_grades_student(some_student_5, 'Data Science', 6)
# print(f'Оценки для some_student_5 - {some_student_5.grades_dict_student}')

some_student_1.courses_in_progress.append('Git')  # Добавление курса в список текущих курсов
# print(some_student_1.courses_in_progress)

some_student_1.finished_courses.append('Введение в программирование')
print(some_student_1)    # Проверка переопределения метода __str__ для студентов

# Проверка словарей с оценками у лекторов:
print(some_lecturer_1.grades_dict_lecturer)
print(some_lecturer_2.grades_dict_lecturer)

# Средние оценки лекторов 1 и 2:
some_lecturer_1.average_grade = some_lecturer_1.average_grade_lectures()
some_lecturer_2.average_grade = some_lecturer_2.average_grade_lectures()
print(some_lecturer_1.average_grade, some_lecturer_2.average_grade)

# Cравнение лекторов по средним оценкам за лекции:
print(some_lecturer_1 < some_lecturer_2)
print(some_lecturer_1 > some_lecturer_2)

# Средние оценки студентов 1 - 3:
some_student_1.average_grade = some_student_1.average_grade_student()
some_student_2.average_grade = some_student_2.average_grade_student()
some_student_3.average_grade = some_student_3.average_grade_student()
print(some_student_1.average_grade, some_student_2.average_grade, some_student_3.average_grade)

# Сравнение студентов по по средней оценки за домашние задания:
print(some_student_1 > some_student_2)
print(some_student_1 < some_student_3)


#  Функция для подсчета средней оценки за домашние задания по всем
#  студентам в рамках конкретного курса (в качестве аргументов принимаем список
#  студентов и название курса)
def get_average_grade_student_course(other_list, course):
     # Cоздаём пустой список оценок всех студентов конкретного курса:
    all_grades_list_course = []
    for student in other_list:
        for key, vul in student.grades_dict_student.items():
            if key == course:
                all_grades_list_course.extend(vul)  # Добавление в общий список оценок, оценки конкретного студента
    sum_ = sum(all_grades_list_course)              # Сумма всех оценок студентов данного курса
    average_grade_student = round(sum_ / len(all_grades_list_course), 1)
    return average_grade_student   

# Проверка работы функции для подсчёта средней оценки за ДЗ студентов для 2-х курсов:     
print(get_average_grade_student_course(Student.student_list,'Python'))
print(get_average_grade_student_course(Student.student_list,'Data Science'))


# Функция , формирующая список курсов лекторов
def get_lecturer_course(other_list):
    lecturer_course_all = []
    for mentor in other_list:
        if len(mentor.grades_dict_lecturer) > 0: # Убираем проверяющих из списка преподавателей
            lecturer_course_all.extend(mentor.courses_attached)
    lecturer_course_list = list(set(lecturer_course_all))
    return lecturer_course_list
# Проверка
print(get_lecturer_course(Mentor.mentor_list))


# Функция для подсчета средней оценки за лекции всех лекторов c проверкой
# (в качестве аргумента принимаем список лекторов и название курса)
def get_average_grade_mentor_course (other_list,course):
    lecturer_course_list = get_lecturer_course(other_list)   # Вызов списка курсов лекторов
    # Проверяем, входит ли подаваемый на вход функции курс в список курсов лекторов
    if course not in lecturer_course_list :
        print('Ошибка.Такого курса нет в списке курсов лекторов')
        return
    all_grades_lecturer_course = [] # Список оценок лекторов
    for lecturer in other_list:
        if len(lecturer.grades_dict_lecturer) > 0:
            for key, vul in lecturer.grades_dict_lecturer.items():
                if key == course:
                    all_grades_lecturer_course.extend(vul)  # Заполняем список оценок лекторов
    sum_ = sum(all_grades_lecturer_course)                  # Сумма всех оценок лекторов данного курса
    # Средняя оценка
    average_grade_lecturer = round(sum_ / len(all_grades_lecturer_course), 1)
    return average_grade_lecturer
# Вызываем функцию для подсчета средней оценки за лекции всех лекторов
print(get_average_grade_mentor_course(Mentor.mentor_list,'Python'))
# Проверка при неправильном введении курса :
print(get_average_grade_mentor_course(Mentor.mentor_list,'ython'))