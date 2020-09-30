from django.shortcuts import render, redirect
from .models import Shows
from django.contrib import messages

def index(request):
    return redirect('/shows')

def shows(request):
    s=Shows.objects.all()
    context={'shows':s}
    return render(request,'shows.html',context)

def add_show(request):
    e=Shows.objects.validation(request.POST)
    if len(e)>0:
        for j in e.values():
            messages.error(request,j)
        return redirect('../shows/new')
    else:
        Shows.objects.create(
            title=request.POST['title'],
            network=request.POST['net'],
            release_date=request.POST['rdate']
        )
        return redirect('/')

def new_show(request):
    return render(request,'new_show.html')

def edit_show(request,show_id):
    s=Shows.objects.get(id=show_id)
    s.release_date=s.release_date.strftime("%Y-%m-%d")
    context={'show': s}
    return render(request,'edit_show.html',context)

def edit_show_now(request, show_id):
    e=Shows.objects.validation(request.POST)
    newstr="/shows/"+str(show_id)
    if len(e)>0:
        for j in e.values():
            messages.error(request,j)
        return redirect(newstr+'/edit')
    else:
        s=Shows.objects.get(id=show_id)
        s.title=request.POST['title']
        s.network=request.POST['net']
        s.release_date=request.POST['rdate']
        s.description=request.POST['desc']
        s.save()
        return redirect(newstr)

def view_show(request,show_id):
    s=Shows.objects.get(id=show_id)
    context={'show':s}
    return render(request,"view_show.html",context)

def delete(request,show_id):
    s=Shows.objects.get(id=show_id)
    s.delete()
    return redirect('/shows')