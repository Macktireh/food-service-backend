import click
import warnings

from typing import Any, Dict, Literal, Tuple, Union
from werkzeug.exceptions import NotFound, Forbidden

from flask import render_template
from flask_migrate import Migrate
from flask_login import LoginManager
from flask.cli import with_appcontext
from flask_admin.menu import MenuLink

from app import create_app, db
from utils import status
from utils.cli import createsuperuserCli, testCli

# models
from models.user import User
from models.product import Product
from models.category import Category
from models.order import Order
from models.cart import Cart

# Admin
from admin.user import UserAdmin
from admin.product import ProductAdmin
from admin.category import CategoryAdmin
from admin.cart import CartAdmin
from admin.order import OrderAdmin

# routes
from admin.auth.login import admin_login
from routes import blueprint as blueprint_api

# create app flask
flask_app, admin = create_app('development')
migrate = Migrate(flask_app, db)

# save models in the admin panel
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', 'Fields missing from ruleset', UserWarning)
    admin.add_view(UserAdmin(User, db.session))
admin.add_view(ProductAdmin(Product, db.session))
admin.add_view(CategoryAdmin(Category, db.session))
admin.add_view(CartAdmin(Cart, db.session))
admin.add_view(OrderAdmin(Order, db.session))

# add menu items in the admin panel
admin.add_link(MenuLink(name='API Docs', category='', url="/api"))
admin.add_link(MenuLink(name='Logout', category='', url="/admin/user/logout"))

# register api routes
flask_app.register_blueprint(blueprint_api)
flask_app.register_blueprint(admin_login)

# flask login configuration
login_manager = LoginManager()
login_manager.init_app(flask_app)
login_manager.login_view = 'admin.login'


@login_manager.user_loader
def user_loader(id: Union[str, int]) -> User:
    return User.getById(int(id))

@login_manager.request_loader
def request_loader(request) -> None:
    return

@flask_app.route('/')
def home() -> Any:
    return render_template('home/home.html') 

@flask_app.errorhandler(status.HTTP_403_FORBIDDEN)
def forbidden(e: Forbidden) -> Tuple[Dict[str, str], Literal[403]]:
    return {
        "message": "Forbidden",
        "error": str(e),
    }, status.HTTP_403_FORBIDDEN

@flask_app.errorhandler(status.HTTP_404_NOT_FOUND)
def forbidden(e: NotFound) -> Tuple[Dict[str, str], Literal[404]]:
    return {
        "message": "Endpoint Not Found",
        "error": str(e),
    }, status.HTTP_404_NOT_FOUND


@click.command(name='createsuperuser')
@with_appcontext
def createsuperuser() -> None:
    """Create a super user"""
    createsuperuserCli()

@click.command(name='test')
@with_appcontext
def test() -> None:
    """Runs the unit tests."""
    testCli()

flask_app.cli.add_command(createsuperuser)
flask_app.cli.add_command(test)