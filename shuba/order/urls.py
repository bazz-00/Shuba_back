from rest_framework import routers
from .api import OrderViewSet, OrderCommentsViewSet

router = routers.DefaultRouter()
router.register('api/order', OrderViewSet, 'order')
router.register('api/order_comments', OrderCommentsViewSet, 'order_comments')
urlpatterns = router.urls




