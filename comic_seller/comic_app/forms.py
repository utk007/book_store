from django.forms import ModelForm
from comic_app.models import Books


class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ['name', 'description', 'comic_pic']