import phonenumbers

from phonenumbers import geocoder
phone_number = phonenumbers.parse("--Give your phone number--")

print("\nPhone numbers Location\n")

print(geocoder.description_for_number(phone_number,"en"));
