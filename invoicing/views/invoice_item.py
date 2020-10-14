
from cornice.resource import resource
import json
from invoicing.models import InvoiceItem, DBSession
from  dateutil import parser

@resource(collection_path='/invoice_item', path='/invoice_item/{id}')
class InvoiceView(object):

    def __init__(self, request):
        self.request = request

    def collection_get(self):
        return {
            'invoice_items': [
                {dict(item)}

                    for item in DBSession.query(InvoiceItem)
                    ]
            }

    def get(self):

        try:
            return DBSession.query(InvoiceItem).get(
                int(self.request.matchdict['id'])).to_json()
        except:
            return {}

    def collection_post(self):
        try:
            invoice_item = self.request.json
            DBSession.add(InvoiceItem.from_json(invoice_item))
            self.request.response.status_code = 201
            return invoice_item
        except Exception as e:
            return {'error': str(e)}
