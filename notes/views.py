from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Note
# Create your views here.



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('note_list')
    else:
        form = UserCreationForm()

    return render(request, 'notes/register.html', {'form': form})

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})

@login_required
def add_note(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        Note.objects.create(
            user=request.user,
            title=title,
            content=content
        )
        return redirect('note_list')

    return render(request, 'notes/add_note.html')

@login_required
def delete_note(request, id):
    note = Note.objects.get(id=id, user=request.user)
    note.delete()
    return redirect('note_list')

@login_required
def edit_note(request, id):
    note = Note.objects.get(id=id, user=request.user)

    if request.method == "POST":
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('note_list')

    return render(request, 'notes/edit_note.html', {'note': note})