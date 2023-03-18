"""crime_investigation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib import admin
from comment.views import CreateComment
from comment.views import HomePage, CommentPage
from home.views import criminal_directory
from home.views import upload_evidence
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from police.views import person_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', TemplateView.as_view(template_name="about.html")),
    path('contact', TemplateView.as_view(template_name="contact.html")),
    path('police/', include('police.urls')),
    path('anonymous/', include('home.url_anonymous')),
    path('citizen/', include('citizen.urls')),
    path('comment/ajax/create', CreateComment, name = "create_comment"),
    path('comment/', CommentPage, name = "comment"),
    path('criminal_directory/', criminal_directory, name = "criminal_directory"),
    path('evidence/<int:id>/upload', upload_evidence, name = "upload_anonymous_evidence"),
    path('person_detail/<int:id>/', person_detail_view, name='person_detail'),

    path('', HomePage, name = "HomePage")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

