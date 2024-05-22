from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

from .models import Meeting, Room
from .forms import MeetingForm

@login_required
def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id, user=request.user)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def rooms_list(request):
    return render(request, "meetings/rooms_list.html", 
                  {"rooms": Room.objects.all()})

@login_required
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.user = request.user
            meeting.save()
            return redirect("home")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})

class MeetingUpdateView(UpdateView):
    model = Meeting
    fields = ['title', 'date', 'start_time', 'duration', 'room', 'comment']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('meetings')

class MeetingDeleteView(DeleteView):
    model = Meeting
    success_url = reverse_lazy('meetings')