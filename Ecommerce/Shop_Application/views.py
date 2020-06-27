from django.shortcuts import render

# Import views
from django.views.generic import ListView, DetailView

# Models
from Shop_Application.models import Product

# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



class Home(ListView):
    model = Product
    template_name = 'Shop_Application/Home.html'

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'Shop_Application/product_detail.html'


def Accessories(request):
	data = 5
	listdata = Product.objects.filter(category=data).order_by('name')
	dic = {'listdata': listdata}
	return render(request,'Shop_Application/Accessories.html',context=dic)


def Clothing(request):
	data = 2
	listdata = Product.objects.filter(category=data).order_by('name')
	dic = {'listdata': listdata}
	return render(request,'Shop_Application/Clothing.html',context=dic)


def EyeWear(request):
	data = 4
	listdata = Product.objects.filter(category=data).order_by('name')
	dic = {'listdata': listdata}
	return render(request,'Shop_Application/EyeWear.html',context=dic)



def Electronics(request):
	data = 1
	listdata = Product.objects.filter(category=data).order_by('name')
	dic = {'listdata': listdata}
	return render(request,'Shop_Application/Electronics.html',context=dic)



def Timepieces(request):
	data = 6
	listdata = Product.objects.filter(category=data).order_by('name')
	dic = {'listdata': listdata}
	return render(request,'Shop_Application/Timepieces.html',context=dic)