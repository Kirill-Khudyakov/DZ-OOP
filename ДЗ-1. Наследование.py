# Исходя из квиза к предыдущему занятию, у нас уже есть класс преподавателей
# и класс студентов . Студентов пока оставим без изменения, а вот преподаватели бывают разные,
# поэтому теперь класс Mentor должен стать родительским классом,
# а от него нужно реализовать наследование классов Lecturer (лекторы)
# и Reviewer (эксперты, проверяющие домашние задания).
# Очевидно, имя, фамилия и список закрепленных курсов логично реализовать
# на уровне родительского класса.

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []  # Текущие курсы
        self.grades_dict = {}  


    # Метод для добавления пройденных курсов:    
    def add_courses (self, course_name):
        self.finished_courses.append(course_name)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # Прилагаемые курсы


    # Метод выставления оценок студентам:
    def add_grades(self, student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_dict:
                student.grades_dict[course] += [grades]
            else:
                student.grades_dict[course] = [grades]
        else:
            return 'Ошибка'
            

class Lecturer(Mentor):
    pass


class Reviever(Mentor):
    pass

# Проверка:
lecturer_1 = Lecturer('Олег', 'Булыгин')
lecturer_1.courses_attached.append('Python')

reviever_1 = Reviever ('Кирилл', 'Худяков')
reviever_1.courses_attached.append('Python')

print(lecturer_1.name)
print(lecturer_1.surname)
print(lecturer_1.courses_attached)

print(reviever_1.name)
print(reviever_1.surname)
print(reviever_1.courses_attached)





        

       