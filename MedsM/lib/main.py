from models import Medicine, User, session
from datetime import date

# Add some medicines
def add_medicine(name, category, quantity, expiry_date):
    medicine = Medicine(name=name, category=category, quantity=quantity, expiry_date=expiry_date, available=True)
    session.add(medicine)
    session.commit()

# Add a user
def add_user(username):
    user = User(username=username)
    session.add(user)
    session.commit()

# Search for medicines
def search_medicines(search_term):
    medicines = session.query(Medicine).filter(Medicine.name.ilike(f'%{search_term}%') | Medicine.category.ilike(f'%{search_term}%')).all()
    return medicines

# Mark a medicine as unavailable
def mark_medicine_unavailable(medicine_id):
    medicine = session.query(Medicine).get(medicine_id)
    if medicine:
        medicine.available = False
        session.commit()

# Remove expired medicines
def remove_expired_medicines():
    expired_medicines = session.query(Medicine).filter(Medicine.expiry_date < date.today()).all()
    for medicine in expired_medicines:
        session.delete(medicine)
    session.commit()

if __name__ == "__main__":
    # Example usage
    add_medicine("Paracetamol", "Painkiller", 100, date(2024, 6, 1))
    add_medicine("Amoxicillin", "Antibiotic", 50, date(2023, 12, 1))
    print(search_medicines("Paracetamol"))
    mark_medicine_unavailable(2)
