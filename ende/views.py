from django.shortcuts import render

def ende_page(request):
    return render(request, 'ende/ende_page.html', {})
