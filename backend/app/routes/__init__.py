"""
©AngelaMos | 2026
__init__.py

Blueprint registration for the Flask application

register_blueprints mounts the identity, event-data, and dashboard
route blueprints under the /v1 API prefix. Called by the application
factory during startup. Extended with further blueprints in later commits.

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
    from app.routes.logs import logs_bp
    from app.routes.alerts import alerts_bp
    from app.routes.dashboard import dashboard_bp

    app.register_blueprint(auth_bp, url_prefix = f"{API_PREFIX}/auth")
    app.register_blueprint(admin_bp, url_prefix = f"{API_PREFIX}/admin")
    app.register_blueprint(logs_bp, url_prefix = f"{API_PREFIX}/logs")
    app.register_blueprint(alerts_bp, url_prefix = f"{API_PREFIX}/alerts")
    app.register_blueprint(dashboard_bp, url_prefix = f"{API_PREFIX}/dashboard")
