# ════════════════════════════════════════════════════════
#  views.py — المنطق البرمجي
#
#  Topic 6 : CRUD بأسلوب FBV (Function-Based Views)
#  Topic 7 : @login_required لحماية الصفحات
#  Topic 9 : CBV (Class-Based Views) لمنتجات
# ════════════════════════════════════════════════════════

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required   # Topic 7
from django.views.generic import ListView, CreateView, UpdateView, DeleteView  # Topic 9
from django.urls import reverse_lazy                         # Topic 9
from .models import Product, Order
from .forms  import ProductForm, OrderForm


# ════════════════════════════════════════════════════════
#  ORDERS — بأسلوب FBV (Topic 6)
#  كل دالة = صفحة واحدة
# ════════════════════════════════════════════════════════

# Topic 7: @login_required ← من غير تسجيل دخول يُحوَّل لـ /login/
@login_required
def order_list(request):
    # اجلب كل الطلبات من قاعدة البيانات
    orders = Order.objects.all()
    # أرسلها للصفحة
    return render(request, 'delivery/order_list.html', {'orders': orders})


@login_required
def order_add(request):
    if request.method == 'POST':
        # المستخدم ضغط "حفظ" — خذ البيانات من النموذج
        form = OrderForm(request.POST)
        if form.is_valid():       # تحقق من صحة البيانات
            form.save()           # احفظ في قاعدة البيانات
            return redirect('order_list')  # ارجع للقائمة
    else:
        # المستخدم فتح الصفحة لأول مرة — أعطه نموذج فارغ
        form = OrderForm()
    return render(request, 'delivery/order_form.html', {'form': form, 'title': 'إضافة طلب'})


@login_required
def order_edit(request, pk):
    # ابحث عن الطلب برقمه — إذا ما وُجد أعطِ خطأ 404
    order = get_object_or_404(Order, pk=pk)
    # نفس النموذج لكن مع بيانات الطلب الموجودة (instance=order)
    form  = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'delivery/order_form.html', {'form': form, 'title': 'تعديل الطلب'})


@login_required
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()            # احذف من قاعدة البيانات
        return redirect('order_list')
    return render(request, 'delivery/order_delete.html', {'order': order})


# ════════════════════════════════════════════════════════
#  PRODUCTS — بأسلوب CBV (Topic 9)
#  Class-Based Views: نفس النتيجة بكود أقل
# ════════════════════════════════════════════════════════

# ListView ← يجلب كل السجلات تلقائياً ويرسلها للصفحة
class ProductListView(ListView):
    model               = Product
    template_name       = 'delivery/product_list.html'
    context_object_name = 'products'   # الاسم في الـ HTML


# CreateView ← يعرض النموذج ويحفظ تلقائياً
class ProductCreateView(CreateView):
    model         = Product
    form_class    = ProductForm
    template_name = 'delivery/product_form.html'
    success_url   = reverse_lazy('product_list')  # بعد الحفظ اذهب للقائمة


# UpdateView ← يجلب السجل ويعرضه جاهزاً للتعديل
class ProductUpdateView(UpdateView):
    model         = Product
    form_class    = ProductForm
    template_name = 'delivery/product_form.html'
    success_url   = reverse_lazy('product_list')


# DeleteView ← يطلب تأكيداً ثم يحذف
class ProductDeleteView(DeleteView):
    model         = Product
    template_name = 'delivery/product_delete.html'
    success_url   = reverse_lazy('product_list')
