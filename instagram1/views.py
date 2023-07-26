from typing import Any
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.http import HttpResponse, HttpRequest, Http404
from django.views.generic import DetailView, ListView, ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView, DateDetailView, CreateView, FormView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from .forms import PostForm
from django.urls import reverse, reverse_lazy

# Create your views here.
# @login_required
# def post_new(request):
#     # POST 요청일 때
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user      # 현재 로그인된 user instance
#             form.save()
#             messages.success(request, '포스팅을 저장했습니다.')
#             return redirect(post)
#     # GET 요청일 때
#     else:
#         form = PostForm()

#     return render(request, 'instagram1/post_form.html', {
#         'form': form,
#         'post': None
#     })

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.author
        messages.success(self.request, '포스팅을 저장했습니다.')
        return super().form_valid(form)
    
post_new = PostCreateView.as_view()

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)

#     # 작성자 Check Tip
#     if post.author != request.user:
#         messages.error(request, '작성자만 수정할 수 있습니다.')
#         return redirect(post)

#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             messages.success(request, '포스팅을 수정했습니다.')
#             return redirect(post)
#     else:
#         form = PostForm(instance=post)

#     return render(request, 'instagram1/post_form.html', {
#         'form': form,
#         'post': post

#     })

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, '포스팅을 수정했습니다.')
        return super().form_valid(form)
    
post_edit = PostUpdateView.as_view()

# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         post.delete()
#         messages.success(request, '포스팅을 삭제했습니다.')
#         return redirect('instagram1:post_list')
#     return render(request, 'instagram1/post_confirm_delete.html', {
#         'post': post,
#     })

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('instagram1:post_list')

    # def get_success_url(self):
    #     return reverse('instagram1:post_list')
    
post_delete = PostDeleteView.as_view()

def post_list(request):
    qs = Post.objects.all()
    # 결과 없으면 ''
    q = request.GET.get("q", "")

    if q:
        qs = qs.filter(message__icontains=q)

    # instagram1/templates/instagram1/post_list.html
    return render(
        request,
        "instagram1/post_list.html",
        {
            "post_list": qs,
            'q': q,
        },
    )

# post_list = ListView.as_view(model=Post, paginate_by=10)

# @method_decorator(login_required, name='dispatch')
# class PostListView(ListView):
#     model = Post
#     paginate_by = 10

# post_list = PostListView.as_view()

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