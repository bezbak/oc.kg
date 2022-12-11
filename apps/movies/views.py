from django.shortcuts import render, redirect
from apps.movies.models import Movie,Comments, Reviews, CommentLikes, CommentDisLikes
from apps.settings.models import Setting
# Create your views here.
def movie_detail(request, id):
    setting = Setting.objects.latest('id')
    movie = Movie.objects.get(id = id)
    recomandations = Movie.objects.all().order_by('?')[:6]
    # ! Рейтинг для видео среднее значение
    review1 = 0
    rev1 = 0
    for rev in movie.review_movie.all():
        review1 +=1
        rev1 +=rev.number
    review = rev1 / review1
    reviews = {}
    # ! Рейтинт для рекомендаций среднее значение
    for movie in recomandations:
        rev_count = 0
        rev_num = 0
        for rev in movie.review_movie.all():
            rev_count += 1
            rev_num += rev.number
        rev_mid = rev_num/ rev_count
        reviews.setdefault(movie.title, str(rev_mid)[:4])
    if request.method == 'POST':
        if 'comment' in request.POST:
            text = request.POST.get('text')
            user = request.user
            parent = request.POST.get('parent')
            if parent:
                comment = Comments.objects.create(user = user, text = text, movie = movie, parent_id=parent)
                comment.save()
                return redirect('movie_detail', movie.id)
            else:
                comment = Comments.objects.create(user = user, text = text, movie = movie)
                comment.save()
                return redirect('movie_detail', movie.id)
        if 'like' in request.POST or 'son_like' in request.POST:
            comment_id = request.POST.get('comment_id')
            try:
                like = CommentDisLikes.objects.get(user = request.user, comment_id = comment_id)
                like.delete()
                try:    
                    like = CommentLikes.objects.get(user = request.user, comment_id = comment_id)
                    like.delete()
                except:
                    CommentLikes.objects.create(user = request.user, comment_id = comment_id)
            except:
                try:    
                    like = CommentLikes.objects.get(user = request.user, comment_id = comment_id)
                    like.delete()
                except:
                    CommentLikes.objects.create(user = request.user, comment_id = comment_id)
            return redirect('movie_detail', movie.id)
        if 'dislike' in request.POST or 'son_dislike' in request.POST:
            comment_id = request.POST.get('comment_id')
            try:
                like = CommentLikes.objects.get(user = request.user, comment_id = comment_id)
                like.delete()
                try:    
                    like = CommentDisLikes.objects.get(user = request.user, comment_id = comment_id)
                    like.delete()
                except:
                    CommentDisLikes.objects.create(user = request.user, comment_id = comment_id)
            except:
                try:    
                    like = CommentDisLikes.objects.get(user = request.user, comment_id = comment_id)
                    like.delete()
                except:
                    CommentDisLikes.objects.create(user = request.user, comment_id = comment_id)
            return redirect('movie_detail', movie.id)
        if 'review' in request.POST:
            title = request.POST.get('title')
            text = request.POST.get('text')
            rating = request.POST.get('rating')
            review = Reviews.objects.create(user = request.user, movie = movie, title = title, text = text, number = rating)
            review.save()
            return redirect('movie_detail_reviews', movie.id)
    context = {
        'setting': setting,
        'movie': movie,
        'review' : str(review)[:4],
        'recomandations':recomandations,
        'reviews':reviews
    }
    
    return render(request, 'main/details1.html', context)