from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from rango.models import Category
# Create your models here.

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class WebLinkPage(Page):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    body = RichTextField(blank=True)
    link = models.URLField(blank=True)
    views = models.IntegerField(default=0)
    content_panels = Page.content_panels +[FieldPanel('link', classname="full"),
                                           SnippetChooserPanel('category',  classname="full")]
