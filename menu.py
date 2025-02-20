from models.people import *
from validator import Validator
from models.library import Book

class Menu(ABC):
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def handle_choice(self, choice: str):
        pass

    def run(self):
        while True:
            self.display()
            choice = input("Выберите действие: ")
            result = self.handle_choice(choice)
            if result == "exit":
                break

class MainMenu(Menu):
    def __init__(self, university: University, head: DepartmentHead, teacher: Teacher, student: Student):
        self.university = university
        self.head = head
        self.teacher = teacher
        self.student = student

    def display(self):
        print("\nГлавное меню:")
        print("1. Создать факультет и добавить в университет")
        print("2. Посмотреть информацию об университете")
        print("3. Посмотреть информацию о факультете")
        print("4. Посмотреть список книг в библиотеке")
        print("5. Добавить книгу в библиотеку")
        print("6. Добавить кафедру на факультет")
        print("7. Войти как заведующий кафедрой")
        print("8. Создать экзамен (как преподаватель)")
        print("9. Войти как студент")
        print("10. Выйти")

    def handle_choice(self, choice: str):
        if choice == "1":
            self.create_faculty()
        elif choice == "2":
            self.show_university_info()
        elif choice == "3":
            self.show_faculty_info()
        elif choice == "4":
            self.show_books()
        elif choice == "5":
            self.add_book()
        elif choice == "6":
            self.add_department()
        elif choice == "7":
            DepartmentHeadMenu(self.head).run()
        elif choice == "8":
            self.create_exam()
        elif choice == "9":
            StudentMenu(self.student, self.university).run()
        elif choice == "10":
            return "exit"
        else:
            print("Неверный выбор!")
        return None

    def create_faculty(self):
        faculty_name = Validator.validate_string("Введите название факультета: ")
        new_faculty = Faculty(faculty_name)
        self.university.faculties.append(new_faculty)
        print(f"Факультет '{faculty_name}' создан и добавлен в университет.")

    def show_university_info(self):
        print("\nИнформация об университете:")
        print(self.university)
        print("Факультеты:")
        for faculty in self.university.faculties:
            print(f"- {faculty.name}")

    def show_faculty_info(self):
        faculty = Validator.validate_in_list(
            "Введите название факультета: ",
            self.university.faculties
        )
        print(f"\nИнформация о факультете {faculty.name}:")
        print(f"Кафедры: {[d.name for d in faculty.departments]}")

    def show_books(self):
        print("\nСписок книг в библиотеке:")
        for book in self.university.library.books:
            print(f"ID: {book.book_id}, Название: {book.title}, Автор: {book.author}")

    def add_book(self):
        book_id = Validator.validate_integer("Введите ID книги: ")
        if any(b.book_id == book_id for b in self.university.library.books):
            print("Книга с таким ID уже существует!")
            return
        title = Validator.validate_non_empty("Введите название книги: ")
        author = Validator.validate_string("Введите автора книги: ")
        new_book = Book(book_id, title, author)
        self.university.library.add_book(new_book)
        print(f"Книга '{title}' добавлена в библиотеку.")

    def add_department(self):
        department_name = Validator.validate_string("Введите название кафедры: ")
        faculty = Validator.validate_in_list(
            "Введите название факультета: ",
            self.university.faculties
        )
        new_department = Department(department_name)
        faculty.departments.append(new_department)
        print(f"Кафедра '{department_name}' добавлена на факультет '{faculty.name}'.")

    def create_exam(self):
        exam_name = Validator.validate_non_empty("Введите название экзамена: ")
        exam = self.teacher.create_exam(exam_name)

        while True:
            question_text = Validator.validate_non_empty("\nВведите текст вопроса (или 'готово'): ").lower()
            if question_text == 'готово':
                break

            answers = []
            num_answers = Validator.validate_integer("Количество вариантов ответов: ")
            for i in range(num_answers):
                answers.append(Validator.validate_non_empty(f"Вариант {i + 1}: "))

            correct = Validator.validate_integer("Номер правильного ответа: ")
            while correct < 1 or correct > num_answers:
                print(f"Ошибка: выберите номер от 1 до {num_answers}")
                correct = Validator.validate_integer("Номер правильного ответа: ")

            self.teacher.add_question_to_exam(exam, question_text, answers, correct - 1)

        department = self.head.department
        department.add_exam(exam)
        print(f"Экзамен '{exam_name}' создан!")

