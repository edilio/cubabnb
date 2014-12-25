from django.views.generic import TemplateView, DetailView
from django.shortcuts import render

from ..models import Property


def home(request):
    properties = Property.objects.all()
    return render(request, 'home.html', {'properties': properties})


class PropertyPageView(TemplateView):
    template_name = 'home.html'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super(PropertyPageView, self).get_context_data(**kwargs)

        p = self.request.GET.get('p')
        search_term = self.request.GET.get('search', '')
        # problems, prior, next_page, p = get_problems(self.request.user, p, term=search_term, category=category_name)
        context.update({
            # 'page': page,
            'properties': Property.objects.all(),
            # 'prior': prior,
            # 'next': next_page,
            # 'p': p,
            # 'previous_page': p - 1
        })
        return context


class PropertyDetail(DetailView):
    model = Property
    template_name = 'property_detail.html'
    http_method_names = ['get']
    context_object_name = 'property_obj'

    def get_context_data(self, **kwargs):
        context = super(PropertyDetail, self).get_context_data(**kwargs)

        return context