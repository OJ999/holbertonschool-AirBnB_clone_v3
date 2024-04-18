#!/usr/bin/python3
"""Module for the BaseModel class."""
import uuid
from datetime import datetime

class BaseModel:
    """Base class for all models in the AirBnB clone project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    # Other common methods (e.g., to_dict, __str__, etc.)
