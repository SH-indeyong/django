from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='root.html'), name='root'),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("blog1/", include("blog1.urls")),
    path("instagram1/", include("instagram1.urls")),
]    

# DEBUG=TRUE일 때 추가
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

# settings.MEDIA_URL
# settings.MEDIA_ROOT
