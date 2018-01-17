from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #Construct a dictionary to pass to the template engine its context
	#Note the key boldmessage is the same as {{boldmessage}} in the template!
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candym cupcake!"}
	
	return render(request, 'rango/index.html', context=context_dict)
	
