# __init__.py để khởi tạo những thành phần cơ bản của web app khi bắt đầu

from flask import Flask

app = Flask(__name__,
            static_url_path='',
            static_folder='templates',
            template_folder='templates'
            )
app.config.from_object('config')

##########
from app import views