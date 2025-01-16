# blog/views.py  
from django.shortcuts import render
from .forms import PostForm


def home(request):
    # Инициализируем или получаем список постов из сессии  
    posts = request.session.get('posts', [])

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            # Добавляем новый пост в список  
            posts.append({'title': title, 'author': author})
            # Сохраняем список постов обратно в сессию  
            request.session['posts'] = posts
            return render(request, 'blog/home.html', {'form': form, 'message': 'Post added!', 'posts': posts})

    else:
        form = PostForm()

        # Передаем список постов в шаблон
    return render(request, 'blog/home.html', {'form': form, 'posts': posts})