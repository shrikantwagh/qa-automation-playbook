"""Utility for generating test data."""
from faker import Faker
from typing import Dict
import random
import string


class DataGenerator:
    """Generate test data for automation tests."""
    
    def __init__(self, locale: str = "en_US"):
        self.faker = Faker(locale)
    
    def generate_full_name(self) -> str:
        """Generate a random full name."""
        return self.faker.name()
    
    def generate_first_name(self) -> str:
        """Generate a random first name."""
        return self.faker.first_name()
    
    def generate_last_name(self) -> str:
        """Generate a random last name."""
        return self.faker.last_name()
    
    def generate_email(self) -> str:
        """Generate a random email address."""
        return self.faker.email()
    
    def generate_address(self) -> str:
        """Generate a random address."""
        return self.faker.address().replace('\n', ', ')
    
    def generate_phone_number(self) -> str:
        """Generate a random phone number."""
        return self.faker.phone_number()
    
    def generate_age(self, min_age: int = 18, max_age: int = 80) -> str:
        """Generate a random age."""
        return str(random.randint(min_age, max_age))
    
    def generate_salary(self, min_salary: int = 30000, max_salary: int = 150000) -> str:
        """Generate a random salary."""
        return str(random.randint(min_salary, max_salary))
    
    def generate_department(self) -> str:
        """Generate a random department name."""
        departments = [
            "Engineering",
            "QA",
            "Sales",
            "Marketing",
            "HR",
            "Finance",
            "Operations",
            "IT",
            "Legal",
            "Support"
        ]
        return random.choice(departments)
    
    def generate_random_string(self, length: int = 10) -> str:
        """Generate a random string."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    def generate_user_data(self) -> Dict[str, str]:
        """Generate complete user data."""
        return {
            "first_name": self.generate_first_name(),
            "last_name": self.generate_last_name(),
            "full_name": self.generate_full_name(),
            "email": self.generate_email(),
            "age": self.generate_age(),
            "salary": self.generate_salary(),
            "department": self.generate_department(),
            "current_address": self.generate_address(),
            "permanent_address": self.generate_address(),
            "phone": self.generate_phone_number()
        }
    
    def generate_text_box_data(self) -> Dict[str, str]:
        """Generate data for text box form."""
        return {
            "full_name": self.generate_full_name(),
            "email": self.generate_email(),
            "current_address": self.generate_address(),
            "permanent_address": self.generate_address()
        }
    
    def generate_table_record(self) -> Dict[str, str]:
        """Generate data for web table record."""
        return {
            "first_name": self.generate_first_name(),
            "last_name": self.generate_last_name(),
            "email": self.generate_email(),
            "age": self.generate_age(),
            "salary": self.generate_salary(),
            "department": self.generate_department()
        }
    
    def generate_multiple_records(self, count: int = 5) -> list:
        """Generate multiple table records."""
        return [self.generate_table_record() for _ in range(count)]


# Create a global instance
data_generator = DataGenerator()
