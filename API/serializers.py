from rest_framework import serializers
from .models import Project, Link, Screenshot


class ScreenshotSerializer(serializers.ModelSerializer):
    """Serializer to map Screenshot Model into JSON."""

    class Meta:
        model = Screenshot
        fields = ('id', 'image')


class LinkSerializer(serializers.ModelSerializer):
    """Serializer to map Link Model into JSON."""

    class Meta:
        model = Link
        fields = ('link_type', 'link')


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer to map Project Model into JSON."""
    project_tags = serializers.StringRelatedField(many=True)
    links = LinkSerializer(many=True)
    screenshots_reference = ScreenshotSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'image', 'description', 'date_added', 'project_tags', 'links', 'screenshots_reference')
