from django.contrib import admin
from mysite.books.models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birth_date')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'publication_date')
	search_fields = ('title',)	
	list_filter = ('author',) 

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
