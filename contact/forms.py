from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.Form):
    from_name = forms.CharField(max_length=50, required=True)
    from_email = forms.EmailField(max_length=100, required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(max_length=2000, widget=forms.Textarea,
                              required=True)
    helper = FormHelper()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'send_message'

        self.helper.add_input(Submit('submit', 'Send message'))
