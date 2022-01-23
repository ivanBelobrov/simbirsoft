from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Choice(models.Model):
    uuid = models.CharField(
        max_length=16,
        null=True,
        verbose_name='Идентификатор'
    )
    text = models.CharField(
        max_length=100,
        verbose_name='Текст ответа'
    )
    is_correct = models.BooleanField(
        verbose_name='Это правильный ответ?'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Текст ответа'
        verbose_name_plural = 'Текст ответов'


class Quiz(models.Model):
    uuid = models.CharField(
        max_length=16,
        null=True,
        verbose_name='Идентификатор'
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Название'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    uuid = models.CharField(
        max_length=16,
        null=True,
        verbose_name='Идентификатор'
    )
    text = models.TextField(
        verbose_name='Описание вопроса'
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.DO_NOTHING,
        related_name='question_quiz'
    )
    choices = models.ManyToManyField(
        Choice,
        related_name='question_choices',
        verbose_name='Варианты ответа'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.DO_NOTHING,
        related_name='answer_question'
    )
    choice = models.ForeignKey(
        Choice,
        on_delete=models.DO_NOTHING,
        related_name='answer_choice'
    )
    user = models.ForeignKey(
        UserProfile,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name='answer_user'
    )

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'



