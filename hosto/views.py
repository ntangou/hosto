from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def index(request):
    return render(request, 'pages/index.html')


@cache_page(60 * 15)
def apropos(request):
    return render(request, 'pages/apropos.html')


@cache_page(60 * 15)
def contact(request):
    return render(request, 'pages/contact.html')


@cache_page(60 * 15)
def handler404(request, exception):
    return render(request, 'erreurs/400.html', {'error': exception}, status=400)


@cache_page(60 * 15)
def handler404(request, exception):
    return render(request, 'erreurs/403.html', {'error': exception}, status=403)

@cache_page(60 * 15)
def handler404(request, exception):
    return render(request, 'erreurs/404.html', {'error': exception}, status=404)

@cache_page(60 * 15)
def handler404(request, exception):
    return render(request, 'erreurs/500.html', {'error': exception}, status=500)