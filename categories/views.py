from django.shortcuts import render

# Create your views here.
def category(request):
    return render(request, 'add_category.html')