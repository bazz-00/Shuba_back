from rest_framework import routers
from .api import  OrdersViewSet

router = routers.DefaultRouter()
router.register('api/orders', OrdersViewSet, 'orders')
urlpatterns = router.urls