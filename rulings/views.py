from django.shortcuts import render, get_object_or_404

from .models import Ruling


def show_ruling(request, slug):
    obj = get_object_or_404(Ruling, slug=slug)
    return render(request, 'rulings/show.html', {'object': obj})
