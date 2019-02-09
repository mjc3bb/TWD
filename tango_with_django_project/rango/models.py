from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args,**kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class WebLink(models.Model):
    category = models.ForeignKey(Category, on_delete='CASCADE')
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE')

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class WebLinkPage(Page):
    category = models.ForeignKey(Category, on_delete='CASCADE',null=True)
    body = RichTextField(blank=True)
    link = models.URLField(blank=True)
    views = models.IntegerField(default=0)
    content_panels = Page.content_panels +[FieldPanel('link', classname="full"),
                                           FieldPanel('category',  classname="full")]
