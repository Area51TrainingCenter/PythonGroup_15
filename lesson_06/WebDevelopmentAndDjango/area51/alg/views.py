from django.http import HttpResponse


def fibonacci(request, num):
    return HttpResponse(fibo(int(num)))


def fibo(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    return fibo(num - 1) + fibo(num - 2)
