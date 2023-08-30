def init_routes(app):
    from .user_routes import user
    with app.app_context():
        app.register_blueprint(user)
