from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        # 导入 myapp.models 模块，以便在应用程序启动时执行模型定义
        import blog.models
