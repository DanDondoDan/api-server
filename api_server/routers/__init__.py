__all___ = ['router']


from rest_framework.routers import DefaultRouter, SimpleRouter


from api_server.settings import SERVICE_VARS as cfg
from api_server import views


_VIEWS = (
    views.DepartmentViewSet,
    views.SearchPersonViewSet,
    views.SearchProductViewSet,
)



router = DefaultRouter()


for rt in _VIEWS:
    name = rt.__name__[:rt.__name__.index(cfg['viewset_suffix'])].lower() + 's'
    router.register(name, rt)