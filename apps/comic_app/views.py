from django.views.generic import TemplateView

from .models import Comic


class ComicTemplateView(TemplateView):
    template_name = 'comic_app/show.html'

    def get_context_data(self, **kwargs):
        start = 1 if kwargs['sequence'] is None or kwargs['sequence'] == '0' else int(kwargs['sequence'])

        context = {
            'comics': Comic.objects.all(),
            'start': start - 1
        }
        return context
