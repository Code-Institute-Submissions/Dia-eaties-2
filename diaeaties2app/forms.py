from .models import Comment, Contact, Recipe
from django_summernote.widgets import SummernoteWidget
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ('slug', 'updated_on', 'shared_on', 'loves',)
        widgets = {
            'content': SummernoteWidget(),
        }