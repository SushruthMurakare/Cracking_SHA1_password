import phonenumbers


from phonenumbers import geocoder
country_history = phonenumbers.parse("type_a_phone_number_with_country_code", "CH")
print(geocoder.description_for_number(country_history, "en"))

from phonenumbers import carrier
service_provider = phonenumbers.parse("type_a_phone_number_with_country_code", "RO")
print(carrier.name_for_number(service_provider, "en"))