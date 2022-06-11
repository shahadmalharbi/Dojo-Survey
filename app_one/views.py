from django.shortcuts import render, redirect
def index(request):
    return render(request,'index.html')

def result(request):
    print("Got Post Info....................")
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    comment = request.POST['comment']
    context = {
    	"name" : name,
    	"location" : location,
        "language" : language,
        "comment": comment
    }
    return render(request,"info.html",context)
