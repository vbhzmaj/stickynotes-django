from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

from .forms import NotesForm
from .models import Snote

class NotesDeleteView(DeleteView):
    model = Snote
    success_url = '/sticky/notes'
    template_name='notes/snote_delete.html'

class NotesUpdateView(UpdateView):
    model = Snote
    success_url = '/sticky/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Snote
    success_url = '/sticky/notes'
    form_class = NotesForm

class NotesListView(ListView):
    model = Snote
    context_object_name = "notes"
    template_name="notes/snote_list.html"


class NotesDetailView(DetailView):
    model = Snote
    context_object_name = "note"
    
def detail(request, pk):
    try:
        note=Snote.objects.get(pk=pk)
    except Snote.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})