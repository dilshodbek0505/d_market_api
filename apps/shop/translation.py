from modeltranslation.translator import register, TranslationOptions

from .models import Category, Product, ProductSize


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    
    
@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

    
@register(ProductSize)
class ProductSizeTranslationOptions(TranslationOptions):
    fields = ('name', )