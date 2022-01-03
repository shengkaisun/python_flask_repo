from basic_app import db, Puppy

# Create a new entry
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

# Read
all_puppies = Puppy.query.all()
print(all_puppies)

# Select by ID
puppy_one = Puppy.query.get(1)

# Filters
puppy_frank = Puppy.query.filter_by(name='Frank')
print(puppy_frank.all())

# Update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# Delete
third_puppy = Puppy.query.get(3)
db.session.delete(third_puppy)
db.session.commit()

# Check the latest data
all_puppies = Puppy.query.all()
print(all_puppies)