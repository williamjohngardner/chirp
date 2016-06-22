from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from main.models import Chirp

class IndexView(ListView):
    template_name = "index.html"
    model = Chirp

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["amount"] = Chirp.objects.all().count()
        return context


class ChirpDetailView(DetailView):
    model = Chirp

    def get_queryset(self):
        return Chirp.objects.filter(bird=self.request.user)


class ChirpCreateView(CreateView):
    model = Chirp
    fields = ["body"]
    success_url = "/"

    def form_valid(self, form):
        chirp = form.save(commit=False)
        chirp.bird = self.request.user
        return super().form_valid(form)
