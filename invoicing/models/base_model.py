
class BaseModel():
    __tablename__ = None
    @classmethod
    def from_json(cls, data):
        return cls(**data)
