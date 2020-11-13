

from flask import redirect, render_template, request, Flask
from werkzeug.exceptions import BadRequest, NotFound 

import models 

app = Flask(__name__, template_folder='views')

@app.route("/")
def index():
    ''' show main page '''
    return render_template('main_page.html')

if __name__ == '__main__':
    app.run(debug=True)

