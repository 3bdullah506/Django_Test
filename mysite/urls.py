# ════════════════════════════════════════════════════════
#  urls.py — الروابط الرئيسية للمشروع
# ════════════════════════════════════════════════════════

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # ← Topic 7: روابط تسجيل الدخول الجاهزة

urlpatterns = [

    # لوحة الإدارة
    path('admin/', admin.site.urls),

    # كل روابط تطبيق delivery
    path('', include('delivery.urls')),

    # ─── Topic 7: Authentication ───────────────────────────
    # صفحة تسجيل الدخول — Django يوفرها جاهزة
    path('login/',  auth_views.LoginView.as_view(template_name='delivery/login.html'),  name='login'),
    # تسجيل الخروج — يرجع للصفحة المحددة في settings.py
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
