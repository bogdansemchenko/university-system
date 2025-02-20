import unittest
from models.people import *

class TestGroup(unittest.TestCase):
    def setUp(self):
        self.group = Group(1)
        self.student1 = Student(1, "Алексей Петров", "2001-02-02", True, 8.0)
        self.student2 = Student(2, "Мария Смирнова", "2002-03-03", False, 5.5)
        self.teacher = Teacher(1, "Иван Иванов", 35, "Программирование")
        self.department = Department("Программирование")
        self.group.add_student(self.student1)
        self.group.add_student(self.student2)

    def test_add_student(self):
        self.assertEqual(len(self.group.students), 2)
        self.assertEqual(self.student1.group, self.group)
        self.assertEqual(self.student2.group, self.group)

    def test_remove_student(self):
        self.group.remove_student(self.student1)
        self.assertEqual(len(self.group.students), 1)
        self.assertIsNone(self.student1.group)

    def test_set_curator(self):
        self.group.set_curator(self.teacher)
        self.assertEqual(self.group.curator, self.teacher)


class TestDepartment(unittest.TestCase):
    def setUp(self):
        self.department = Department("Программирование")
        self.teacher = Teacher(1, "Иван Иванов", 35, "Программирование")
        self.department_head = DepartmentHead(1, "Анна Петровна", 45, "Программирование")
        self.student1 = Student(1, "Алексей Петров", "2001-02-02", True, 8.0)
        self.student2 = Student(2, "Мария Смирнова", "2002-03-03", False, 5.5)
        self.group = Group(1)
        self.group.add_student(self.student1)
        self.group.add_student(self.student2)

    def test_add_teacher(self):
        self.department.add_teacher(self.teacher)
        self.assertIn(self.teacher, self.department.teachers)

    def test_set_head(self):
        self.department.add_teacher(self.department_head)
        self.department.set_head(self.department_head)
        self.assertEqual(self.department.head, self.department_head)

    def test_add_group(self):
        self.department.add_group(self.group)
        self.assertIn(self.group, self.department.groups)




class TestUniversity(unittest.TestCase):
    def setUp(self):
        self.university = University("Технический Университет")
        self.faculty = Faculty("Информационные технологии")
        self.department = Department("Программирование")
        self.group = Group(1)
        self.student1 = Student(1, "Алексей Петров", "2001-02-02", True, 8.0)
        self.student2 = Student(2, "Мария Смирнова", "2002-03-03", False, 5.5)
        self.group.add_student(self.student1)
        self.group.add_student(self.student2)

    def test_add_faculty(self):
        self.university.faculties.append(self.faculty)
        self.assertIn(self.faculty, self.university.faculties)

    def test_add_department_to_faculty(self):
        self.faculty.departments.append(self.department)
        self.assertIn(self.department, self.faculty.departments)

    def test_add_group_to_department(self):
        self.department.add_group(self.group)
        self.assertIn(self.group, self.department.groups)

    def test_university_str(self):
        self.university.faculties.append(self.faculty)
        self.assertEqual(str(self.university), "Университет: Технический Университет, Количество факультетов: 1")
