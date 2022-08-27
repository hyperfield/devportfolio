from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your name"
        })
    )
    comment = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={
            "rows": 5, "cols": 10,
            "class": "form-control",
            "placeholder": "Post a comment"
        })
    )
    helper = FormHelper()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-comment_form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'post_comment'

        self.helper.add_input(Submit('submit', 'Post comment'))
