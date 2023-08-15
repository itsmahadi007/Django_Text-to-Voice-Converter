from bark import preload_models


class AudioModelPreloadMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        preload_models()

    def __call__(self, request):
        response = self.get_response(request)
        return response
