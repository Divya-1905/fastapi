from database import Base,engine
from models import Item,accounts,profile

print("Creating database ....")

Base.metadata.create_all(engine)
