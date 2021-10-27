import json

sampleJson = """{
    "company": {
        "employee": {
            "name": "emma",
            "payable": {
                "salary": 7000,
                "bonus": 800
            }
        }
    }
}"""


jsonFile = json.loads(sampleJson)
testFile = jsonFile["company"]["employee"]["birthday"] = "1995-12-30"
json_file = "my_file.json"

with open(json_file, 'w') as file_obj:
    json.dump(sampleJson, file_obj)

