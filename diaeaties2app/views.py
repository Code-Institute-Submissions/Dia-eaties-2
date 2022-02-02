from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import CommentForm, ContactForm

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


"""Display the contact form"""
def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thank you for contacting us!')
            return redirect('landing_page.html')
            
    contact_form = ContactForm()
    context = {'contact_form': contact_form}
    return render(request, 'contact.html', context)

