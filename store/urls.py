from django.urls import path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("products", views.ProductViewSet, basename="products")
router.register("customers", views.CustomerViewSet)
router.register("collections", views.CollectionViewSet)
router.register("carts", views.CartViewSet)
router.register("orders", views.OrderViewSet, basename="orders")


product_router = routers.NestedDefaultRouter(router, "products", lookup="product")
product_router.register("reviews", views.ReviewViewSet, basename="product-reviews")
product_router.register("images", views.ProductImageViewSet, basename="product-images")

cart_router = routers.NestedDefaultRouter(router, "carts", lookup="cart")
cart_router.register("items", views.CartItemsViewSet, basename="cart-items")


urlpatterns = router.urls + product_router.urls + cart_router.urls
