from django.shortcuts import render

# Create your views here.


def indexPageView(request) :
    return render(request, 'MP_Table/index.html',)  

def postPageView(request) :
    return render(request, 'MP_Table/post.html',)

def aboutPageView(request):
    return render(request, 'MP_Table/about.html',)

