from django.contrib import admin

from catalog.models import Book, Genre, Author, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Genre)


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


class BooksInline(admin.TabularInline):
    model = Book
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "display_genre"     # ManyToManyField -> large database access "cost"
    )
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("book", "status", "due_back", "id")
    list_filter = ("status", "due_back")
    fieldsets = (
        (None, {
            "fields": ("book", "imprint", "id")
        }),
        ("Availability", {
            "fields": ("status", "due_back")
        }),
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "last_name",
        "first_name",
        "date_of_birth",
        "date_of_death"
    )
    fields = [
        "first_name",
        "last_name",
        ("date_of_birth", "date_of_death")
    ]
    inlines = [BooksInline]

admin.site.register(Author, AuthorAdmin)
