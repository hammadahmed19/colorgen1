from django.urls import path
from colors.views import register_user, login_user, color_hash_list_create ,color_hash_update
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    
     
    path('get/', color_hash_list_create, name='colorhash-list-create'),
    path('add/', color_hash_list_create, name='colorhash-list-create'), #adding color hash
     path('get/<int:id>', color_hash_list_create, name='colorhash-list-create'), #getting by id
     
    path('update/<int:id>/', color_hash_update, name='colorhash-update'), #updating color hash by using id


    # JWT token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
