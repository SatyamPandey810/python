class DBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'api' and model._meta.model_name == 'product':
            return 'default'  
        if model._meta.app_label == 'api' and model._meta.model_name == 'order':
            return 'secondary' 
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'api' and model._meta.model_name == 'product':
            return 'default'
        if model._meta.app_label == 'api' and model._meta.model_name == 'order':
            return 'secondary'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'api' and model_name == 'product':
            return db == 'default'
        if app_label == 'api' and model_name == 'order':
            return db == 'secondary'
        return None