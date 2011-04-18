from django.views.generic.simple import direct_to_template


def base(request):
    return direct_to_template(request, 'base.html',
                              extra_context={'request': request})