import time

from django.http import HttpRequest
from django.shortcuts import render


class ThrottlingMiddleware:
    def __init__(self, get_responce):
        self.get_responce = get_responce
        self.request_count = 0
        self.responses_count = 0
        self.request_time = {}
    def __call__(self, request: HttpRequest):
        time_delay = 0.1
        if not self.request_time:
            print('This is first request')
        elif time.time() - self.request_time['time'] < time_delay and \
                    self.request_time['ip-address'] == request.META.get('REMOTE_ADDR'):
            print('Error time request')
            return render(request, 'requestdataapp/error-request.html')
        self.request_time = {'time': time.time(), 'ip-address': request.META.get('REMOTE_ADDR')}
        responce = self.get_responce(request)
        return responce
