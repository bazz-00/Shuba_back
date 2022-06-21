from rest_framework import routers
from .api import ExecutorViewSet, SpecialityViewSet, OrdersViewSet

router = routers.DefaultRouter()
router.register('api/executor', ExecutorViewSet, 'executor')
router.register('api/speciality', SpecialityViewSet, 'speciality')
router.register('api/orders', OrdersViewSet, 'orders')
urlpatterns = router.urls

