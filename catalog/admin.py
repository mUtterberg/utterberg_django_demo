from django.contrib import admin

from .models import Book, Author, Genre, Language, BookInstance

# Minimal registration of Models:
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(BookInstance)

# Admin model classes

# Ended up defining inlines for associated models
class BooksInline(admin.TabularInline):
    """
    Defines format of inline book insertion (used in AuthorAdmin)
    """
    model = Book
    extra = 0

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    # Configure list view:
    list_display = (
        'last_name',
        'first_name',
        'date_of_birth',
        'date_of_death'
    )
    # Organize the detail view layout:
    fields = [
        'first_name',
        'last_name',
        ('date_of_birth', 'date_of_death')
    ]
    inlines = [BooksInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Inline associations make sense to add associated records simultaneously.
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# The following syntax accomplishes the same
# list view configurations for Book and BookInstance
# as the verbose definition from Author

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'display_genre'
    )
    # Displays inlines below detail view:
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """
    Administration object for BookInstance models.
    Defines:
     - fields to be displayed in list view (list_display)
     - filters that will be displayed in sidebar (list_filter)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ('book', 'status', 'borrower','due_back', 'id')
    list_filter = ('status', 'due_back')

    # Sectioning the detail view:
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )