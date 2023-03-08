from django import forms
from .models import *


class ReviewForm(forms.ModelForm):
    """
    Review form with custom empty label
    Add review author or none (current_user) from args
    """
    def __init__(self, current_user, *args, **kwargs):
        self.current_user = current_user
        super().__init__(*args, **kwargs)
        self.fields['city'].empty_label = 'Выберите город'
        self.fields['specialization'].empty_label = 'Выберите тип'

    def save(self, *args, **kwargs):
        self.instance.review_author = self.current_user
        return super().save(*args, **kwargs)

    class Meta:
        model = MainContentReview
        fields = ['city', 'specialization', 'review_content']
        widgets = {
            'review_content': forms.Textarea(attrs={'cols': 60, 'rows': 5})
        }


class ReviewAnswerFormContent(forms.Form):
    """
    Form to send only content to action url from all reviews list
    """
    answer_content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}),
                                     label="Ответ", required=True, min_length=10)


class ReviewAnswerForm(forms.ModelForm):
    """
    Review answer form for save user review reply
    """
    class Meta:
        model = MainContentReviewAnswer
        fields = ['review_author', 'answer_content', 'review']
