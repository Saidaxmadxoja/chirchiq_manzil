from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Category, Manzil
from .serializers import CategorySerializer, ManzilSerializer
from django.db.models import Q

# --- API ViewSet-lar (DRF & JWT uchun tayyor) ---
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
        # Qidiruv natijalarini ID bo'yicha tartiblash
        manzillar = Manzil.objects.filter(
            Q(name__icontains=query) | Q(address__icontains=query)
        ).order_by('id')
        return render(request, 'manzil/manzil_list.html', {
            'manzillar': manzillar,
            'query': query,
            'category': None
        })

    categories = Category.objects.all().order_by('id')
    return render(request, 'manzil/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    """Tanlangan kategoriya ichidagi manzillar ro'yxati"""
    category = get_object_or_404(Category, id=category_id)
    
    # MUHIM: Nomi bo'yicha emas, ID bo'yicha tartiblash (1, 2, 3... 10 tartibi uchun)
    manzillar = Manzil.objects.filter(category=category).order_by('id')
    
    query = request.GET.get('q')
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
    """Manzil haqida to'liq ma'lumot (Batafsil sahifa)"""
    manzil = get_object_or_404(Manzil, pk=pk)
    return render(request, 'manzil/manzil_detail.html', {'manzil': manzil})
