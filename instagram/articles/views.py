from django.shortcuts import render
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/forms.html', context)