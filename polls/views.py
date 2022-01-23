from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Question, Quiz, Choice, Answer, UserProfile
from .forms import GreetingForm, PollsForm
from quiz.services import QuizResultService
from quiz.dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO


class GreetingPageView(View):
    """Представление страницы приветствия"""
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        quiz = Quiz.objects.all().first()
        form = GreetingForm()
        return render(request, 'polls/greeting_page.html', context={
            'form': form,
            'quiz': quiz
        })

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        form = GreetingForm(request.POST)
        if not form.is_valid():
            return render(request, 'polls/greeting_page.html', context={
                'form': form
            })
        else:
            user = UserProfile.objects.create(**form.cleaned_data)
            response = redirect('/polls/1')
            response.set_cookie('id', user.id)
            return response


class DetailQuestion(View):
    """Представление вопроса с формой ответа"""
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        try:
            self.request.COOKIES['id']
        except KeyError:
            return redirect('/polls/')
        question = Question.objects.select_related('quiz').get(id=pk)
        quiz = question.quiz
        form = PollsForm(initial={'text': question.text}, instance=question)
        return render(request, 'polls/question_detail.html', context={
            'form': form,
            'question': question,
            'quiz': quiz
        })

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        user = UserProfile.objects.get(id=self.request.COOKIES['id'])
        question = Question.objects.get(id=pk)
        form = PollsForm(request.POST, instance=question)
        try:
            next_question_id = Question.objects.get(id=(pk + 1)).id
        except Question.DoesNotExist:
            next_question_id = None
        if not form.is_valid():
            return render(request, 'polls/question_detail.html', context={
                'form': form
            })
        else:
            for answer in form.cleaned_data['choices']:
                Answer.objects.create(choice_id=answer.id,
                                      question_id=question.id,
                                      user_id=user.id
                                      )
            if next_question_id is None:
                return redirect('/polls/result/')
            else:
                return redirect(f'/polls/{next_question_id}')


class ResultView(View):
    """Представление для отображения результатов пройденного теста"""
    def get(self, request: HttpRequest) -> HttpResponse:
        user = UserProfile.objects.get(id=self.request.COOKIES['id'])
        quiz = Quiz.objects.all().first()

        question_list = [
            QuestionDTO(uuid=question.uuid, text=question.text, choices=[
                ChoiceDTO(
                    uuid=choice.uuid,
                    text=choice.text,
                    is_correct=choice.is_correct
                )
                for choice in Choice.objects.filter(
                    question_choices__id=question.id
                )
            ]) for question in Question.objects.filter(quiz_id=quiz.id)]

        quiz_dto = QuizDTO(
            uuid=quiz.uuid,
            title=quiz.title,
            questions=question_list
        )

        answers_list = [AnswerDTO(
            question_uuid=answer.question.uuid,
            choices=[answer.choice.uuid]
        ) for answer in Answer.objects.filter(user_id=user.id)]

        answers_dto = AnswersDTO(quiz_uuid=quiz.uuid, answers=answers_list)

        result = QuizResultService(quiz_dto=quiz_dto, answers_dto=answers_dto)
        result_data = result.get_result(result.answers_dto.answers)
        result_data = round(result_data * 100, 2)
        Answer.objects.filter(user_id=user.id).delete()
        return render(request, 'polls/result_page.html', context={
            'result': result_data,
            'quiz': quiz
        })
