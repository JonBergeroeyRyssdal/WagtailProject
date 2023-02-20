from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.fields import StreamField


class HomePage(Page):
    banner_title = models.CharField(max_length=100, default="Welcome to my blogg!"
    )
    introduction = models.TextField(blank=True)
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    image_1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    image_2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    image_3 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    author = models.ForeignKey(
        'Author',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    body = StreamField([
        ('heading', blocks.CharBlock(template="heading_block.html")), 
        ('image', ImageChooserBlock()), 
        ('paragraph', blocks.RichTextBlock())
    ], null=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("introduction"),
        FieldPanel("banner_image"),
        FieldPanel("image_1"),
        FieldPanel("image_2"),
        FieldPanel("image_3"),
        FieldPanel("author"),
        FieldPanel('body')
    ]

@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(blank=True, max_length=100)
    company_name = models.CharField(blank=True, max_length=100)
    company_url = models.URLField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='+'
    )


    def __str__(self):
        return self.name