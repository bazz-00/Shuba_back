from rest_framework import routers
from .api import ExecutorViewSet, SpecialityViewSet

router = routers.DefaultRouter()
router.register('api/executor', ExecutorViewSet, 'executor')
router.register('api/speciality', SpecialityViewSet, 'speciality')
urlpatterns = router.urls

