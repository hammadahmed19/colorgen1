from django.urls import path
from colors.views import register_user, login_user, color_hash_list_create ,color_hash_update
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    
    # Path for creating (POST) and retrieving (GET) color hashes
    path('get/', color_hash_list_create, name='colorhash-list-create'),
     path('get/<int:id>', color_hash_list_create, name='colorhash-list-create'),
    # Path for updating (PUT) and deleting (DELETE) color hashes by ID
    path('update/<int:id>/', color_hash_update, name='colorhash-update'),


    # JWT token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
