from flask import Flask,render_template_string,render_template
from flask_restful import Api

from resource.product import ProductListResource
from resource.main import MainPageResource


app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string('<h1 style="text-align:center">Welcome Products API</h1>')

# Add "Flask Resource"
api=Api(app)
api.add_resource(MainPageResource,"/test")
api.add_resource(ProductListResource,"/products")


if __name__ == "__main__":

    app.run(port=5000,debug=True)