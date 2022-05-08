from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from aplicatie3.models import Jobs

# Create your views here.


class JobsView(LoginRequiredMixin, ListView):
    model = Jobs
    template_name = 'aplicatie3/jobs_index.html'
    paginate_by = 6


class CreateJobsView(LoginRequiredMixin, CreateView):
    model = Jobs
    fields = ['title', 'type', 'url', 'description', 'how_to_apply' ]
    template_name = 'aplicatie3/jobs_form.html'

    def get_success_url(self) -> str:
        return reverse('jobs:jobs_list')


class UpdateJobsView(LoginRequiredMixin, UpdateView):
    model = Jobs
    fields = ['title', 'type', 'url', 'description', 'how_to_apply']
    template_name = 'aplicatie3/jobs_form.html'

    def get_success_url(self) -> str:
        return reverse('jobs:jobs_list')


@login_required
def delete_job(request, pk):
    Jobs.objects.filter(id=pk).update(active=0)
    return redirect('jobs:jobs_list')


@login_required
def activate_job(request, pk):
    Jobs.objects.filter(id=pk).update(active=1)
    return redirect('jobs:jobs_list')
