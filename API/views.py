from rest_framework import generics
from .serializers import ProjectSerializer, LinkSerializer
from .models import Project, Tag, Link, Screenshot


class ListProjectView(generics.ListAPIView):
    """This class creates a GET(All) request for projects"""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class SingleProjectView(generics.RetrieveAPIView):
    """This class creates a single object GET request for a particular project"""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
