from django.shortcuts import render 

def home(request):
    context = {
        'title': 'Home Page',
        'message': 'Welcome to the Home Page!',

        'data': {
            'name': 'Muhammad Umair 😎',
            'age': 20,
            'skills' : 'Python 🐍, SQL 📅',
            'city': 'Karachi - '
        }
    }
    if request.method == "POST":
        print(request.POST)
    
    return render(request, 'home.html', context)