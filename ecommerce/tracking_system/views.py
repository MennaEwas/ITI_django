from django.shortcuts import render

# endpoint 
def home(request):
    return render(request=request, template_name="home.html")
