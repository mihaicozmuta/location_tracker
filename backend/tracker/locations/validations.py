from rest_framework import serializers



def name_validator(name:str):
    if name is None:
        raise serializers.ValidationError("The name cannot be empty")
    return name

def mail_validator(mail:str):
    if '@' not in mail:
        raise serializers.ValidationError('This is not a vaild e-mail')
    if '.com' or '.ro' not in mail:
        raise serializers.ValidationError('This is not a valid e-mail')
    return mail 