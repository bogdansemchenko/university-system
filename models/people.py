from abc import ABC, abstractmethod
from models.university_structure import *
from models.exam import Exam, ExamResult, Question


class Student:
    def __init__(self, student_id: int, name: str, birth_date: str, is_budget: bool, average_grade: float):
        self.student_id = student_id
        self.name = name
        self.birth_date = birth_date
        self.is_budget = is_budget
        self.scholarship: float = 0.0
        self.average_grade = average_grade
        self._group: Optional[Group] = None
        self.borrowed_books: List[Book] = []

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value: Group):
        if self._group != value:
            old_group = self._group
            self._group = value
            if old_group:
                old_group.remove_student(self)
            if value:
                value.add_student(self)

    def update_average_grade(self, new_grade: float):
        self.average_grade = new_grade

    def take_exam(self, exam: Exam) -> ExamResult:
        return exam.conduct_exam(self)

    def choose_exam(self, department: 'Department') -> Optional[Exam]:
        print(f"\nДоступные экзамены в кафедре {department.name}:")
        for idx, exam in enumerate(department.exams):
            print(f"{idx + 1}. {exam.name}")

        try:
            exam_choice = int(input("Выберите номер экзамена, который хотите пройти: ")) - 1
            if 0 <= exam_choice < len(department.exams):
                return department.exams[exam_choice]
            else:
                print("Некорректный выбор.")
                return None
        except ValueError:
            print("Пожалуйста, введите правильный номер.")
            return None

    def borrow_book_from_library(self, library: Library, book_id: int):
        book = library.borrow_book(book_id)
        if book:
            self.borrowed_books.append(book)
            print(f"{self.name} взял книгу '{book.title}'")
        else:
            print(f"Книга с ID {book_id} не найдена в библиотеке.")

    def return_book_to_library(self, library: Library, book_id: int):
        book = None
        for b in self.borrowed_books:
            if b.book_id == book_id:
                book = b
                break

        if book:
            library.add_book(book)
            self.borrowed_books.remove(book)
            print(f"{self.name} вернул книгу '{book.title}' в библиотеку.")
        else:
            print(f"Книга с ID {book_id} не была взята студентом.")

    def __str__(self):
        return f"Студент ID: {self.student_id}, Имя: {self.name}, Средний балл: {self.average_grade}"


class DepartmentMember(ABC):
    @abstractmethod
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Teacher(DepartmentMember):
    def __init__(self, teacher_id: int, name: str, age: int, subject: str):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.subject = subject

    def create_exam(self, exam_name: str) -> Exam:
        return Exam(exam_name, self.subject)

    def add_question_to_exam(self, exam: Exam, text: str,
                             answers: List[str], correct_answers: List[int]):
        question = Question(text, answers, correct_answers)
        exam.add_question(question)

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Age: {self.age}, Subject: {self.subject}"



class DepartmentHead(Teacher):
    def __init__(self, teacher_id: int, name: str, age: int, subject: str):
        super().__init__(teacher_id, name, age, subject)
        self.department: Optional[Department] = None

    def assign_scholarships(self, department: 'Department'):
        for group in department.groups:
            for student in group.students:
                if student.average_grade < 5 or not student.is_budget:
                    student.scholarship = 0
                elif 5 <= student.average_grade < 6:
                    student.scholarship = 121
                elif 6 <= student.average_grade < 8:
                    student.scholarship = 160
                elif 8 <= student.average_grade < 9:
                    student.scholarship = 180
                elif 9 <= student.average_grade <= 10:
                    student.scholarship = 200
                print(f"Студент {student.name} получает стипендию: {student.scholarship} руб.")

    def hire_teacher(self, teacher: Teacher, department: 'Department'):
        if teacher not in department.teachers:
            department.teachers.append(teacher)
            print(f"Преподаватель {teacher.name} нанят на кафедру {department.name}.")
        else:
            print(f"Преподаватель {teacher.name} уже работает на кафедре {department.name}.")

    def fire_teacher(self, teacher: Teacher, department: 'Department'):
        if teacher in department.teachers:
            department.teachers.remove(teacher)
            print(f"Преподаватель {teacher.name} уволен с кафедры {department.name}.")
        else:
            print(f"Преподаватель {teacher.name} не найден на кафедре {department.name}.")

    def create_curriculum(self, department: 'Department', curriculum_data: dict):
        department.curriculum = curriculum_data
        print(f"Учебный план для кафедры {department.name} создан: {curriculum_data}")

    def set_curator_for_group(self, group: 'Group', teacher: 'Teacher'):
        group.set_curator(teacher)
        print(f"Преподаватель {teacher.name} назначен куратором группы {group.group_id}.")

    def add_group_to_department(self, department: 'Department', group: 'Group'):
        department.add_group(group)
        print(f"Группа {group.group_id} добавлена на кафедру {department.name}.")

    def set_department(self, department: Department):
        self.department = department