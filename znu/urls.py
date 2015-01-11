from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from znu import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'znu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('timetable.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)