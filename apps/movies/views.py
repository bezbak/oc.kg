from django.shortcuts import render, redirect
from apps.movies.models import Movie,Comments, Reviews, CommentLikes, CommentDisLikes
from django.db.models import Q
from apps.settings.models import Setting
from apps.categories.models import Genre
from django.db.models import Sum, Count
from datetime import date
# Create your views here.
def movie_detail(request, id):
    setting=Setting.objects.latest('id')
    movie=Movie.objects.get(id=id)
    recomandations=Movie.objects.all().order_by('?')[:6]
    if request.method == 'POST':
        movie=Movie.objects.get(id=id)
        
        if 'comment' in request.POST:
            movie=Movie.objects.get(id=id)
            text=request.POST.get('text')
            user=request.user
            parent=request.POST.get('parent')
            if parent:
                comment=Comments.objects.create(user=user, text=text, movie=movie, parent_id=parent)
                comment.save()
                return redirect('movie_detail', movie.id)
            else:
                comment=Comments.objects.create(user=user, text=text, movie=movie)
                comment.save()
                return redirect('movie_detail', movie.id)
        if 'like' in request.POST or 'son_like' in request.POST:
            movie=Movie.objects.get(id=id)
            comment_id=request.POST.get('comment_id')
            try:
                like=CommentDisLikes.objects.get(user=request.user, comment_id=comment_id)
                like.delete()
                try:    
                    like=CommentLikes.objects.get(user=request.user, comment_id=comment_id)
                    like.delete()
                except:
                    CommentLikes.objects.create(user=request.user, comment_id=comment_id)
            except:
                try:    
                    like=CommentLikes.objects.get(user=request.user, comment_id=comment_id)
                    like.delete()
                except:
                    CommentLikes.objects.create(user=request.user, comment_id=comment_id)
            return redirect('movie_detail', movie.id)
        if 'dislike' in request.POST or 'son_dislike' in request.POST:
            movie=Movie.objects.get(id=id)
            comment_id=request.POST.get('comment_id')
            try:
                like=CommentLikes.objects.get(user=request.user, comment_id=comment_id)
                like.delete()
                try:    
                    like=CommentDisLikes.objects.get(user=request.user, comment_id=comment_id)
                    like.delete()
                except:
                    CommentDisLikes.objects.create(user=request.user, comment_id=comment_id)
            except:
                try:    
                    like=CommentDisLikes.objects.get(user=request.user, comment_id=comment_id)
                    like.delete()
                except:
                    CommentDisLikes.objects.create(user=request.user, comment_id=comment_id)
            return redirect('movie_detail', movie.id)
        if 'review' in request.POST:
            title=request.POST.get('title')
            text=request.POST.get('text')
            rating=request.POST.get('rating')
            review=Reviews.objects.create(user=request.user, movie=movie, title=title, text=text, number=rating)
            mid_rate = movie.review_movie.aggregate(
                numbers = Sum('number'),
                len = Count('id')
            )
            movie.rating = float(str(mid_rate['numbers'] / mid_rate['len'])[:4])
            movie.save()
            
            review.save()
            return redirect('movie_detail', movie.id)
    context={
        'setting': setting,
        'movie': movie,
        'recomandations':recomandations,
    }
    
    return render(request, 'main/details1.html', context)

def movie_search(request):
    movies=Movie.objects.all()
    setting=Setting.objects.latest('id')
    search_key=request.GET.get('key')
    genres=Genre.objects.all()
    genre=request.GET.get('genre')
    review_start=request.GET.get('reviews_start')
    review_end=request.GET.get('reviews_end')
    release_year=request.GET.get('release_year')
    release_year2=request.GET.get('release_year2')
    if search_key:
        movies=Movie.objects.filter(Q(title__icontains=search_key) | Q(description__icontains=search_key))
    genre_list = []
    for genreswe in genres:
        if genre == genreswe.name:
            genre_list.append(genreswe.id)
    if genre or review_start or release_year:
        movies=Movie.objects.filter(genres__in=genre_list,year__year__range=[release_year, release_year2], rating__range = [review_start, review_end])
    context={
        'setting':setting,
        'movies':movies,
        'genres':genres,
        'genre_list':genre_list
        
    }
    return render(request, 'main/search.html', context)

def movie_catalog(request, slug):
    catalog = {
        'movie': 'Фильм',
        'tv_show': 'Сериал',
        'cartoon': 'Мультфильм'
    }
    movies = Movie.objects.all().filter(category__name = catalog[slug])
    setting=Setting.objects.latest('id')
    context = {
        'setting': setting,
        'movies': movies,
    }
    return render(request, 'main/movie_catalog.html', context)