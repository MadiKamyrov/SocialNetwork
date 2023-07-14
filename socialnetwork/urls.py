from socialnetwork.views import PostViewSet, LikeViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'post', PostViewSet, basename='post')
router.register(r'likes', LikeViewSet, basename='like')

urlpatterns = [

]
urlpatterns += router.urls