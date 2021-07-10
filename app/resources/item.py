from flask_restful import Resource
from flask import request
from database.db import db

from database.models import ItemModel, ItemSchema

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
#
class ItemListResource(Resource):
    def get(self):
        items = ItemModel.query.all()
        return items_schema.dump(items)

    def post(self):
        new_post = ItemModel(
            title=request.json['title'],
            street=request.json['street']
        )
        db.session.add(new_post)
        db.session.commit()
        return item_schema.dump(new_post)


class ItemResource(Resource):
    def get(self, post_id):
        post = ItemModel.query.get_or_404(post_id)
        return item_schema.dump(post)

    def patch(self, post_id):
        post = ItemModel.query.get_or_404(post_id)

        if 'title' in request.json:
            post.title = request.json['title']
        if 'content' in request.json:
            post.content = request.json['content']

        db.session.commit()
        return item_schema.dump(post)

    def delete(self, post_id):
        post = ItemModel.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return '', 204





























#
#
#
# class Item(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('title',
#                         type=str,
#                         required=True,
#                         help="This field cannot be left blank!"
#                         )
#     parser.add_argument('street',
#                         type=str,
#                         required=True,
#                         help="Every item needs a store_id."
#                         )
#
#
#     def get(self, title):
#         item = ItemModel.find_by_name(title)
#         if item:
#             return item.json()
#         return {'message': 'Item not found'}, 404
#
#     def post(self, title):
#         if ItemModel.find_by_name(title):
#             return {'message': "An item with name '{}' already exists.".format(title)}, 400
#
#         data = Item.parser.parse_args()
#
#         item = ItemModel(title, **data)
#
#         try:
#             item.save_to_db()
#         except:
#             return {"message": "An error occurred inserting the item."}, 500
#
#         return item.json(), 201
#
#     def delete(self, title):
#         item = ItemModel.find_by_name(title)
#         if item:
#             item.delete_from_db()
#             return {'message': 'Item deleted.'}
#         return {'message': 'Item not found.'}, 404
#
#     def put(self, title):
#         data = Item.parser.parse_args()
#
#         item = ItemModel.find_by_name(title)
#
#         if item:
#             item.price = data['title']
#         else:
#             item = ItemModel(title, **data)
#
#         item.save_to_db()
#
#         return item.json()
#
#
# class ItemList(Resource):
#     def get(self):
#         items = ItemModel.query.all()
#         return posts_schema.dump(items)
#         # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
