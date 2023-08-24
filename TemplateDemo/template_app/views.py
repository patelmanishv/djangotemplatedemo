from django.shortcuts import render

def demo_view(request):
    context = {
        'name': 'John',
        'age': 25,
        'numbers': [1, 2, 3, 4, 5],
        'show_numbers': True,
    }
    return render(request, 'template_app/demo_template.html', context)
