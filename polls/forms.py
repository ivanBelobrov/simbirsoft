from django import forms
from .models import UserProfile, Question, Choice


class GreetingForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class PollsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choices'].queryset = Choice.objects.filter(
            question_choices__id=self.instance.pk
        )
        self.initial['choices'] = [
            False for _ in self.fields['choices'].queryset
        ]

    class Meta:
        model = Question
        fields = ('choices',)
        widgets = {
            'choices': forms.CheckboxSelectMultiple()
        }
