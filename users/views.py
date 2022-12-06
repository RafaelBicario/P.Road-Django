from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from users.forms import UserForm


class UserCreate(CreateView):
    form_class = UserForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        super().form_valid(form)
        return redirect(reverse('index'))