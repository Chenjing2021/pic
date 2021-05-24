from django.shortcuts import render
from .models import *


def picture(request):
	products = Item.objects.all()
	context = {'products': products}
	return render(request, 'store/picture.html', context)