class Student:
    def __init__(self, name, surname, gender): #Конструктор
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name): #Метод добавления нового курса в список оконченных студентом курсов
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade): #Метод выставления оценок лекторам
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self): #функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса.
        total_grades = 0
        count = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            count += len(grades)
        return total_grades / count if count != 0 else 0

    def __str__(self): #метод вывода информации
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade():.1f}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"

    def __lt__(self, other): #метод сравнения объектов этих классов по их средней оценке.
        if not isinstance(other, Student):
            print("Сравнение невозможно")
            return
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname): #Конструктор
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self): #метод вывода информации
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor): #Класс лекторы
    def __init__(self, name, surname): #Конструктор
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self): #функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса.
        total_grades = 0
        count = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            count += len(grades)
        return total_grades / count if count != 0 else 0

    def __str__(self): #метод вывода информации
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade():.1f}"

    def __lt__(self, other): #метод сравнения объектов этих классов по их средней оценке.
        if not isinstance(other, Lecturer):
            print("Сравнение невозможно")
            return
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor): #Класс эксперты
    def rate_hw(self, student, course, grade): #метод для оценки домашних заданий студента по определенному курсу
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Создание экземпляров классов и вызов методов

# Студенты
student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Jack', 'Smith', 'male')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Введение в программирование']

# Лекторы
lecturer_1 = Lecturer('John', 'Doe')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Jane', 'Doe')
lecturer_2.courses_attached += ['Python']

# Проверяющие
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python', 'Git']

reviewer_2 = Reviewer('Another', 'Reviewer')
reviewer_2.courses_attached += ['Python']

# Оценка студентов за домашние задания
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Python', 8)

# Оценка лекторов за лекции
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Git', 9)
student_2.rate_lecturer(lecturer_2, 'Python', 8)

# Вывод информации
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

# Сравнение студентов и лекторов
print(student_1 < student_2)  # False
print(lecturer_1 > lecturer_2)  # True


# Функции для подсчета средней оценки

def average_grade_students(students, course):
    total_grades = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            count += len(student.grades[course])
    return total_grades / count if count != 0 else 0


def average_grade_lecturers(lecturers, course):
    total_grades = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total_grades / count if count != 0 else 0


# Вычисление средней оценки
students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]
print(average_grade_students(students, 'Python'))  # Средняя оценка студентов за курс "Python"
print(average_grade_lecturers(lecturers, 'Python'))  # Средняя оценка лекторов за курс "Python"