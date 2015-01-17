
from .conf import settings
from .models import Temporary
from .utils import get_ip


class TemporaryFormMixin(object):

    request = None
    
    def __init__(self, request, *args, **kwargs):
        super(TemporaryFormMixin, self).__init__(*args, **kwargs)
        self.request = request

        if not self.request.session.session_key:
            self.request.session.save()
    
    def save(self, *args, **kwargs):
        obj = super(TemporaryFormMixin, self).save(*args, **kwargs)
        
        obj.session_key = self.request.session.session_key
        obj.ip_address = get_ip(self.request)
        if self.request.user.is_authenticated():
            obj.user = self.request.user
        obj.save()

        if not self.request.user.is_authenticated():
            session = self.request.session
            if not obj.pk in session[settings.TEMPORARY_SESSION_KEY]:
                session[settings.TEMPORARY_SESSION_KEY].append(obj.pk)
                session.save()

        return obj
