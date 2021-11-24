from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, RichTextFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.api.fields import ImageRenditionField
from wagtail.api import APIField
from wagtail_headless_preview.models import HeadlessPreviewMixin


class NewsPage(HeadlessPreviewMixin, Page):
    intro = models.CharField(max_length=250)
    body = StreamField([
        ("heading", blocks.CharBlock(classname="full title", icon="title")),
        ("paragraph", blocks.RichTextBlock(icon='pilcrow')),
        ("image", ImageChooserBlock(icon="image")),
    ])
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        ImageChooserPanel('image'),
    ]
    
    api_fields = [
        APIField('intro'),
        APIField('body'),
        APIField('image_thumbnail', serializer=ImageRenditionField('fill-300x300', source='image')),
    ]