from app import db
from typing import Dict

class TitanicPassenger(db.Model):
    """Model for Titanic passengers."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    sex = db.Column(db.String(10), index=True)
    age = db.Column(db.Integer, index=True)

    def __repr__(self) -> str:
        """Return a string representation of the TitanicPassenger."""
        return f"<TitanicPassenger {self.name}>"

    def as_dict(self) -> Dict[str, str]:
        """Convert the TitanicPassenger instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'sex': self.sex,
            'age': self.age
        }