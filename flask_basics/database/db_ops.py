# Operate on the DB from db_models
from db_models import db, Puppy, Owner, Toy

# Only need for the first time
# db.create_all()

# Create 2 Puppies
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# Add Puppies to DB
db.session.add_all([rufus, fido])
db.session.commit()

# Check
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# Create owner Object
jose = Owner('Jose', rufus.id)

# Give Rufus some toys
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

# Grab Rufus after those additions
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

rufus.report_toys()