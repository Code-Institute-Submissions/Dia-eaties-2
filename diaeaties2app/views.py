from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Recipe
from .forms import CommentForm, ContactForm, RecipeForm

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created')
    template_name = 'index.html'
    paginate_by = 2


class RecipeDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created')
        loved = False
        if recipe.loves.filter(id=self.request.user.id).exists():
            loved = True
    
        return render (
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "loved": loved,
                "comment_form": CommentForm()
            },
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created')
        loved = False
        if recipe.loves.filter(id=self.request.user.id).exists():
            loved = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.display_name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()
        
        return render (
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "loved": loved,
                "comment_form": CommentForm()
            },
        )


class LovedRecipe(View):
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.loves.filter(id=request.user.id).exists():
            recipe.loves.remove(request.user)
        else:
            recipe.loves.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


"""Displays the contact form"""
def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thank you for contacting us!')
            return redirect('home')
            
    contact_form = ContactForm()
    context = {'contact_form': contact_form}
    return render(request, 'contact.html', context)


class CreateRecipe(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'create_recipe.html'
    success_message = "Thank you for submitting your recipe dia-buddy"

    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.creator = self.request.user
        print(form.cleaned_data)
        return super().form_valid(form)


class UpdateRecipe(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'update_recipe.html'
    success_message = "You have successfully updated your recipe!"

    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'slug': self.object.slug})

"""Delete a blog post"""
class DeleteRecipe(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy("home")


class Profile(View):
    """
    Display recipes created by user as draft and published,
    and the ones they have hit the love button for
    """
    # code credit
    # https://stackoverflow.com/questions/12615154/how-to-get-the-currently
    # -logged-in-users-user-id-in-django

    def get(self, request, *args, **kwargs):
        published = Recipe.objects.filter(status=1, creator=request.user)
        drafts = Recipe.objects.filter(status=0, creator=request.user)
        this_user = request.user
        loves = User.objects.get(pk=this_user.id).main_loves.all()

        return render(
            request,
            'profile.html',
            {
                'published': published,
                'drafts': drafts,
                'loves': loves,
            },
        )
