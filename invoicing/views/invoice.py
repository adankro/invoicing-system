
from cornice.resource import resource
import json
from invoicing.models import Invoice, DBSession
from  dateutil import parser

@resource(collection_path='/invoice', path='/invoice/{id}')
class InvoiceView(object):

    def __init__(self, request):
        self.request = request

    def collection_get(self):
        return {
            'invoices': [
                {'id': invoice.id, 'date': str(invoice.date)}

                    for invoice in DBSession.query(Invoice)
                    ]
            }

    def get(self):

        try:
            return DBSession.query(Invoice).get(
                int(self.request.matchdict['id'])).to_json()
        except:
            return {}

    def collection_post(self):
        try:
            invoice = self.request.json
            date_str = invoice.get('date')
            invoice['date'] = parser.parse(date_str)
            DBSession.add(Invoice.from_json(invoice))
            invoice['date'] = date_str
            self.request.response.status_code = 201
            return invoice
        except Exception as e:
            return {'error': str(e)}
