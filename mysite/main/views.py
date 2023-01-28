from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.
 
def index(response):
    return render(response, "main/home.html", {})

@login_required(login_url='/login')
def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name = n)
            t.save()
            response.user.todolist.add(t)
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

@login_required(login_url='/login')
def point(response, id):
    ls = ToDoList.objects.get(id=id)
    if ls in response.user.todolist.all():
        if response.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                if len(txt) > 1:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("Invalid")

        return render(response, "main/list.html", {"ls":ls})
    return render(response, "main/view.html", {})


def view(response):
    return render(response, "main/view.html", {})

def v1(response):
    return HttpResponse("<button><a href=/>Home</a></button><h2>View from Vinay Poul</h1></br><a href= /admin>Admin page</a>")

