from django.conf.urls import patterns, url, include
from django.views import generic
from tastypie.api import Api
from timetable import views, api
from znu import settings

v1_api = Api(api_name='v1')
v1_api.register(api.DepartmentResource())
v1_api.register(api.GroupResource())
v1_api.register(api.TeacherResource())
v1_api.register(api.CampusResource())
v1_api.register(api.AudienceResource())
v1_api.register(api.LessonResource())
v1_api.register(api.TimeResource())
v1_api.register(api.TimetableResource())
v1_api.register(api.CurrentWeekResource())

urlpatterns = patterns(
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^map/$', views.MapView.as_view(), name='map'),
    url(r'^teachers/$', views.TeacherListView.as_view(), name='teacher_list'),
    url(r'^teachers/(?P<teacher_id>[0-9]+)/$', views.TeacherDetailView.as_view(), name='teacher_detail'),
    url(r'^api/', include(v1_api.urls)),
)