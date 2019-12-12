from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo,HeroInfo

# Create your views here.

def books(request):
    books = BookInfo.objects.all()
    # return render(request, 'booktest/books.html', {'books':books()})
    return HttpResponse("成功")





