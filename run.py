import os
from myapp import app

app.main_dir = os.path.dirname(__file__)

if __name__=='__main__':
    app.run()
