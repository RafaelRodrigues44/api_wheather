from django.shortcuts import render

def home(request):
    user = None
    if request.user:
        user = request.user
    return render(request, 'base.html', {'user': user})
