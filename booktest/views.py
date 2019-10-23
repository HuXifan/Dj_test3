from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'booktest/index.html')


from django.shortcuts import render_to_response


def page_not_found(request):
    return render_to_response('404page.html')


def page_error(request):
    return render_to_response('500.html')
