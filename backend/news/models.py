from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, RichTextFieldPanel
from wagtail.api import APIField


class NewsPage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        RichTextFieldPanel('body')
    ]
    
    api_fields = [
        APIField('intro'),
        APIField('body'),
    ]