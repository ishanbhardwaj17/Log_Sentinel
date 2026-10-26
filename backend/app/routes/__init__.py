"""
©AngelaMos | 2026
__init__.py

Blueprint registration for the Flask application

register_blueprints mounts the identity and access route blueprints
under the /v1 API prefix. Called by the application factory during
startup. Extended with further blueprints in later commits.

Key exports:
  register_blueprints - registers route blueprints on the Flask app
"""

from flask import Flask


API_PREFIX = "/v1"


def register_blueprints(app: Flask) -> None:
    """
    Register route blueprints under the API version
    """
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp

    app.register_blueprint(auth_bp, url_prefix = f"{API_PREFIX}/auth")
    app.register_blueprint(admin_bp, url_prefix = f"{API_PREFIX}/admin")
