from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse, HttpRequest, Http404

# Create your views here.
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

def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    # DoesNotExist 예외 발생
    # try:
    #     post = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     raise Http404
    return render(request, 'instagram1/post_detail.html', {
        'post': post,
    })

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")