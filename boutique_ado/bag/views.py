from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ View to show the shopping bag """
    return render(request, 'bag/bag.html')

