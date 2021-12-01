from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView
from .models import Notes
from .forms import NotesForm

# Create your views here.
class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

# def list(request):
#     notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': notes})
class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'