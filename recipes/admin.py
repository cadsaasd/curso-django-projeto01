from django.contrib import admin
from .models import Category, Recipe, Author

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...

class RecipeAdmin(admin.ModelAdmin):
    ...

class AuthorAdmin(admin.ModelAdmin):
    ...


admin.site.register(Author, AuthorAdmin)

admin.site.register(Recipe, RecipeAdmin)

admin.site.register(Category, CategoryAdmin)