class DepartmentHeadMenu(Menu):
    def __init__(self, department_head: DepartmentHead):
        self.department_head = department_head

    def display(self):
        print("\nМеню заведующего кафедрой:")
        print("1. Посмотреть группы")
        print("2. Добавить группу")
        print("3. Добавить студента")
        print("4. Составить учебный план")
        print("5. Начислить стипендии")
        print("6. Нанять преподавателя")
        print("7. Уволить преподавателя")
        print("8. Список преподавателей")
        print("9. Назначить куратора")
        print("10. Информация о кафедре")
        print("11. Назад")

    def handle_choice(self, choice: str):
        if choice == "1":
            self.show_groups()
        elif choice == "2":
            self.add_group()
        elif choice == "3":
            self.add_student()
        elif choice == "4":
            self.create_curriculum()
        elif choice == "5":
            self.assign_scholarships()
        elif choice == "6":
            self.hire_teacher()
        elif choice == "7":
            self.fire_teacher()
        elif choice == "8":
            self.show_teachers()
        elif choice == "9":
            self.set_curator()
        elif choice == "10":
            self.view_department_info()
        elif choice == "11":
            return "exit"
        else:
            print("Неверный выбор. Попробуйте снова.")
        return None

    def show_groups(self):
        print("\nСписок групп на кафедре:")
        if not self.department_head.department.groups:
            print("Группы отсутствуют")
            return

        for group in self.department_head.department.groups:
            print(f"\nГруппа ID: {group.group_id}")
            print(f"Куратор: {group.curator.name if group.curator else 'Не назначен'}")
            print("Студенты:")
            for student in group.students:
                print(f"- {student.name} (ID: {student.student_id}, Средний балл: {student.average_grade}, Статус: {'Бюджет' if student.is_budget else 'Контракт'})")

    def add_group(self):
        group_id = Validator.validate_integer("Введите ID новой группы: ")
        if any(g.group_id == group_id for g in self.department_head.department.groups):
            print("Группа с таким ID уже существует!")
            return

        new_group = Group(group_id)
        self.department_head.department.add_group(new_group)
        print(f"Группа {group_id} успешно добавлена на кафедру {self.department_head.department.name}.")

    def add_student(self):
        group_id = Validator.validate_integer("Введите ID группы для добавления студента: ")
        group = next((g for g in self.department_head.department.groups if g.group_id == group_id), None)
        if not group:
            print(f"Группа с ID {group_id} не найдена")
            return

        student_name = Validator.validate_string("Введите ФИО студента: ")
        birth_date = Validator.validate_date("Дата рождения (ДД.ММ.ГГГГ): ")
        is_budget = Validator.validate_boolean("Бюджетное обучение? (да/нет): ")
        avg_grade = Validator.validate_float("Средний балл: ")

        new_student = Student(
            student_id=len(group.students) + 1,
            name=student_name,
            birth_date=birth_date,
            is_budget=is_budget,
            average_grade=avg_grade
        )

        group.add_student(new_student)
        print(f"Студент {student_name} успешно добавлен в группу {group_id}")

    def create_curriculum(self):
        try:
            curriculum_input = input("Введите учебный план в формате словаря (предмет: часы): ")
            curriculum = eval(curriculum_input)

            if not isinstance(curriculum, dict):
                raise ValueError("Некорректный формат данных")

            self.department_head.create_curriculum(self.department_head.department, curriculum)
            print("Учебный план успешно обновлен!")

        except Exception as e:
            print(f"Ошибка при создании учебного плана: {str(e)}")
            print("Пример правильного формата: {'Математика': 120, 'Физика': 90}")

    def assign_scholarships(self):
        try:
            self.department_head.assign_scholarships(self.department_head.department)
            print("Стипендии успешно начислены!")
        except Exception as e:
            print(f"Ошибка при начислении стипендий: {str(e)}")

    def hire_teacher(self):
        name = Validator.validate_string("Введите ФИО преподавателя: ")
        teacher_id = Validator.validate_integer("Введите ID преподавателя: ")
        if any(t.teacher_id == teacher_id for t in self.department_head.department.teachers):
            print("Преподаватель уже работает на кафедре!")
            return
        age = Validator.validate_choice("Введите возраст (от 21 до 70): ")
        subject = Validator.validate_string("Введите преподаваемый предмет: ")

        new_teacher = Teacher(teacher_id, name, age, subject)
        self.department_head.hire_teacher(new_teacher, self.department_head.department)
        print(f"Преподаватель {name} успешно принят на работу!")

    def fire_teacher(self):
        name = Validator.validate_string("Введите ФИО преподавателя для увольнения: ")
        teacher = next((t for t in self.department_head.department.teachers if t.name == name), None)

        if teacher:
            self.department_head.fire_teacher(teacher, self.department_head.department)
            print(f"Преподаватель {name} уволен с кафедры")
        else:
            print("Преподаватель не найден")

    def show_teachers(self):
        print("\nСписок преподавателей кафедры:")
        if not self.department_head.department.teachers:
            print("Преподаватели отсутствуют")
            return

        for teacher in self.department_head.department.teachers:
            print(f"- {teacher.name} (ID: {teacher.teacher_id}, Предмет: {teacher.subject})")

    def set_curator(self):
        teacher_name = Validator.validate_string("Введите ФИО преподавателя: ")
        teacher = next((t for t in self.department_head.department.teachers if t.name == teacher_name), None)
        if not teacher:
            print("Преподаватель не найден")
            return

        group_id = Validator.validate_integer("Введите ID группы: ")
        group = next((g for g in self.department_head.department.groups if g.group_id == group_id), None)
        if group:
            self.department_head.set_curator_for_group(group, teacher)
        else:
            print("Группа не найдена")

    def view_department_info(self):
        print("\nИнформация о кафедре:")
        print(f"Название: {self.department_head.department.name}")
        print(f"Заведующий: {self.department_head.name}")
        print(f"Количество групп: {len(self.department_head.department.groups)}")
        print(f"Количество преподавателей: {len(self.department_head.department.teachers)}")
        if self.department_head.department.curriculum:
            print("\nУчебный план:")
            for subject, hours in self.department_head.department.curriculum.items():
                print(f"- {subject}: {hours} часов")
        else:
            print("Учебный план не установлен")



