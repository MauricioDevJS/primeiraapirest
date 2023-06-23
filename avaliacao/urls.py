from .views import *
from rest_framework.routers import SimpleRouter

routers = SimpleRouter()
routers.register('alunos', AlunosViewset)