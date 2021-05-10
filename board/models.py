from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=256, unique_for_date="created_at")
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[self.created_at.year, self.created_at.month, self.created_at.day, self.slug],
        )

