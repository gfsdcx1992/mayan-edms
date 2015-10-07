from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .api_views import (
    DocumentOCRAPIView, DocumentPageContentAPIView, DocumentVersionOCRAPIView
)
from .views import (
    DocumentAllSubmitView, DocumentSubmitView, DocumentSubmitManyView,
    DocumentTypeSettingsEditView, DocumentTypeSubmitView, EntryListView
)

urlpatterns = patterns(
    'ocr.views',
    url(
        r'^(?P<document_id>\d+)/content/$', 'document_content',
        name='document_content'
    ),
    url(
        r'^document/(?P<pk>\d+)/submit/$', DocumentSubmitView.as_view(),
        name='document_submit'
    ),
    url(
        r'^document/all/submit/$', DocumentAllSubmitView.as_view(),
        name='document_submit_all'
    ),
    url(
        r'^document/type/submit/$', DocumentTypeSubmitView.as_view(),
        name='document_type_submit'
    ),
    url(
        r'^document/multiple/submit/$', DocumentSubmitManyView.as_view(),
        name='document_submit_multiple'
    ),
    url(
        r'^document_type/(?P<pk>\d+)/ocr/settings/$',
        DocumentTypeSettingsEditView.as_view(),
        name='document_type_ocr_settings'
    ),

    url(r'^all/$', EntryListView.as_view(), name='entry_list'),
    url(r'^(?P<pk>\d+)/delete/$', 'entry_delete', name='entry_delete'),
    url(
        r'^multiple/delete/$', 'entry_delete_multiple',
        name='entry_delete_multiple'
    ),
    url(r'^(?P<pk>\d+)/re-queue/$', 'entry_re_queue', name='entry_re_queue'),
    url(
        r'^multiple/re-queue/$', 'entry_re_queue_multiple',
        name='entry_re_queue_multiple'
    ),
)

api_urls = patterns(
    '',
    url(
        r'^document/(?P<pk>\d+)/submit/$', DocumentOCRAPIView.as_view(),
        name='document-ocr-submit-view'
    ),
    url(
        r'^document_version/(?P<pk>\d+)/submit/$', DocumentVersionOCRAPIView.as_view(),
        name='document-version-ocr-submit-view'
    ),
    url(
        r'^page/(?P<pk>\d+)/content/$', DocumentPageContentAPIView.as_view(),
        name='document-page-content-view'
    ),

)

