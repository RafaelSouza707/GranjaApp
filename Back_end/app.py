from helpers.application import app, api
from helpers.database import db
from resources.HomeResources import HomeResources

# adiciona recurso
api.add_resource(HomeResources, '/')


if __name__ == "__main__":
    app.run(debug=True)