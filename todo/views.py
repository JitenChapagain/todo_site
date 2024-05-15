from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages

from .forms import TodoForm
from .forms import Todo

# Create your views here.
def index(request):
    item_list = Todo.objects.order_by("date")
    if request.method =="POST":
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title":"TODO LIST"
    }
    return render (request, 'index.html',page)

def remove(request, item_id):
    item =Todo.objects.get(id=item_id)
    a=item.title
    item.delete()
    messages.info(request,a+ "removed !!!!!!")
    return redirect('todo')