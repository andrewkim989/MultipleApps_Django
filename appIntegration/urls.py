from django.conf.urls import url, include  

urlpatterns = [
    url(r'^', include("apps.home.urls")),
    url(r'^time/', include("apps.timedisplay.urls")),
    url(r'^words/', include("apps.words.urls")),
    url(r'^survey/', include("apps.surveyform.urls")),
    url(r'^courses/', include("apps.courses.urls")),
    url(r'^login/', include("apps.loginreg.urls"))
]
