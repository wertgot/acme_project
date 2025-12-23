from datetime import date
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import BirthdayForm
from .models import Birthday


def calculate_birthday_countdown(birthday):
    today = date.today()
    this_year_birthday = get_birthday_for_year(birthday, today.year)
    if this_year_birthday < today:
        next_birthday = get_birthday_for_year(birthday, today.year + 1)
    else:
        next_birthday = this_year_birthday
    birthday_countdown = (next_birthday - today).days
    return birthday_countdown


def get_birthday_for_year(birthday, year):
    try:
        calculated_birthday = birthday.replace(year=year)
    except ValueError:
        calculated_birthday = date(year=year, month=3, day=1)
    return calculated_birthday


class BirthdayMixin:
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayCreateView(BirthdayMixin, CreateView):
    form_class = BirthdayForm


class BirthdayUpdateView(BirthdayMixin, UpdateView):
    form_class = BirthdayForm


class BirthdayDeleteView(BirthdayMixin, DeleteView):
    pass

class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10
