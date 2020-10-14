from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import DBSession

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config.include("cornice")
    config.scan('invoicing.views.invoice')
    return config.make_wsgi_app()
