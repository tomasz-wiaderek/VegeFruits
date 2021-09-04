from django.shortcuts import render, get_list_or_404
from user_management.models import Profile, Voivodship, District
from .forms import SearchForm


def home(request):
    return render(request, 'site/home.html', context={})


def validate_location(model, form_cleaned_data):
    """Return all instances of given model if queryset is None."""
    if form_cleaned_data is None:
        form_cleaned_data = model.objects.all()
    return form_cleaned_data


def home_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            queryset = get_list_or_404(Profile, profile_type='producer',
                                       inventory__product__name__icontains=form.cleaned_data['product_name'],
                                       user__username__icontains=form.cleaned_data['producer_name'],
                                       # profilelocation__voivodship=form.cleaned_data['voivodship'],
                                       # profilelocation__district=form.cleaned_data['district'],
                                       # profilelocation__city__iexact=form.cleaned_data['city'],
                                       # profileadditionalinfo__delivery_available=form.cleaned_data['delivery_available']
                                       )
            context = {
                'profiles': set(queryset),
                }
            return render(request, 'search/profiles_list.html', context=context)
    else:
        form = SearchForm()
        context = {'search_form': form}
    return render(request, 'search/search.html', context=context)
