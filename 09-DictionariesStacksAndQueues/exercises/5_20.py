###
# Zapisuje dane pacjenta do pliku json
#
import json

# Słownik zawiera zagnieżdżone słowniki i listy (dane w kilku poziomach)
data = {
    "patient_record": {
        "patient_id": "P001234",
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "1985-05-15",
        "gender": "Male",
        "contact_info": {
            "phone_number": "+1-555-123-4567",
            "email": "johndoe@example.com",
            "address": {
                "street": "123 Main St",
                "city": "New York",
                "state": "NY",
                "postal_code": "10001",
                "country": "USA"
            }
        },
        "medical_history": {
            "allergies": ["Penicillin", "Peanuts"],
            "current_medications": ["Lisinopril 10mg", "Metformin 500mg"],
            "past_illnesses": ["Hypertension", "Type 2 Diabetes"],
            "surgeries": [
                {
                    "surgery_type": "Appendectomy",
                    "date": "2015-08-20"
                }
            ]
        }
    }
}

# Nazwa pliku, do którego zapisujemy
file_name = "patient.json"

# 'w' - zapis do pliku. json.dump() zapisuje słownik w formacie json,
# indent=4 sprawia, że plik jest czytelny (wcięcia po 4 spacje)
with open(file_name, 'w') as file:
    json.dump(data, file, indent=4)

print("Data has been written to", file_name)
