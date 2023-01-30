from rest_framework import routers
from .drf import UserDRF_REST

router = routers.DefaultRouter()
router.register('',UserDRF_REST, 'profile')

urlpatterns = router.urls