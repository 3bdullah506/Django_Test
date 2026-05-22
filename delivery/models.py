# ════════════════════════════════════════════════════════
#  models.py — جداول قاعدة البيانات
#  Topic 4: Models & Database
#  Topic 8: Foreign Keys (علاقة بين جدولين)
# ════════════════════════════════════════════════════════

from django.db import models


# ─────────────────────────────────────────────────────────
#  الجدول الأول: المنتجات
#  كل منتج له اسم وسعر فقط — بسيط
# ─────────────────────────────────────────────────────────
class Product(models.Model):

    name  = models.CharField(max_length=200)   # اسم المنتج
    price = models.DecimalField(max_digits=8, decimal_places=2)  # السعر

    # هذه الدالة تحدد ما يظهر عند طباعة الكائن
    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = 'منتج'
        verbose_name_plural = 'المنتجات'


# ─────────────────────────────────────────────────────────
#  الجدول الثاني: الطلبات
#  Topic 8: ForeignKey — كل طلب مرتبط بمنتج من الجدول أعلاه
# ─────────────────────────────────────────────────────────
class Order(models.Model):

    # خيارات حالة الطلب
    STATUS = [
        ('pending',   'قيد الانتظار'),
        ('shipped',   'تم الشحن'),
        ('delivered', 'تم التسليم'),
    ]

    customer_name = models.CharField(max_length=100)   # اسم العميل
    phone         = models.CharField(max_length=20)    # رقم الهاتف
    address       = models.CharField(max_length=300)   # العنوان
    quantity      = models.IntegerField(default=1)     # الكمية
    status        = models.CharField(max_length=20, choices=STATUS, default='pending')  # الحالة
    created_at    = models.DateTimeField(auto_now_add=True)  # التاريخ — يُعبَّأ تلقائياً

    # ── Topic 8: ForeignKey ───────────────────────────────
    # هذا الحقل يربط الطلب بمنتج من جدول Product
    # بدلاً من كتابة اسم المنتج كنص، نربطه بالجدول مباشرة
    product = models.ForeignKey(
        Product,               # الجدول المرتبط به
        on_delete=models.CASCADE,  # لو حُذف المنتج → تُحذف طلباته
        verbose_name='المنتج'
    )

    def __str__(self):
        return f"{self.customer_name} - {self.product.name}"

    class Meta:
        verbose_name        = 'طلب'
        verbose_name_plural = 'الطلبات'
