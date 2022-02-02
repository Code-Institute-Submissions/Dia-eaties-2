from django.contrib import admin
from .models import Recipe, Comment, Contact
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('recipe_name', 'slug', 'status', 'created')
    prepopulated_fields = {'slug': ('recipe_name',)}
    search_fields = ['recipe_name', 'content']
    list_filter = ('status', 'created')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'comment_text', 'recipe', 'created', 'approved')
    search_fields = ('display_name', 'email', 'comment_text')
    list_filter = ('approved', 'created')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'contact_email',
        'subject',
        'message',
        'sent',
    )

    ordering = ('sent',)