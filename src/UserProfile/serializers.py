from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(read_only=True,many=False,view_name='user-detail')
    class Meta:
        model=Profile
        fields = ['url','id','user',
    'profile_first_name',
    'profile_middle_name',
    'profile_last_name',
    'country_code',
    'phone_number',
    'email',
    'gender',
    'marital_status',
    'alternate_phone_number',
    'website_link',
    'linkedin_link',
    'insta_user_id',
    'street_number',
    'city',
    'state',
    'country',
    'pincode',
    'father_first_name',
    'father_middle_name',
    'father_last_name',
    'mother_first_name',
    'mother_middle_name',
    'mother_last_name',
    'father_phone_number',
    'mother_phone_number',
    'tenth_board',
    'tenth_school_name',
    'tenth_year_of_passing',
    'twelfth_board',
    'twelfth_year_of_joining',
    'twelfth_year_of_passing',
    'college_name'
]



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = False)
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['url','id','username','first_name','last_name','email','password','profile']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        
        if password is None:
            password = User.objects.make_random_password()
        
        validated_data['password'] = make_password(password)
        user = super().create(validated_data)  # Use super() to call create method of the parent class
        
        # Optionally, store the temporary password
        user.temporary_password = password
        user.save()  # Saving again is not strictly necessary
        
        return user
    
    def update(self, instance, validated_data):
        # Check if 'password' is present in validated_data
        password = validated_data.pop('password', None)
        
        if password:
            validated_data['password'] = make_password(password)  # Hash the new password
        
        return super().update(instance, validated_data)