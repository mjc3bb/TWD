import os



os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, WebLink as Page, User, UserProfile

def populate():
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/",
         "views":20},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/",
         "views":10},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/",
         "views":300}
    ]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views":500},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/",
         "views":20},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/",
         "views":40}
    ]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/",
         "views":80},
        {"title": "Flask",
         "url": "http://flask.pocoo.org",
         "views":90}
    ]

    cats = {"Python": {"pages": python_pages,"views": 128, "likes": 64},
            "Django": {"pages": django_pages,"views": 64, "likes": 32},
            "Other Frameworks": {"pages": other_pages,"views": 32, "likes": 16},
            "No Category": {"pages":{},"views":300,"likes":20}}

    test_users = {"User1":{"username":"testuser2","email":"test@email.com","password":"testing" }}

    for cat, cat_data, in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"],p['views'])

    for usr, usr_data in test_users.items():
        add_userprofile(usr_data['username'],usr_data['email'],usr_data['password'], "http://www.url.com", None)


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views = views
    p.save()
    return p


def add_cat(name, views, likes):
    try:
        c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
        c.save()
    except django.db.utils.IntegrityError:
        c=None
    return c


def add_userprofile(username, email, password,website,picture=None):
    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        #user.save()
        user_profile = UserProfile.objects.get_or_create(website=website,picture=picture)[0]
        user_profile.save()
    except django.db.utils.IntegrityError:
        user_profile=None
    return user_profile


if __name__ == '__main__':
    print("Starting rango population script...")
    populate()
