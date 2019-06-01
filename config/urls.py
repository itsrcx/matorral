# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views import defaults as default_views

from rest_framework.routers import DefaultRouter

from alameda.sprints import views as sprints_views
from alameda.stories import views as stories_views


router = DefaultRouter()
router.register(r'epics', stories_views.EpicViewSet)
router.register(r'sprints', sprints_views.SprintViewSet)
router.register(r'stories', stories_views.StoryViewSet)
router.register(r'tasks', stories_views.TaskViewSet)

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # health checks
    url(r'^health-check/', include('watchman.urls')),
    url(r'^health/', include('alameda.health_checks.urls')),

    # User management
    url(r'^users/', include('alameda.users.urls')),
    # comments app
    url(r'^comments/', include('django_comments_xtd.urls')),

    # API urls
    url(r'^api/v1/', include('alameda.authentication.urls')),
    url(r'^api/v1/', include(router.urls)),

    # App
    path(r'', include('alameda.stories.urls', namespace='stories')),
    path(r'sprints/', include('alameda.sprints.urls', namespace='sprints')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    import debug_toolbar

    urlpatterns = [  # prepend
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
