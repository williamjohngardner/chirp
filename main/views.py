from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main.models import Chirp, StopWord, Profile
from django.core.urlresolvers import reverse_lazy

class IndexView(CreateView):
    template_name = "index.html"
    model = Chirp
    fields = ["body"]
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        stop_words = StopWord.objects.all()
        chirp_body = form.cleaned_data["body"].lower()
        for stop_word in stop_words:
            if stop_word.word in chirp_body:
                form.add_error("body", "YOU IS A POTTY MOUTH!!!")
                return self.form_invalid(form)
        chirp = form.save(commit=False)
        chirp.bird = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Chirp.objects.all()
        context["amount"] = Chirp.objects.all().count()
        return context


class ChirpDetailView(DetailView):
    model = Chirp

    def get_queryset(self):
        return Chirp.objects.filter(bird=self.request.user)


class ProfileUpdateView(UpdateView):

    fields = ["favorite_bird", "photo"]
    success_url = reverse_lazy("profile_update_view")

# this will override the need for a pk or a slug from the Url and lets us delete get_queryset
    def get_object(self, queryset=None):
        return self.request.user.profile



class ChirpDeleteView(DeleteView):
    success_url = reverse_lazy("index")

    def get_queryset(self):
        return Chirp.objects.filter(bird=self.request.user)
