from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ListProjectView, SingleProjectView


urlpatterns = {
    url(r'^projects/$', ListProjectView.as_view(), name="List of projects"),
    url(r'^projects/(?P<pk>[0-9]+)/$', SingleProjectView.as_view(), name='Project'),
}

urlpatterns = format_suffix_patterns(urlpatterns)
