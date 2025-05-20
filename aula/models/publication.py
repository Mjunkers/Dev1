from django.db import models
from .base_model import BaseModel
from .revista import Magazine
from .article import Article


class Publication(BaseModel):
    magazine = models.ForeignKey(Magazine, on_delete=models.RESTRICT)
    article = models.ForeignKey(Article, on_delete=models.RESTRICT)
    #editor = models.ForeignKey(Editor, on_delete=models.RESTRICT)
    date = models.DateField()
    obs = models.TextField()