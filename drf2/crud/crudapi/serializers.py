from rest_framework import serializers
from .models import Student

#Model serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['name','roll','city']
        
    def validate_roll(self, value):
        print(value)
        if value>=110:
            raise serializers.ValidationError("Invalid Roll No.")
        return value
        

# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=200)
#     roll=serializers.IntegerField()
#     city=serializers.CharField(max_length=100)

#     def create(self,validate_data):
#         return Student.objects.create(**validate_data)
    
#     def update(self,instance,validate_data):
#         instance.name=validate_data.get('name',instance.name)
#         instance.roll=validate_data.get('roll',instance.roll)
#         instance.city=validate_data.get('city',instance.city)
#         instance.save()
#         return instance
#     # Field level validation
#     def validate_roll(self, value):#value is int not dict
#         print(value)
#         if value>=110:
#             raise serializers.ValidationError("Invalid Roll No.")
#         return value
#     def validate(self,data): #here data is dict
#         nm=data.get('name')
#         ct=data.get('city')
#         # do some validation
#         return data
