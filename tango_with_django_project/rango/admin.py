from django.contrib import admin
from .models import Category, WebLink, UserProfile
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    list_filter = ['category']
    search_fields = ['title', 'url']


admin.site.register(WebLink, PageAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(UserProfile)
