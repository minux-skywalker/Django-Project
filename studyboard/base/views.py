from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse('HomePage')

# def room(request):
#     return HttpResponse('ROOM')

rooms=[
    {'id':1, 'name':'Let\'s learn python!' },
    {'id':1, 'name':'Design the UX!' },
    {'id':1, 'name':'Learn MERN Stack!' },
]

def home(request):
    context={'rooms':rooms}
    return render(request,'base/home.html', context)

def room(request):
    return render(request, 'base/room.html')