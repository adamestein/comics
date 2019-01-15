from django.conf import settings
from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from django.views.static import serve

from django.contrib import admin
admin.autodiscover()

from comic_app.views import ComicTemplateView

urlpatterns = [
    # Admin URL patterns
    url(r'^admin/', include(admin.site.urls)),

    # Top level home page URL pattern
    url(r'^$', RedirectView.as_view(url=reverse_lazy('show_comic')), name='home'),

    # Show a comic
    url(r'^show/(?:(?P<sequence>\d+)/?)?$', ComicTemplateView.as_view(), name='show_comic')
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]
