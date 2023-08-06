from .models import *
from modeltranslation.translator import TranslationOptions,register,translator
    
    
    
class PostTranslationOptions(TranslationOptions):
    fields = ('read_time', 'title', 'body','summary')

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    
class ResumeTranslationOptions(TranslationOptions):
    fields = ('body','interest')
    
translator.register(Post, PostTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Resume, ResumeTranslationOptions)