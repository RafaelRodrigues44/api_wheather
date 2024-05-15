from django.shortcuts import render

def home(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    return render(request, 'base.html', {'user': user})
