"""
Patch for Django 4.2.x compatibility with Python 3.14.x
"""
import django.template.context


def patched_copy(self):
    """
    Patched __copy__ method for Context class to fix Python 3.14 compatibility
    """
    duplicate = self.__class__(self.dicts[:-1], 
                              autoescape=self.autoescape, 
                              use_l10n=self.use_l10n, 
                              use_tz=self.use_tz)
    duplicate.template = self.template
    duplicate.render_context = self.render_context.copy()
    return duplicate


# Apply the patch
django.template.context.Context.__copy__ = patched_copy