
class RequestFromKwargsMixin(object):

    def get_form_kwargs(self):
        kwargs = super(RequestFromKwargsMixin, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
