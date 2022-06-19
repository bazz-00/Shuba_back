from rest_framework import routers
from .api import ExecutorViewSet

router = routers.DefaultRouter()
router.register('api/ex', ExecutorViewSet, 'executor')

urlpatterns = router.urls

