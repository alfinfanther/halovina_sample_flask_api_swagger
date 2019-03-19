from flask import Flask
from flask import jsonify
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Sembako API',
    description='Sembako API V 1.0',
)
smbk = api.namespace('sembako', description='Sembako API')
produk_model = smbk.model('Sembako',{
    'id': fields.Integer(required=True, description='The sembako identifier'),
    'product_name': fields.String(required=True, description='The sembako product name'),
    'jumlah': fields.String(required=True, description='The sembako jumlah')
})

produk = [
	{
		'id':1,
		'product_name':'kacang panjang',
		'jumlah':'1kg'
	},
	{
		'id':2,
		'product_name':'kacang tanah',
		'jumlah':'1kg'
	},
	{
		'id':3,
		'product_name':'buncis',
		'jumlah':'1kg'
	}
]
 
@app.route('/')
def hello_world():
    return jsonify({'message':'hello world'})

@smbk.route('/produk')
class Produk_all(Resource):
    @smbk.doc('get_produk_model')
    @smbk.marshal_with(produk_model)
    def get(self):
        return produk

@smbk.route('/produk/<int:id>')
@smbk.param('id','id identifier')
class Produk_by_id(Resource):
    @smbk.doc('get_produk_model')
    @smbk.marshal_with(produk_model)
    def get(self, id):
        data = {}
        for x in produk:
            if x['id'] == id:
                data = {
                    'id': x['id'],
                    'product_name': x['product_name'],
                    'jumlah': x['jumlah']
                }
        return data

if __name__ == "__main__":
    app.run(host='0.0.0.0')