from django.urls import path

from blog.views import BlogViewSet 

url_view_set = {
    'blog': BlogViewSet,
}

url_view = [
    # path('deploy_action/', DeployAction.as_view(), {'method': 'action'}),
    # path('cost/', ProjectCost.as_view())
]