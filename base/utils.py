from .models import Tag,Project
from django.db.models import Q

def searchProjects(request):
    search_query = ''

    if request.GET.get('query'):
        search_query = request.GET.get('query')
    
    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains = search_query) |
        Q(tags__in = tags)
    )
    return projects