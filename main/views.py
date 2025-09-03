from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406401193',
        'name': 'Ilham Shahputra Hasim',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
