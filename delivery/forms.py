# ════════════════════════════════════════════════════════
#  forms.py — نماذج الإدخال
#  Topic 6: CRUD — نموذج لكل جدول
# ════════════════════════════════════════════════════════

from django import forms
from .models import Product, Order


# نموذج إدخال المنتج
class ProductForm(forms.ModelForm):
    class Meta:
        model  = Product               # مرتبط بجدول Product
        fields = ['name', 'price']     # الحقول التي تظهر في النموذج


# نموذج إدخال الطلب
class OrderForm(forms.ModelForm):
    class Meta:
        model  = Order   # مرتبط بجدول Order
        fields = ['customer_name', 'phone', 'address', 'product', 'quantity', 'status']
        # product ← سيظهر كقائمة منسدلة بالمنتجات الموجودة (بسبب ForeignKey)
