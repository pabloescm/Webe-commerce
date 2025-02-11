from rest_framework.routers import DefaultRouter
from .api.category_view import CategoryViewSet
from .api.product_view import ProductViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')

urlpatterns = router.urls