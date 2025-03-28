from django.utils.deprecation import MiddlewareMixin

class SecurityHeadersMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response.headers['Content-Security-Policy'] = "default-src 'self'"
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        return response

class ContentSecurityPolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Content-Security-Policy'] = "default-src 'self'"
        return response