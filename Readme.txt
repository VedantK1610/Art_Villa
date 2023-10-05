start virtual env:
    python -m venv my_env
    my_env\Static\activate

create photoshare:
    django-admin  startproject photoshare

create model named photos :
     python manage.py startapp photos 
     migrate
     modify app.py and include the app in photoshare/settings.py(installed apps)

create templates inside photos:
    add HTML and CSS

modify photos/views.py and give their urls

create superuser(admin)

create models in photos/models.py and mention them in admin.py

modify photoshare/settings.py include static and media urls 
mention them in photos/urls.py 

python manage.py collectstatic :- To create staticfiles folder

create categories on admin panel 
then import models in photos/views.py and add in views
then from views we can take it in our html file

now create add form (add.html):
    add method post to form
    then modify views.py with if req==post

no to filter images by categories:
    we need to add a tag in list with the ? line(gallery.html)   
    then go to views and add category=request.GET.get('category') in gallery(request)