from prometheus_client import Counter, Histogram
import time

REQUESTS_TOTAL = Counter('http_requests_total', 'Total HTTP Requests')
REQUESTS_LATENCY = Histogram('http_request_latency_seconds', 'HTTP request latency')

class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        latency = time.time() - start_time

        REQUESTS_TOTAL.inc()
        REQUESTS_LATENCY.observe(latency)
        
        # Track additional metrics
        if hasattr(request, 'user') and request.user.is_authenticated:
            user_type = request.user.user_type
            REQUESTS_TOTAL.labels(
                method=request.method,
                path=request.path,
                user_type=user_type
            ).inc()

        return response