from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.http import HttpResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin

from series.models import Serie, Episode

class SerieView(View):

    def get(self, request):
        if request.user.is_authenticated:

            context = {
                'series': list(Serie.objects.all())
            }
            return render(request, 'series.html', context=context)

        raise Http404()

class EpisodeView(LoginRequiredMixin, View):

    def get(self, request, serie_id: int):
        context = {
            'episodes': list(Episode.objects.filter(serie_id=serie_id))
        }

        return render(request, 'episodes.html', context=context)