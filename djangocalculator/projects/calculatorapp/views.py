from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'index.html')

def submitquery(request):
    query = request.GET['query']
    try:
        answer = eval(query)
        mydictionary = {
            "q" : query,
            "ans" : answer,
            "error" : False,
            "result" : True
        }
        return render(request,'index.html',context=mydictionary)
    except:
        mydictionary = {
            "error" : True,
            "result" : False

        }
        return render(request,'index.html',context=mydictionary)


        