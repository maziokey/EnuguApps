
#from django.core.urlresolvers import reverse_lazy (old version of django)
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Applicant
from .forms import ApplicantForm
from .filters import ApplicantFilter

# Create your views here.
def home(request):
	#if request.user.is_authenticated:
	#	return redirect('epass_applicant_list')
	return render(request, 'epass/home.html')

@method_decorator([login_required], name='dispatch')
class ApplicantList(ListView):
	model = Applicant

@method_decorator([login_required], name='dispatch')
class ApplicantDetail(DetailView):
	model = Applicant

@method_decorator([login_required], name='dispatch')
class ApplicantCreate(CreateView):
	form_class = ApplicantForm
	model = Applicant

@method_decorator([login_required], name='dispatch')
class ApplicantUpdate(UpdateView):
	form_class = ApplicantForm
	model = Applicant
	template_name_suffix = '_form_update'

@method_decorator([login_required], name='dispatch')
class ApplicantDelete(DeleteView):
	model = Applicant
	success_url = reverse_lazy('epass_applicant_list')

"""
def search(request):
	applicant_list = Applicant.objects.all()
	applicant_filter = ApplicantFilter(request.GET, queryset=applicant_list)
	return render(request, 'epass/applicant_list.html', {'filter': applicant_filter})
"""