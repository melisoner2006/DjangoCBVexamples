"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from myformapp.models import Contact

     
class ContactTests(TestCase):
    def test_str(self):
        contact = Contact(first_name='John', last_name='Smith')
        self.assertEquals(
                      str(contact),
                      'John Smith'
                      )
    
 