import os
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

Base = declarative_base()

def get_database_engine():
    """Get database engine using environment variables."""
    db_url = os.environ.get('DATABASE_URL', 'sqlite:///db/medicine.db')
    return create_engine(db_url, echo=True)

engine = get_database_engine()
DBSession = sessionmaker(bind=engine)
session = DBSession()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)

    def buy_drug(self, medicine_name, quantity):
        medicine = session.query(Medicine).filter_by(name=medicine_name).first()
        if medicine and medicine.quantity >= quantity:
            updated_quantity = medicine.quantity - quantity
            session.query(Medicine).filter(Medicine.id == medicine.id).update({"quantity": updated_quantity})
            session.commit()
            return f"{quantity} units of {medicine_name} bought successfully"
        else:
            return "Medicine not available or insufficient quantity"

class Medicine(Base):
    __tablename__ = 'medicines'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    quantity = Column(Integer)
    expiry_date = Column(Date)
    available = Column(Boolean)

    def __repr__(self):
        return f"<Medicine(name='{self.name}', category='{self.category}', quantity='{self.quantity}', expiry_date='{self.expiry_date}', available='{self.available}')>"

    def mark_as_available(self):
        self.available = True

    def mark_as_unavailable(self):
        self.available = False

    def is_expired(self):
        return self.expiry_date < date.today()
    
    @classmethod
    def add_medicine(cls, name, category, quantity, expiry_date):
        medicine = cls(name=name, category=category, quantity=quantity, expiry_date=expiry_date, available=True)
        session.add(medicine)
        session.commit()
        
    @classmethod
    def search_medicines(cls, search_term):
        medicines = session.query(cls).filter(cls.name.ilike(f'%{search_term}%') | cls.category.ilike(f'%{search_term}%')).all()
        return medicines

    @classmethod
    def remove_expired_medicines(cls):
        expired_medicines = session.query(cls).filter(cls.expiry_date < date.today()).all()
        for medicine in expired_medicines:
            session.delete(medicine)
        session.commit()

    @classmethod
    def delete_medicine(cls, medicine_id):
        medicine = session.query(cls).get(medicine_id)
        if medicine:
            session.delete(medicine)
            session.commit()


class CategoryMedicine(Base):
    __tablename__ = 'category_medicine'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    medicine_id = Column(Integer, ForeignKey('medicines.id'))
    quantity = Column(Integer)
    
    category = relationship("Category", back_populates="medicines")
    medicine = relationship("Medicine", back_populates="categories")

class ExpiredMedicine(Base):
    __tablename__ = 'expired_medicine'
    id = Column(Integer, primary_key=True)
    medicine_id = Column(Integer, ForeignKey('medicines.id'))
    quantity = Column(Integer)
    
    medicine = relationship("Medicine", back_populates="expired")

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    medicines = relationship("CategoryMedicine", back_populates="category")
