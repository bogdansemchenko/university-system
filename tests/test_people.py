import unittest


from models.people import *

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student(1, "Иван Иванов", "2000-01-01", True, 8.5)
        self.library = Library()
        self.book1 = Book(1, "Программирование на Python", "Иван Иванов")
        self.library.add_book(self.book1)

    def test_student_creation(self):
        self.assertEqual(self.student.student_id, 1)
        self.assertEqual(self.student.name, "Иван Иванов")
        self.assertEqual(self.student.average_grade, 8.5)

    def test_borrow_book(self):
        self.student.borrow_book_from_library(self.library, 1)
        self.assertIn(self.book1, self.student.borrowed_books)

    def test_return_book(self):
        self.student.borrow_book_from_library(self.library, 1)
        self.student.return_book_to_library(self.library, 1)
        self.assertNotIn(self.book1, self.student.borrowed_books)

class TestDepartmentHead(unittest.TestCase):
    def setUp(self):
        self.department = Department("Программирование")
        self.department_head = DepartmentHead(1, "Анна Петровна", 45, "Программирование")
        self.teacher = Teacher(1, "Иван Иванов", 35, "Программирование")
        self.student1 = Student(1, "Алексей Петров", "2001-02-02", True, 8.0)
        self.student2 = Student(2, "Мария Смирнова", "2002-03-03", False, 5.5)
        self.group = Group(1, )

    def test_assign_scholarships(self):

        self.group.add_student(self.student1)
        self.group.add_student(self.student2)
        self.department.add_group(self.group)
        self.student2.gpa = 3.2
        self.department_head.assign_scholarships(self.department,)
        self.assertEqual(self.student1.scholarship, 180)
        self.assertEqual(self.student2.scholarship, 0)

    def test_hire_teacher(self):
        self.department_head.hire_teacher(self.teacher, self.department)
        self.assertIn(self.teacher, self.department.teachers)

    def test_fire_teacher(self):
        self.department_head.hire_teacher(self.teacher, self.department)
        self.department_head.fire_teacher(self.teacher, self.department)
        self.assertNotIn(self.teacher, self.department.teachers)

    def test_create_curriculum(self):
        curriculum_data = {"Программирование": "8 семестр"}
        self.department_head.create_curriculum(self.department, curriculum_data)
        self.assertEqual(self.department.curriculum, curriculum_data)


class TestTeacher(unittest.TestCase):
    def setUp(self):
        self.teacher = Teacher(1, "Иван Иванов", 35, "Программирование")
        self.exam = Exam("Экзамен по программированию", "Программирование")

    def test_create_exam(self):
        self.assertEqual(self.exam.name, "Экзамен по программированию")
        self.assertEqual(self.exam.subject, "Программирование")

    def test_add_question_to_exam(self):
        question = Question("Что такое Python?", ["Язык программирования", "Фрукты", "Животные"], 0)
        self.teacher.add_question_to_exam(self.exam, question.text, question.answers, [question.correct_answer])
        self.assertEqual(len(self.exam.questions), 1)
        self.assertEqual(self.exam.questions[0].text, "Что такое Python?")
        self.assertEqual(self.exam.questions[0].correct_answer, [0])