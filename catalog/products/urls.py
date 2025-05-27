from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.views import index, about, product_details, cart_add, cart_detail, cart_delete, checkout
from products.views.product import ProductViewSet
from products.views.category import CategoryViewSet
from products.views.cart import CartViewSet

app_name = 'products'
router = DefaultRouter()
router.register(r"products", viewset=ProductViewSet)
router.register(r"categories", viewset=CategoryViewSet)
router.register(r"cart", viewset=CartViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('product/<int:product_id>/', product_details, name='product_details'),
    path('cart_add/<int:product_id>/', cart_add, name='cart_add'),
    path("cart_detail/", cart_detail, name="cart_detail"),
    path('cart_delete/<int:product_id>/', cart_delete, name="cart_delete"),
    path("checkout/", checkout, name="checkout"),
    
]
urlpatterns += router.urls