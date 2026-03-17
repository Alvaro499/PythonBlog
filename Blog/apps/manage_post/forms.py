from django import forms
from apps.manage_post.models import Rating

class CommentForm(forms.ModelForm):
    CHOICES = [
        (5, str("5 " + chr(11083))),
        (4, str("4 " + chr(11083))),
        (3, str("3 " + chr(11083))),
        (2, str("2 " + chr(11083))),
        (1, str("1 " + chr(11083)))
    ]

    value = forms.ChoiceField(label="Calification",
                              choices=CHOICES,
                              widget=forms.RadioSelect())

    class Meta:
        model = Rating
        fields = [
            'value',
            'description'
        ]