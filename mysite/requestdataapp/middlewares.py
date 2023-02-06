import time
from django.http import HttpRequest


def set_useragent_on_request_middleware(get_response):

    print("initial call")

    def middleware(request: HttpRequest):
        print("before get response")
        request.user_agent = request.META["HTTP_USER_AGENT"]
        response = get_response(request)
        print("after get response")
        return response
    return middleware


class CountRequestsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.response_count = 0
        self.exceptions_count = 0
        self.log_ip_dict = {}

    def __call__(self, request: HttpRequest):
        self.requests_count += 1
        print("requests count", self.requests_count)
        ip_address = request.META["REMOTE_ADDR"]
        if ip_address in self.log_ip_dict:
            if self.log_ip_dict[ip_address] > 1:
                if (time.time() - self.log_ip_dict[ip_address]) < 1:
                    print("!!! You make requests very often !!!")
                    # raise ValueError

        response = self.get_response(request)
        self.log_ip_dict[ip_address] = time.time()
        self.response_count += 1
        print("responses count", self.response_count)
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print("got", self.exceptions_count, "exceptions so far")
