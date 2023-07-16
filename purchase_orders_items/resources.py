from flask_restful import Resource, reqparse
from flask import jsonify 


purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido de Compra 1',
        'items': [
            {
                'id': 1,
                'description': 'Item do pedido 1',
                'price': 20.99   
            }
        ]

    }
]


class PurchaseOrdersItems(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'id',
        type=int,
        required=True,
        help="Informe um ID"
    )
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help="Informe uma descrição"
    )
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="Informe um preço"
    )

    def get(self, id):
        for po in purchase_orders:
            if po['id'] == id:
                return jsonify(po['items'])
        return jsonify({'message': 'Pedido {} não encontrado'.format(id)})  

    def post(self, id):
        req_data = PurchaseOrdersItems().parser.parse_args()
        for po in purchase_orders:
            if po['id'] == id:
                po['items'].append({
                'id': req_data['id'],
                'description': req_data['description'],
                'price': req_data['price']
                })
            return jsonify(po)
        return jsonify({'message': 'Pedido {} não encontrado'.format(id)})       



