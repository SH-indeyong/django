from typing import Any
from django.db import models
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse, HttpRequest, Http404
from django.views.generic import DetailView, ListView, ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView, DateDetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
# def post_list(request):
#     qs = Post.objects.all()
#     # 결과 없으면 ''
#     q = request.GET.get("q", "")

#     if q:
#         qs = qs.filter(message__icontains=q)

#     # instagram1/templates/instagram1/post_list.html
#     return render(
#         request,
#         "instagram1/post_list.html",
#         {
#             "post_list": qs,
#             'q': q,
#         },
#     )

# post_list = ListView.as_view(model=Post, paginate_by=10)

@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    paginate_by = 10

post_list = PostListView.as_view()

# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     # DoesNotExist 예외 발생
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#     return render(request, 'instagram1/post_detail.html', {
#         'post': post,
#     })

class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs

post_detail = PostDetailView.as_view(model=Post)

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)
post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at')
post_archive_month = MonthArchiveView.as_view(model=Post, date_field='created_at')
post_archive_day = DayArchiveView.as_view(model=Post, date_field='created_at')