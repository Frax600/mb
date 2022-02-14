from django.views.generic import ListView # new
from .models import Post                  # new

# Create your views here.


class HomePageView(ListView):             # new
    model = Post                          # new
    template_name = 'home.html'           # new
    context_object_name = 'all_posts_list'  # new
