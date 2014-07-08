from __future__ import absolute_import

from rest_framework import serializers
from rest_framework.reverse import reverse

from .classes import StagingFile
from .models import StagingFolder


class SerializerStagingFolderFile(serializers.Serializer):
    url = serializers.SerializerMethodField('get_url')
    image_url = serializers.SerializerMethodField('get_image_url')
    filename = serializers.CharField(max_length=255)

    def get_url(self, obj):
        return reverse('stagingfolderfile-detail', args=[obj.staging_folder.pk, obj.filename], request=self.context.get('request'))

    def get_image_url(self, obj):
        return reverse('stagingfolderfile-image-view', args=[obj.staging_folder.pk, obj.filename], request=self.context.get('request'))


class SerializerStagingFolder(serializers.HyperlinkedModelSerializer):
    files = serializers.SerializerMethodField('get_files')

    def get_files(self, obj):
        return [SerializerStagingFolderFile(entry).data for entry in obj.get_files()]

    class Meta:
        model = StagingFolder