from sqlalchemy import Column, Integer, String, Float, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from app import app
import dao

db = SQLAlchemy(app)


class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255), nullable=True)
    price = Column(Float, default=0)
    image = Column(String(255), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        # categories = dao.load_categories()
        # for c in categories:
        #     db.session.add(Category(name=c['name']))
        prods = dao.load_products()
        for p in prods:
            prod = Product(name=p['name'], description=p['description'], price=p['price'], image=p['image'],
                           category_id=p['category_id'])
            db.session.add(prod)
        db.session.commit()
