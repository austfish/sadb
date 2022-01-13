# sadb
安全资产与配置中心

## wsl2
sudo chown -R alaia /home/alaia/

## django
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

python3 manage.py migrate

python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('sadb', 'root@ohlinge.cn', 'sadb') if not User.objects.filter(username='gosint').exists() else 0"

python3 manage.py runserver

## simpleui
python3 manage.py collectstatic