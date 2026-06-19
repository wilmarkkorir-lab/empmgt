from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    name = 'employees'
    
    def ready(self):
        # Apply Django compatibility patch for Python 3.14
        import django.template.context
        import copy
        
        def patched_copy(self):
            duplicate = self.__class__(self.dicts[:-1], 
                                      autoescape=self.autoescape, 
                                      use_l10n=self.use_l10n, 
                                      use_tz=self.use_tz)
            duplicate.template = self.template
            # Use deepcopy instead of copy() method
            duplicate.render_context = copy.deepcopy(self.render_context)
            return duplicate
            
        django.template.context.Context.__copy__ = patched_copy
