from django.shortcuts import render

from .models import Notes

# Create your views here.
def list(request):
    notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': notes})