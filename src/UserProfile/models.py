from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE,editable=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    MARITAL_STATUS_CHOICES = (
        ('Unmarried', 'Unmarried'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    )

    BOARD_CHOICES_10TH = (
        ('SSC', 'SSC'),
        ('CBSE', 'CBSE'),
        ('ICSE', 'ICSE'),
        ('Other', 'Other'),
    )

    BOARD_CHOICES_12TH = (
        ('CBSE', 'CBSE'),
        ('ICSE', 'ICSE'),
        ('Other', 'Other'),
    )

    Country_Codes = [
    ('+93', 'Afghanistan'),
    ('+355', 'Albania'),
    ('+213', 'Algeria'),
    ('+376', 'Andorra'),
    ('+244', 'Angola'),
    ('+1-268', 'Antigua and Barbuda'),
    ('+54', 'Argentina'),
    ('+374', 'Armenia'),
    ('+61', 'Australia'),
    ('+43', 'Austria'),
    ('+994', 'Azerbaijan'),
    ('+1-242', 'Bahamas'),
    ('+973', 'Bahrain'),
    ('+880', 'Bangladesh'),
    ('+1-246', 'Barbados'),
    ('+375', 'Belarus'),
    ('+32', 'Belgium'),
    ('+501', 'Belize'),
    ('+229', 'Benin'),
    ('+975', 'Bhutan'),
    ('+591', 'Bolivia'),
    ('+387', 'Bosnia and Herzegovina'),
    ('+267', 'Botswana'),
    ('+55', 'Brazil'),
    ('+673', 'Brunei'),
    ('+359', 'Bulgaria'),
    ('+226', 'Burkina Faso'),
    ('+257', 'Burundi'),
    ('+238', 'Cabo Verde'),
    ('+855', 'Cambodia'),
    ('+237', 'Cameroon'),
    ('+1', 'Canada'),
    ('+236', 'Central African Republic'),
    ('+235', 'Chad'),
    ('+56', 'Chile'),
    ('+86', 'China'),
    ('+57', 'Colombia'),
    ('+269', 'Comoros'),
    ('+242', 'Congo (Congo-Brazzaville)'),
    ('+506', 'Costa Rica'),
    ('+385', 'Croatia'),
    ('+53', 'Cuba'),
    ('+357', 'Cyprus'),
    ('+420', 'Czechia (Czech Republic)'),
    ('+45', 'Denmark'),
    ('+253', 'Djibouti'),
    ('+1-767', 'Dominica'),
    ('+1-809', 'Dominican Republic'),
    ('+1-829', 'Dominican Republic'),
    ('+1-849', 'Dominican Republic'),
    ('+593', 'Ecuador'),
    ('+20', 'Egypt'),
    ('+503', 'El Salvador'),
    ('+240', 'Equatorial Guinea'),
    ('+291', 'Eritrea'),
    ('+372', 'Estonia'),
    ('+268', 'Eswatini (fmr. "Swaziland")'),
    ('+251', 'Ethiopia'),
    ('+679', 'Fiji'),
    ('+358', 'Finland'),
    ('+33', 'France'),
    ('+241', 'Gabon'),
    ('+220', 'Gambia'),
    ('+995', 'Georgia'),
    ('+49', 'Germany'),
    ('+233', 'Ghana'),
    ('+30', 'Greece'),
    ('+1-473', 'Grenada'),
    ('+502', 'Guatemala'),
    ('+224', 'Guinea'),
    ('+245', 'Guinea-Bissau'),
    ('+592', 'Guyana'),
    ('+509', 'Haiti'),
    ('+504', 'Honduras'),
    ('+36', 'Hungary'),
    ('+354', 'Iceland'),
    ('+91', 'India'),
    ('+62', 'Indonesia'),
    ('+98', 'Iran'),
    ('+964', 'Iraq'),
    ('+353', 'Ireland'),
    ('+972', 'Israel'),
    ('+39', 'Italy'),
    ('+1-876', 'Jamaica'),
    ('+81', 'Japan'),
    ('+962', 'Jordan'),
    ('+7', 'Kazakhstan'),
    ('+254', 'Kenya'),
    ('+686', 'Kiribati'),
    ('+965', 'Kuwait'),
    ('+996', 'Kyrgyzstan'),
    ('+856', 'Laos'),
    ('+371', 'Latvia'),
    ('+961', 'Lebanon'),
    ('+266', 'Lesotho'),
    ('+231', 'Liberia'),
    ('+218', 'Libya'),
    ('+423', 'Liechtenstein'),
    ('+370', 'Lithuania'),
    ('+352', 'Luxembourg'),
    ('+261', 'Madagascar'),
    ('+265', 'Malawi'),
    ('+60', 'Malaysia'),
    ('+960', 'Maldives'),
    ('+223', 'Mali'),
    ('+356', 'Malta'),
    ('+692', 'Marshall Islands'),
    ('+222', 'Mauritania'),
    ('+230', 'Mauritius'),
    ('+52', 'Mexico'),
    ('+691', 'Micronesia'),
    ('+373', 'Moldova'),
    ('+377', 'Monaco'),
    ('+976', 'Mongolia'),
    ('+382', 'Montenegro'),
    ('+212', 'Morocco'),
    ('+258', 'Mozambique'),
    ('+95', 'Myanmar (formerly Burma)'),
    ('+264', 'Namibia'),
    ('+674', 'Nauru'),
    ('+977', 'Nepal'),
    ('+31', 'Netherlands'),
    ('+64', 'New Zealand'),
    ('+505', 'Nicaragua'),
    ('+227', 'Niger'),
    ('+234', 'Nigeria'),
    ('+850', 'North Korea'),
    ('+389', 'North Macedonia (formerly Macedonia)'),
    ('+47', 'Norway'),
    ('+968', 'Oman'),
    ('+92', 'Pakistan'),
    ('+680', 'Palau'),
    ('+970', 'Palestine'),
    ('+507', 'Panama'),
    ('+675', 'Papua New Guinea'),
    ('+595', 'Paraguay'),
    ('+51', 'Peru'),
    ('+63', 'Philippines'),
    ('+48', 'Poland'),
    ('+351', 'Portugal'),
    ('+974', 'Qatar'),
    ('+40', 'Romania'),
    ('+7', 'Russia'),
    ('+250', 'Rwanda'),
    ('+1-869', 'Saint Kitts and Nevis'),
    ('+1-758', 'Saint Lucia'),
    ('+1-784', 'Saint Vincent and the Grenadines'),
    ('+685', 'Samoa'),
    ('+378', 'San Marino'),
    ('+239', 'Sao Tome and Principe'),
    ('+966', 'Saudi Arabia'),
    ('+221', 'Senegal'),
    ('+381', 'Serbia'),
    ('+248', 'Seychelles'),
    ('+232', 'Sierra Leone'),
    ('+65', 'Singapore'),
    ('+421', 'Slovakia'),
    ('+386', 'Slovenia'),
    ('+677', 'Solomon Islands'),
    ('+252', 'Somalia'),
    ('+27', 'South Africa'),
    ('+82', 'South Korea'),
    ('+211', 'South Sudan'),
    ('+34', 'Spain'),
    ('+94', 'Sri Lanka'),
    ('+249', 'Sudan'),
    ('+597', 'Suriname'),
    ('+46', 'Sweden'),
    ('+41', 'Switzerland'),
    ('+963', 'Syria'),
    ('+886', 'Taiwan'),
    ('+992', 'Tajikistan'),
    ('+255', 'Tanzania'),
    ('+66', 'Thailand'),
    ('+670', 'Timor-Leste'),
    ('+228', 'Togo'),
    ('+676', 'Tonga'),
    ('+1-868', 'Trinidad and Tobago'),
    ('+216', 'Tunisia'),
    ('+90', 'Turkey'),
    ('+993', 'Turkmenistan'),
    ('+688', 'Tuvalu'),
    ('+256', 'Uganda'),
    ('+380', 'Ukraine'),
    ('+971', 'United Arab Emirates'),
    ('+44', 'United Kingdom'),
    ('+1', 'United States'),
    ('+598', 'Uruguay'),
    ('+998', 'Uzbekistan'),
    ('+678', 'Vanuatu'),
    ('+379', 'Vatican City'),
    ('+58', 'Venezuela'),
    ('+84', 'Vietnam'),
    ('+967', 'Yemen'),
    ('+260', 'Zambia'),
    ('+263', 'Zimbabwe')
]


    profile_first_name = models.CharField(max_length=50, blank=True, null=True)
    profile_middle_name = models.CharField(max_length=50, blank=True, null=True)
    profile_last_name = models.CharField(max_length=50, blank=True, null=True)
    country_code = models.CharField(max_length=6, choices=Country_Codes, default="+91")
    phone_number = models.CharField(max_length=15, blank=True , null= True)
    email = models.EmailField(max_length=45, blank=True , null= True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M', blank=True , null= True)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES, default = "Unmarried", blank=True , null= True)
    alternate_phone_number = models.CharField(max_length=15, blank=True , null= True)
    website_link = models.URLField( blank=True , null= True)
    linkedin_link = models.URLField( blank=True , null= True)
    insta_user_id = models.CharField(max_length=50, blank=True , null= True)
    street_number = models.CharField(max_length=100, blank=True , null= True)
    city = models.CharField(max_length=100, blank=True , null= True)
    state = models.CharField(max_length=100, blank=True , null= True)
    country = models.CharField(max_length=100, blank=True , null= True)
    pincode = models.CharField(max_length=10, blank=True , null= True)
    father_first_name = models.CharField(max_length=50, blank=True , null= True)
    father_middle_name = models.CharField(max_length=50, blank=True , null= True)
    father_last_name = models.CharField(max_length=50, blank=True , null= True)
    mother_first_name = models.CharField(max_length=50, blank=True , null= True)
    mother_middle_name = models.CharField(max_length=50, blank=True , null= True)
    mother_last_name = models.CharField(max_length=50, blank=True , null= True)
    father_phone_number = models.CharField(max_length=15, blank=True , null= True)
    mother_phone_number = models.CharField(max_length=15, blank=True , null= True)
    tenth_board = models.CharField(max_length=10, choices=BOARD_CHOICES_10TH, blank=True , null= True)
    tenth_school_name = models.CharField(max_length=100, blank=True , null= True)
    tenth_year_of_passing = models.IntegerField(blank=True , null= True)
    twelfth_board = models.CharField(max_length=10, choices=BOARD_CHOICES_12TH, blank=True , null= True)
    twelfth_year_of_joining = models.IntegerField( blank=True , null= True)
    twelfth_year_of_passing = models.IntegerField(blank=True , null= True)
    college_name = models.CharField(max_length=100, blank=True , null= True)
    
    def __str__(self):
        return f"{self.user.username}\'s Profile"
    
