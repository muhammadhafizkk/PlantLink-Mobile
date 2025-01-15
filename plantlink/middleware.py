class XFrameOptionsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Content-Security-Policy'] = "frame-ancestors 'self' http://localhost:8000 https://989b-2405-3800-8bb-a348-d1ed-f1e4-4aa7-4c15.ngrok-free.app https://27.125.250.42 http://127.0.0.1:8000 http://52.64.72.29:8000"
        return response