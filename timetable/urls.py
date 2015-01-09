from django.conf.urls import patterns, url, include
from django.views import generic
from tastypie.api import Api

from timetable.api import DepartmentResource, GroupResource, TeacherResource, CampusResource, AudienceResource, \
    LessonResource, TimetableResource, CurrentWeekResource, TimeResource

v1_api = Api(api_name='v1')
v1_api.register(DepartmentResource())
v1_api.register(GroupResource())
v1_api.register(TeacherResource())
v1_api.register(CampusResource())
v1_api.register(AudienceResource())
v1_api.register(LessonResource())
v1_api.register(TimeResource())
v1_api.register(TimetableResource())
v1_api.register(CurrentWeekResource())

urlpatterns = patterns('',
                       # url(r'^$', views.IndexView.as_view(), name='index'),
                       (r'^api/', include(v1_api.urls)),
)