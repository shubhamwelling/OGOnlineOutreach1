from django.contrib import admin
from django.urls import path, include

from blog.views import frontpage, post_detail, faq, index, events, second, home, search, suggestions, feedback, results
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('frontpage/', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('faq/',faq,name='faq'),
    path('results/',results,name='results'),
    path('feedback/',feedback,name='feedback'),
    path('suggestions/',suggestions,name="suggestions"),
    path('events/',events,name='events'),
    path('index/', index, name="index"),
    path('second/',second,name='second'),
    path('',home,name='home'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('search',search,name="search")


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )