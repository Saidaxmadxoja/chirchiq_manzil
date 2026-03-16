from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Category, Manzil
from .serializers import CategorySerializer, ManzilSerializer
from django.db.models import Q

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
    """Barcha kategoriyalar ro'yxati va umumiy qidiruv"""
    query = request.GET.get('q')
    if query:
        # Asosiy sahifadan qidirilganda hamma manzillar ichidan qidiradi
        manzillar = Manzil.objects.filter(
            Q(name__icontains=query) | Q(address__icontains=query)
        ).order_by('-id')
        return render(request, 'manzil/manzil_list.html', {
            'manzillar': manzillar,
            'query': query,
            'category': None
        })

    categories = Category.objects.all()
    return render(request, 'manzil/category_list.html', {
        'categories': categories
    })

def manzil_list(request, category_id):
    """Kategoriya ichidagi qidiruv"""
    category = get_object_or_404(Category, id=category_id)
    query = request.GET.get('q')

    manzillar = Manzil.objects.filter(category=category).order_by('-id')

    if query:
        manzillar = manzillar.filter(
            Q(name__icontains=query) | Q(address__icontains=query)
        )

    return render(request, 'manzil/manzil_list.html', {
        'category': category,
        'manzillar': manzillar,
        'query': query
    })

def manzil_detail(request, pk):
    manzil = get_object_or_404(Manzil, pk=pk)
    return render(request, 'manzil/manzil_detail.html', {
        'manzil': manzil
    })