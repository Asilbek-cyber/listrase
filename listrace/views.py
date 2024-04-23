from django.shortcuts import render

# home_view

def home_view(request):
    return render(request,"index.html")
