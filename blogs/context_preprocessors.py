from .models import Category
from assignments.models import SocialLinks

def get_categories(request):
    return{
        "categories": Category.objects.all(),
    }
def get_social_links(request):
    return{
        "sociallinks": SocialLinks.objects.all()
    }