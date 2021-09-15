from django.shortcuts import render

def main(request):
	context = {}
	return render(request, 'index.html', context)

def cart(request):
	context = {}
	return render(request, 'cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'checkout.html', context)