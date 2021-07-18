from django.urls import path, include, re_path
from rest_framework import routers, permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenRefreshView
from api.views import MyObtainTokenPairView, UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

# swagger ui api doc settings
schema_view = get_schema_view(
    openapi.Info(
        title="Auth API's",
        default_version='v1',
        description="This API allows authentication and authorization",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('api/token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
