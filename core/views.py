from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# def hello(request):
#     return HttpResponse("Hello world!")

from django import views
from django.shortcuts import  render
from core.models import Movie, age_chs
from django.views.generic import TemplateView, ListView, FormView

from core.forms import MovieForm
from core.models import Movie

class MovieCreateView (FormView):
    template_name = 'form.html'
    form_class=MovieForm

class MovieView(ListView):
    template_name='movies.html'
    model=Movie

    def get_context_data(self,**kwargs):
        contex=super().get_context_data(**kwargs)
        contex['age_limits']=age_chs
        return contex



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
