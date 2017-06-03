from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    # Admin URL patterns
    url(r'^admin/', include(admin.site.urls)),

    # Top level home page URL pattern
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home')
)
