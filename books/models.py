from django.db import models
from users.models import User

class Author(models.Model):
    COUNTRY_NAME_CHOICES = [
    ('SL','Select Country Name') ,  
    ('BD', 'Bangladesh'),
    ('IN', 'India'),
    ('US', 'United States'),
    ('CA', 'Canada'),
    ('AU', 'Australia'),
    ('GB', 'United Kingdom'),
    ('CN', 'China'),
    ('JP', 'Japan'),
    ('DE', 'Germany'),
    ('FR', 'France'),
    ('BR', 'Brazil'),
    ('ZA', 'South Africa'),
    ('RU', 'Russia'),
    ('MX', 'Mexico'),
    ('IT', 'Italy'),
    ('ES', 'Spain'),
    ('NG', 'Nigeria'),
    ('AR', 'Argentina'),
    ('SA', 'Saudi Arabia'),
    ('KR', 'South Korea'),
    ('ID', 'Indonesia'),
    ('TR', 'Turkey'),
    ('EG', 'Egypt'),
    ('PK', 'Pakistan'),
    ('NL', 'Netherlands'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('BE', 'Belgium'),
    ('PL', 'Poland'),
    ('MY', 'Malaysia'),
    ('PH', 'Philippines'),
    ('TH', 'Thailand'),
    ('IR', 'Iran'),
    ('IQ', 'Iraq'),
    ('VN', 'Vietnam'),
    ('IL', 'Israel'),
    ('NO', 'Norway'),
    ('FI', 'Finland'),
    ('NZ', 'New Zealand'),
    ('SG', 'Singapore'),
    ('AE', 'United Arab Emirates'),
    ('GR', 'Greece'),
    ('PT', 'Portugal'),
    ('CZ', 'Czech Republic'),
    ('HU', 'Hungary'),
    ('AT', 'Austria'),
    ('DK', 'Denmark'),
    ('IE', 'Ireland'),
    ('CL', 'Chile'),
    ('RO', 'Romania'),
    ('KE', 'Kenya'),
]
    image=models.ImageField(
        upload_to='author_image/',
        blank=True,
        null=True
    )
    name= models.CharField(max_length=255)
    bio=models.TextField(blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    country=models.CharField(
        max_length=30,
        choices=COUNTRY_NAME_CHOICES,
        default='SL',
        )
    
    def __str__(self):
        return self.name
   

class BookCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    
class Book(models.Model):
    LANGUAGE_NAME_CHOICES = [
    ('BD', 'Bangla'),
    ('PK', 'Urdu'),
    ('LN', 'Select Book Language'),
    ('IN', 'Hindi'),
    ('EN', 'English'),
    ('FR', 'French'),
    ('ES', 'Spanish'),
    ('DE', 'German'),
    ('CN', 'Mandarin'),
    ('JP', 'Japanese'),
    ('RU', 'Russian'),
    ('IT', 'Italian'),
    ('PT', 'Portuguese'),
    ('AR', 'Arabic'),
    ('KR', 'Korean'),
    ('TR', 'Turkish'),
]
    image = models.ImageField(
        upload_to='book_image/',
        blank=True,
        null=True 
    )
    
    title = models.CharField(max_length=255)
    entry_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, null=True, blank=True)
    isbn = models.CharField(max_length=13)
    published_date = models.DateField()
    language=models.CharField(
        max_length=30,
        choices=LANGUAGE_NAME_CHOICES,
        default='LN',
        )
    available_copies = models.IntegerField()
    
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title