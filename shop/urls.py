from rest_framework.routers import DefaultRouter
from .api.category_view import CategoryViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')

urlpatterns = router.urls