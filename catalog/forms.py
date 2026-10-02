from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["text", "rating"]

        widgets = {
            "text": forms.Textarea(attrs={
                "placeholder": "Write your review...",
                "rows": 5,
            }),
            "rating": forms.NumberInput(attrs={
                "min": 1,
                "max": 5,
            }),
        }