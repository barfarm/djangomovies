from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# def hello(request):
#     return HttpResponse("Hello world!")

from django import views
from django.shortcuts import  render
from core.models import Movie, age_chs
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
import logging
from django.shortcuts import render

from django.urls import reverse_lazy

from core.forms import MovieForm
from core.models import Movie

logging.basicConfig(
    filemode='w',
                    filename='log.txt',
                    level=logging.INFO
                    )
LOGGER=logging.getLogger(__name__)
from core.forms import MovieForm
from core.models import Movie

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff
# class MovieCreateView (FormView):
#     template_name = 'form.html'
#     form_class=MovieForm
class MovieListView(LoginRequiredMixin,ListView,StaffRequiredMixin):
    template_name = 'movie_list.html'
    model=Movie

class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
    model=Movie

class MovieDeleteView(LoginRequiredMixin,DeleteView,StaffRequiredMixin):
    template_name = 'movie_confirm_delete.html'
    model=Movie
    success_url= reverse_lazy("core:movie_list")

# class IndexView(MovieListView):
#     template_name = 'index.html'

class MovieCreateView(LoginRequiredMixin,CreateView,StaffRequiredMixin):
    title='Add Movie'
    template_name = 'form.html'
    form_class = MovieForm
    success_url= reverse_lazy("core:movie_list")


    def form_invalid(self,form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        result=super().post(request,*args,**kwargs)
        if title := request._post.get('title'):
            LOGGER.info(f'Successfully added new movie: {title}')
        # LOGGER.info(f" Created movie {request._post['title']} ")
        return result


class MovieUpdateView(LoginRequiredMixin,UpdateView,StaffRequiredMixin):
    template_name = 'form.html'
    model=Movie
    form_class = MovieForm
    success_url= reverse_lazy('core:movie_list')

    def form_invalid(self,form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)



# class MovieView(ListView):
#     template_name='movies.html'
#     model=Movie
#
#     def get_context_data(self,**kwargs):
#         contex=super().get_context_data(**kwargs)
#         contex['age_limits']=age_chs
#         return contex



# class MovieView(TemplateView):
#     template_name='movies.html'
#     context = {'movies': Movie.objects.all(), 'limits': age_chs}

# class MovieView(views.View):
#     def get(self,request):
#         return render(
#             request,
#             template_name='movies.html',
#             context={'movies':Movie.objects.all(),'limits':age_chs},
#         )

def hello(request):
    LOGGER.info('wreszcie dziala')
    return render(
        request,
        template_name="hello.html",
        context= {'adjectives':["beautiful","cruel","wonderful"]},
    )
#
# def movies(request):
#     return render(
#         request,
#         template_name="movies.html",
#         context= {'movies':Movie.objects.all(),'limits':age_chs},
#     )
