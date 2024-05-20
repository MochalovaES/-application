from django.urls import path, include
from rest_framework.routers import DefaultRouter

from publication.apps import PublicationConfig
from publication.views import PostViewSet, CommentViewSet

app_name = PublicationConfig.name

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'post/(?P<post_pk>\d+)/comments', CommentViewSet, basename='comment')

urlpatterns = [path("", include(router.urls))]
