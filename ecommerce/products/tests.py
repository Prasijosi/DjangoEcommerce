from django.test import TestCase
from datetime import datetime 

# Create your tests here.
class Message():
      def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

