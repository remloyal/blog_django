# blog

创建虚拟环境
python -m virtualenv venv

启动项目
python manage.py runserver  
python manage.py runserver 0.0.0.0:8000

创建应用
python manage.py startapp app


迁移数据库
python manage.py makemigrations

初始化Django数据库
python manage.py migrate


生成requirements.txt文件
pip freeze > requirements.txt

安装requirements.txt依赖
pip install -r requirements.txt