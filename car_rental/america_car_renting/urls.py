from django.urls import include, path
from . import views  # from the same path
from . import api

urlpatterns = [
    # path("", views.StartingPageView.as_view(), name="starting-page"),
    # path("posts", views.AllPostsView.as_view(), name="posts-page"),
    # path("posts/<slug:slug>", views.SingleCarView.as_view(),
    #      name="cars-detail-page"),  # /posts/my-first-post
    path('',views.index,name='index'),
    path('api/vehicle/<int:pk>',api.VehicleDetails.as_view(),name='vehicle-detail'),
    # path('api/owner/top-5-with-most-vehicles',api.OwnerWithMostVehicles.as_view()),
    path('api/vehicles',api.VehicleList.as_view()),
    path('api/owner/top5',api.OwnerWithMostVehicles),
    path('api/owner/top10',api.StatListView.as_view()),
        
]
