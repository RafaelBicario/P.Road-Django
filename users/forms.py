from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field, ButtonHolder, Div, HTML
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django import forms

class UserForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

    # template_name = 'register/register_account.html'
    # success_url = reverse_lazy('index')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.layout = Layout(
            Row(
                Column(Field('first_name', css_class='form-control form-control-user'),
                       css_class='col-lg mb-0'),
                Column(Field('last_name', css_class='form-control form-control-user'),
                       css_class='col-lg mb-0'),
            ),
            Row(Column(Field('email', css_class='form-control form-control-user'),
                       css_class='col-lg mb-0'), ),
            Row(Column(Field('password1', css_class='form-control form-control-user'),
                       css_class='col-lg mb-0'), ),
            Row(Column(Field('password2', css_class='form-control form-control-user'),
                       css_class='col-lg mb-0'), ),
            ButtonHolder(
                Div(
                    HTML("""
                            <button type="submit" class="btn btn-primary btn-user btn-block">
                            Cadastrar
                            </button>
                        """),
                ))

        )