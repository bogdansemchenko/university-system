from university_storage import *
from menu import *


def main():
    filename = 'university_state.pkl'
    university = UniversityStorage.load(filename)

    if not university:
        print("Создание нового университета...")
        university = University(name="БГУИР")
        fitu_faculty = Faculty(name="ФИТУ")
        university.faculties.append(fitu_faculty)
        iit_department = Department(name="ИИТ")
        fitu_faculty.departments.append(iit_department)
        head = DepartmentHead(
            teacher_id = 1,
            name = "Шункевич Даниил Вячеславович",
            age = 40,
            subject = "МОИС"
        )
        head.set_department(iit_department)
        iit_department.add_teacher(head)
        iit_department.set_head(head)

        teacher = Teacher(
            teacher_id = 2,
            name = "Зотов Никита Владимирович",
            age = 22,
            subject = "ППОИС"
        )
        iit_department.add_teacher(teacher)

        # Создаем группу и студента
        group = Group(group_id = 321703)
        student = Student(
            student_id = 1,
            name = "Грибанов Егор Владимирович",
            birth_date = "01.01.2000",
            is_budget = False,
            average_grade = 6
        )
        group.add_student(student)
        iit_department.add_group(group)

        UniversityStorage.save(university, filename)
    else:
        print("\nЗагружены сохраненные данные университета!")
        fitu_faculty = university.faculties[0] if university.faculties else None
        iit_department = fitu_faculty.departments[0] if fitu_faculty else None
        head = iit_department.head if iit_department else None
        teacher = next((t for t in iit_department.teachers if t.teacher_id == 2), None) if iit_department else None
        group = iit_department.groups[0] if iit_department else None
        student = group.students[0] if group else None


    main_menu = MainMenu(university, head, teacher, student)
    main_menu.run()
    UniversityStorage.save(university, filename)
    print("Состояние университета сохранено!")


if __name__ == "__main__":
    main()