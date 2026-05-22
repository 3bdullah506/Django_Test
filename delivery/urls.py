# ════════════════════════════════════════════════════════
#  urls.py — روابط تطبيق delivery
# ════════════════════════════════════════════════════════

from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter   # Topic 10
from rest_framework import viewsets                 # Topic 10
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer


# ─── Topic 10: API ViewSets ───────────────────────────────
# ViewSet = CBV مخصص للـ API — يوفر GET, POST, PUT, DELETE تلقائياً

class ProductViewSet(viewsets.ModelViewSet):
    queryset           = Product.objects.all()
    serializer_class   = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset           = Order.objects.all()
    serializer_class   = OrderSerializer


# الـ Router يولّد روابط الـ API تلقائياً
router = DefaultRouter()
router.register('products', ProductViewSet)   # → /api/products/
router.register('orders',   OrderViewSet)     # → /api/orders/


# ─── الروابط الكاملة ──────────────────────────────────────
urlpatterns = [

    # ── الطلبات (FBV) ──────────────────────────────────────
    path('',               views.order_list,   name='order_list'),
    path('order/add/',     views.order_add,    name='order_add'),
    path('order/edit/<int:pk>/', views.order_edit,   name='order_edit'),
    path('order/del/<int:pk>/',  views.order_delete, name='order_delete'),

    # ── المنتجات (CBV) ─────────────────────────────────────
    path('products/',              views.ProductListView.as_view(),   name='product_list'),
    path('products/add/',          views.ProductCreateView.as_view(), name='product_add'),
    path('products/edit/<int:pk>/',views.ProductUpdateView.as_view(), name='product_edit'),
    path('products/del/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),

]

# أضف روابط الـ API
from django.urls import include
urlpatterns += [
    path('api/', include(router.urls)),   # → /api/products/ و /api/orders/
]
