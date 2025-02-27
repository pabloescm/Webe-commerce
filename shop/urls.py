from rest_framework.routers import DefaultRouter
from .api.category_view import CategoryViewSet
from .api.product_view import ProductViewSet
from .api.product_image_view import ProductImageViewSet
from .api.user_registration_view import UserRegistrationViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')
router.register('product-images', ProductImageViewSet, basename='productimage')
router.register('register/', UserRegistrationViewSet, basename='user_register'),

urlpatterns = router.urls