import datetime

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

# models
from django.db.models import Sum, Count
from sets_app.models import Boat, Set
# forms
from sets_app.forms import AddSetForm, AddRiderModelFrom

@login_required
def index(request):
    """View function for home page of app"""

    # Generate counts for sets and boats
    num_sets = Set.objects.all().count()
    num_boats = Boat.objects.all().count()

    # Counting number of total minutes
    num_min = Set.objects.aggregate(Sum('duration'))['duration__sum']

    # aggregating all info into context variable
    context = {
        'num_sets': num_sets,
        'num_boats': num_boats,
        'num_mins': num_min,
    }

    return render(request, 'index.html', context=context)

@login_required
def stats(request):
    """View function for stats page"""

    # query for all sets per boat
    query = list(Set.objects.values('boat_id').annotate(Sum('duration'), Count('id')))
    # getting boat ids from queries
    boat_ids = list(map(lambda d: d['boat_id'], query))
    boats = [Boat.objects.get(id=id_) for id_ in boat_ids]

    context = {
        'sets_query': query
    }

    return render(request, 'stats.html', context=context)


@login_required
def add_new_set(request):

    # if this is a POST request then process the form data
    if request.method == "POST":

        # create a AddSetForm form instance and populate it with data from teh request (binding)
        form = AddSetForm(request.POST)

        # check if form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data
            set_instance = Set(duration=form.cleaned_data["duration"],
                               driver=form.cleaned_data["driver"],
                               rider=form.cleaned_data["rider"],
                               boat=form.cleaned_data["boat"],
                               date_set=form.cleaned_data["date_set"])
            set_instance.save()

            # redirect to a new URL
            # TODO: add successfully added html page
            # return HttpResponseRedirect(reverse("set-added"))
            return HttpResponseRedirect(reverse("index"))

    # if this is a GET request create a default form
    else:
        # can only read from db and not write to it - currently not implemented!
        form = AddSetForm()
        # set_instance = None

    context = {
        'form': form,
        # 'set_instance': set_instance,
    }

    return render(request, 'sets_app/add_new_set.html', context)


@login_required
def add_new_rider(request):
    # if post request
    if request.method == "POST":
        form = AddRiderModelFrom(request.POST)
        # check if form is valid
        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect(reverse("index"))
    # if get request
    else:
        # pass
        form = AddRiderModelFrom()

    return render(request, 'sets_app/add_new_rider.html', {'form': form})
