from django.conf.urls import patterns, url, include
from tastypie.api import Api
from timetable import views, api

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

urlpatterns = patterns('',
    url(r'^$', views.GroupListView.as_view(), name='group_list'),
    url(r'^map/$', views.MapView.as_view(), name='map'),
    url(r'^teachers/$', views.TeacherListView.as_view(), name='teacher_list'),
    url(r'^teachers/(?P<teacher_id>[0-9]+)/$', views.TeacherDetailView.as_view(), name='teacher_detail'),
    url(r'^groups/$', views.GroupListView.as_view(), name='group_list'),
    url(r'^groups/(?P<group_id>[0-9]+)$', views.GroupDetailView.as_view(), name='group_detail'),
    url(r'^api/$', views.APIView.as_view(), name='api'),
    url(r'^api/', include(v1_api.urls)),
)