class StudentMenu(Menu):
    def __init__(self, student: Student, university: University):
        self.student = student
        self.university = university

    def display(self):
        print("\nМеню студента:")
        print("1. Взять книгу из библиотеки")
        print("2. Вернуть книгу в библиотеку")
        print("3. Посмотреть мои книги")
        print("4. Сдать экзамен")
        print("5. Вернуться в главное меню")

    def handle_choice(self, choice: str):
        if choice == "1":
            book_id = Validator.validate_integer("Введите ID книги: ")
            self.student.borrow_book_from_library(self.university.library, book_id)

        elif choice == "2":
            book_id = Validator.validate_integer("Введите ID книги: ")
            self.student.return_book_to_library(self.university.library, book_id)

        elif choice == "3":
            print("\nВаши книги:")
            for book in self.student.borrowed_books:
                print(f"- {book.title} (ID: {book.book_id})")
            if not self.student.borrowed_books:
                print("У вас нет взятых книг")

        elif choice == "4":
            if not self.student.group or not self.student.group.department:
                print("Студент не привязан к кафедре!")
                return

            department = self.student.group.department
            exam = self.student.choose_exam(department)

            if exam:
                result = exam.conduct_exam(self.student)
                print(f"\nЭкзамен: {exam.name}")

                for q_num, question in enumerate(exam.questions):
                    print(f"\nВопрос {q_num + 1}: {question.text}")
                    for i, answer in enumerate(question.answers):
                        print(f"{i + 1}. {answer}")

                    answer = Validator.validate_integer("Номер правильного ответа: ")
                    while answer < 1 or answer > len(question.answers):
                        print(f"Ошибка: выберите номер от 1 до {len(question.answers)}")
                        answer = Validator.validate_integer("Номер правильного ответа: ")

                    result.submit_answer(q_num, answer - 1)

                result.calculate_score()
                print(f"\nРезультат: {result.score}/{len(exam.questions)}")

        elif choice == "5":
            return "exit"

        else:
            print("Неверный выбор!")
        return None