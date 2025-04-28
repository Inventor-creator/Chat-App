
from flask import request
from master import app
from master import routes


if __name__ == "__main__":
   
    app.run(host='0.0.0.0' ,
            debug=True,
            port=8080)