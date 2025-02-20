from models.exam import Exam
from models.library import *



class Group:
    def __init__(self, group_id: int):
        self.group_id = group_id
        self.students: List['Student'] = []
        self.department: Optional['Department'] = None
        self.curator: Optional['Teacher'] = None

    def set_department(self, department: 'Department'):
        self.department = department

    def add_student(self, student: 'Student'):
        if student not in self.students:
            self.students.append(student)
            student.group = self

    def remove_student(self, student: 'Student'):
        if student in self.students:
            self.students.remove(student)
            student.group = None

    def set_curator(self, curator: 'Teacher'):

        self.curator = curator

    def __str__(self):
        return f"Группа ID: {self.group_id}, Студентов: {len(self.students)}, Куратор: {self.curator.name if self.curator else 'Не назначен'}"



class Department:
    def __init__(self, name: str):
        self.name = name
        self.groups: List[Group] = []
        self.teachers: List['Teacher'] = []
        self.head: Optional['DepartmentHead'] = None
        self.exams: List[Exam] = []
        self.curriculum: dict = {}

    def add_exam(self, exam: Exam):
        self.exams.append(exam)

    def get_exam(self, exam_name: str) -> Optional[Exam]:
        for exam in self.exams:
            if exam.name == exam_name:
                return exam
        return None

    def add_group(self, group: Group):
        self.groups.append(group)
        group.set_department(self)

    def set_head(self, head: 'DepartmentHead'):
        if head not in self.teachers:
            raise ValueError("Head must be a member of department teachers")
        self.head = head

    def add_teacher(self, teacher: 'Teacher'):
        self.teachers.append(teacher)

    def view_department_info(self):
        print("\nИнформация о кафедре:")
        print(f"Название кафедры: {self.name}")
        print(f"Заведующий кафедрой: {self.head.name if self.head else 'Не назначен'}")
        print("\nПреподаватели:")
        if self.teachers:
            for teacher in self.teachers:
                print(f"- {teacher.name}")
        else:
            print("Преподавателей пока нет.")

        print("\nУчебный план:")
        if self.curriculum:
            for subject, hours in self.curriculum.items():
                print(f"- {subject}: {hours} часов")
        else:
            print("Учебный план еще не составлен.")

        print("\n")


class Faculty:
    def __init__(self, name: str):
        self.name = name
        self.departments: List[Department] = []

    def __str__(self):
        return f"Факультет: {self.name}, Количество кафедр: {len(self.departments)}"

class University:
    def __init__(self, name: str):
        self.name = name
        self.faculties: List[Faculty] = []
        self.library = Library()
        self.departments = []

    def __str__(self):
        return f"Университет: {self.name}, Количество факультетов: {len(self.faculties)}"

    def add_department(self, department_name):
        self.departments.append(department_name)