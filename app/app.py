from flask import Flask
from flask_restful import Api

from flask_admin import Admin
from flask_security import SQLAlchemyUserDatastore, Security

from helper.adminsecure import HomeSecurityView, AdminSecurityView
from database.models import *


from resources.item import ItemListResource, ItemResource
from database.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
api = Api(app)



@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(ItemResource, '/item/<string:title>')
api.add_resource(ItemListResource, '/items')

admin = Admin(app,  name='itemAdmin', template_mode='bootstrap3', index_view=HomeSecurityView(name='Home'))
admin.add_view(AdminSecurityView(ItemModel, db.session))
admin.add_view(AdminSecurityView(User, db.session))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
