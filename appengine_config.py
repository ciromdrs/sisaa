def webapp_add_wsgi_middleware(app):
    from engineauth import middleware
    return middleware.AuthMiddleware(app)

engineauth = {
    'secret_key': 'CHANGE_TO_A_SECRET_KEY',
    'user_model': 'engineauth.models.User',
}

engineauth['provider.auth'] = {
    'user_model': 'engineauth.models.User',
    'session_backend': 'datastore',
}

# Facebook settings for Development
FACEBOOK_APP_KEY = '343417275669983'
FACEBOOK_APP_SECRET = 'fec59504f33b238a5d7b5f3b35bd958a'

engineauth['provider.facebook'] = {
    'client_id': FACEBOOK_APP_KEY,
    'client_secret': FACEBOOK_APP_SECRET,
    'scope': 'email',
    }