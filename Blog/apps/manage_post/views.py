from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from apps.manage_post.models import Article, Category
from apps.manage_post.forms import CommentForm
from django.contrib.auth import get_user_model

User = get_user_model()

class IndexView(ListView):
    #Django execute the encapsulated query methods (from This one's father)
    model = Article

    # we override the orignial get_context_method
    def get_context_data(self, **kwargs):
        #also, we get activate articles (using the original query)
        context = super().get_context_data(**kwargs)

        #we add more queries, now the query is --> SELECT * FROM Article WHERE Status = Treue
        context['articles'] = Article.objects.filter(status='True')

        # SELECT * FROM category WHERE featured = true
        context['navbar_category'] = Category.objects.filter(featured=True)
        return context

# We show only one of all of them
class CategoryDetailView(DetailView):
    #Django execute the encapsulated query methods (from This one's father)
    #DetailView is special, it gets data from URL
    model = Category
    #we change the key name
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #Send activated articles based on their category
        #SELECT * FROM category WHERE slug='python'
        context['articles'] = Article.objects.filter(status=True).filter(categories=Category.objects.get(slug=self.kwargs['slug'])
                                                                         )

        context['navbar_category'] = Category.objects.filter(featured=True)
        return context


class ListAllCategoriesView(ListView):
    model = Category
    context_object_name = 'categories'

#Multiple Inheritance
class ShowPostDetailView(FormMixin, DetailView):
    model = Article
    form_class = CommentForm
    context_object_name = 'article'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        form.instance.article_id = Article.objects.get(slug=self.kwargs['slug']).id
        form.instance.user_id = User.objects.get(id=self.request.user.id)

        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'slug': self.kwargs['slug']})

