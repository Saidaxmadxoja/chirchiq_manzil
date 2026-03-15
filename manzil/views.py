from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Category, Manzil
from .serializers import CategorySerializer, ManzilSerializer


# --- API ViewSet-lar (REST Framework uchun) ---

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ManzilViewSet(viewsets.ModelViewSet):
    queryset = Manzil.objects.all()
    serializer_class = ManzilSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# --- Oddiy View-lar (HTML shablonlar uchun) ---

def category_list(request):
    """Barcha kategoriyalar ro'yxati"""
    categories = Category.objects.all()
    return render(request, 'manzil/category_list.html', {
        'categories': categories
    })


def manzil_list(request, category_id):
    """Tanlangan kategoriya ichidagi manzillar ro'yxati"""
    category = get_object_or_404(Category, id=category_id)

    # .order_by('id') minus belgisiz yozildi.
    # Endi 1-maktab tepada, 26-maktab esa eng pastda chiqadi.
    manzillar = Manzil.objects.filter(category=category).order_by('id')

    return render(request, 'manzil/manzil_list.html', {
        'category': category,
        'manzillar': manzillar
    })


def manzil_detail(request, pk):
    """Manzil haqida to'liq ma'lumot"""
    manzil = get_object_or_404(Manzil, pk=pk)
    return render(request, 'manzil/manzil_detail.html', {
        'manzil': manzil
    })