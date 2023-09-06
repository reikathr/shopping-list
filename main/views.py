from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Athira Reika',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)