from basic_app import db, Puppy

# Create ALl the ables Model --> DB table
db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Frank', 4)

# Should see None for now
print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])
#db.session.add(sam)
# Save to DB
db.session.commit()

# Should see the id now
print(sam.id)
print(frank.id)
