from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r"admin/", admin.site.urls),
    url(r"", include("physics_quiz.apps.home.urls")),
    url(r"", include("physics_quiz.apps.quiz.urls")),
    url(r"", include("physics_quiz.apps.classroom.urls")),
    url(r"", include("django.contrib.auth.urls")),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
