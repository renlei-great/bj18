from django.http import HttpResponse


def index(request):
	return HttpRseponse('弟弟')


def login(request):
	return HttpRseponse('成功')
