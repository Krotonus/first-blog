from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')
	
def contact(request):
	return render(request,'personal/basic.html', {'content':['This is how you can contact me.','lalithm.work@gmail.com']})