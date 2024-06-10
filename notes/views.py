from typing import Any
from django.http.response import HttpResponseRedirect
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin 

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
    login_url = "/admin"


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Snote
    success_url = '/sticky/notes'
    form_class = NotesForm
    login_url = "/admin"

    def form_valid(self, form): 
         self.object = form.save(commit=False)
         self.object.user = self.request.user
         self.object.save()
         return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
    model = Snote
    context_object_name = "notes"
    template_name="notes/snote_list.html"
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(DetailView):
    model = Snote
    context_object_name = "note"
    
def detail(request, pk):
    try:
        note=Snote.objects.get(pk=pk)
    except Snote.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/snote_detail.html', {'note': note})