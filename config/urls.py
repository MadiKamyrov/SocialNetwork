from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from socialnetwork.views import UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("socialnetwork.urls")),
    path('users/', UserCreateView.as_view(), name='token_obtain_pair'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]