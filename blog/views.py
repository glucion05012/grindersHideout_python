from django.shortcuts import render

def home(request):
	context = {
		'title': 'HOME'
	}
	return render(request, 'blog/home.html', context)
