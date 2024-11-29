from rest_framework import routers
from .api import FacturaViewSet, ProductoViewSet

router = routers.DefaultRouter()

router.register('api/factura', FacturaViewSet,'factura')
router.register('api/productos', ProductoViewSet,'productos')

urlpatterns = router.urls