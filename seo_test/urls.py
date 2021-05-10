from board.sitemaps import PostSitemap
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path("board/", include("board.urls", namespace="board")),
    path(
        "sitesmap.xml",
        sitemap,
        {"stiemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
