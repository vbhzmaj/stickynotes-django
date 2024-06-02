from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Snote

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