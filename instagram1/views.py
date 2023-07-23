from django.shortcuts import render
from .models import Post


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
        },
    )
