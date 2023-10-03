from project import create_app

app, celery = create_app()
app.app_context().push()

from project.lab.api import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)
    