from django.shortcuts import render, redirect
from django.contrib import messages
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
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:index')
        messages.warning(request, '폼을 확인 후 제출해주세요.')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/forms.html', context)