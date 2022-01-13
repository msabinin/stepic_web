from django.http import HttpResponse

def return_ok(request):
    return HttpResponse('OK')
