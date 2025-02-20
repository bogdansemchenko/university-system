from typing import List,  Dict

class Question:
    def __init__(self, text: str, answers: List[str], correct_answer: int):
        self.text = text
        self.answers = answers
        self.correct_answer = correct_answer  # Теперь это одно число, а не список

    def check_answer(self, user_answer: int) -> bool:
        return user_answer == self.correct_answer

    def __str__(self):
        return f"Вопрос: {self.text}, Ответы: {', '.join(self.answers)}, Правильный ответ: {self.correct_answer}"


class Exam:
    def __init__(self, name: str, subject: str):
        self.name = name
        self.subject = subject
        self.questions: List[Question] = []

    def add_question(self, question: Question):
        self.questions.append(question)

    def conduct_exam(self, student: 'Student') -> 'ExamResult':
        return ExamResult(self, student)

    def __str__(self):
        return f"Экзамен '{self.name}' по предмету '{self.subject}', Вопросов: {len(self.questions)}"


class ExamResult:
    def __init__(self, exam: Exam, student: 'Student'):
        self.exam = exam
        self.student = student
        self.answers: Dict[int, int] = {}
        self.score = 0

    def submit_answer(self, question_num: int, answer: int):
        if 0 <= question_num < len(self.exam.questions):
            self.answers[question_num] = answer

    def calculate_score(self):
        self.score = sum(
            1 for q_num, user_answer in self.answers.items()
            if self.exam.questions[q_num].check_answer(user_answer)
        )

    def __str__(self):
        return f"Результат экзамена: {self.score} правильных ответов из {len(self.exam.questions)}"