from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from typing import List


class QuizResultService():
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto

    def get_result(self, answers: List[AnswerDTO]) -> float:
        points_for_one_question = round(1 / len(self.quiz_dto.questions), 2)
        result = 0
        for question in self.quiz_dto.questions:
            is_correct = False
            true_choices = [choice.uuid for choice in question.choices if choice.is_correct]
            user_answers = [answer.choices[0] for answer in answers if answer.question_uuid == question.uuid]
            if len(true_choices) == len(user_answers):
                for true_choice in true_choices:
                    if true_choice in user_answers:
                        is_correct = True
                    else:
                        is_correct = False
                        break
            if is_correct:
                result += points_for_one_question
        return result
