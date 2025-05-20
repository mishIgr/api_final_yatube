from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GroupViewSet, PostViewSet, FollowViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'follow', FollowViewSet, basename='follow')

comment_router = DefaultRouter()
comment_router.register(r'comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
    path('posts/<int:post_id>/', include(comment_router.urls)),
]
