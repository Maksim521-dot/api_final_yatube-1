from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostViewSet)
router_v1.register(r'groups', GroupViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments')
router_v1.register(r'follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/jwt/create/', TokenObtainPairView),
    path('v1/jwt/refresh/', TokenRefreshView),
    path('v1/jwt/verify/', TokenVerifyView),
    path('v1/', include(router_v1.urls)),
]
