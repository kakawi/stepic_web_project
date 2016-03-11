from django import forms

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    question = forms.IntegerField()
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer