# run_app.py dùng để chạy chương trình

# Gọi object app từ __init__.py trong folder app
from app import app
import os

##########
if __name__ == '__main__':
    myPort = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=myPort)


