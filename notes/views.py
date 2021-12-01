from typing import List
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NotesForm

# Create your views here.
class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'
    login_url = '/login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'
    login_url = '/login'

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
    login_url = '/login'
# def list(request):
#     notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': notes})
class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})
class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'
    login_url = '/login'