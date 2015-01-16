from .conf import settings

class TemporaryMiddleware(object):

    def process_request(self, request):
        if not settings.TEMPORARY_SESSION_KEY in request.session:
            request.session[settings.TEMPORARY_SESSION_KEY] = []

        return None
