from django.db import models
from django.contrib.auth import get_user_model
from apps.common.models import TimeStampModel
from apps.articles.models import Article
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Response(TimeStampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responses")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="responses")
    parent_response = models.ForeignKey(
            "self",
            on_delete=models.CASCADE,
            null=True,
            blank=True,
            related_name="replies"
        )
    
    content = models.TextField(verbose_name=_("response_content"))

    class Meta:
        verbose_name = "Response"
        verbose_name_plural = "Responses"
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.user.first_name} commented on {self.article.title}"
