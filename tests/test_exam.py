import unittest
from models.exam import Exam, Question, ExamResult


class TestQuestion(unittest.TestCase):
    def setUp(self):
        self.question = Question("2 + 2?", ["3", "4", "5"], 1)
    def test_check_answer_correct(self):
        self.assertTrue(self.question.check_answer(1))
    def test_check_answer_incorrect(self):
        self.assertFalse(self.question.check_answer(0))
    def test_check_answer_out_of_range(self):
        self.assertFalse(self.question.check_answer(5))

class TestExam(unittest.TestCase):
    def setUp(self):
        self.exam = Exam("Математика", "Математика")
        self.question1 = Question("Что такое 2 + 2?", ["3", "4", "5"], 1)
        self.question2 = Question("Что такое 3 + 3?", ["5", "6", "7"], 1)
        self.exam.add_question(self.question1)
        self.exam.add_question(self.question2)

    def test_exam_creation(self):
        self.assertEqual(self.exam.name, "Математика")
        self.assertEqual(self.exam.subject, "Математика")
        self.assertEqual(len(self.exam.questions), 2)

    def test_add_question(self):
        question3 = Question("Что такое 5 + 5?", ["8", "9", "10"], 2)
        self.exam.add_question(question3)
        self.assertEqual(len(self.exam.questions), 3)


class TestExamResult(unittest.TestCase):
    def setUp(self):
        self.exam = Exam("Математика", "Математика")
        self.question1 = Question("Что такое 2 + 2?", ["3", "4", "5"], 1)
        self.question2 = Question("Что такое 3 + 3?", ["5", "6", "7"], 1)
        self.exam.add_question(self.question1)
        self.exam.add_question(self.question2)
        self.student = "Иван"  # Простой пример студента
        self.exam_result = ExamResult(self.exam, self.student)

    def test_exam_result_creation(self):
        self.assertEqual(self.exam_result.exam, self.exam)
        self.assertEqual(self.exam_result.student, self.student)
        self.assertEqual(len(self.exam_result.answers), 0)

    def test_submit_answer(self):
        self.exam_result.submit_answer(0, 1)
        self.assertEqual(self.exam_result.answers[0], 1)

    def test_calculate_score(self):
        self.exam_result.submit_answer(0, 1)
        self.exam_result.submit_answer(1, 1)
        self.exam_result.calculate_score()
        self.assertEqual(self.exam_result.score, 2)