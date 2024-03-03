api_response = {
    "first_name": "Pramod",
    "age": 34,
    "last_name": "Dutta",
    "email": "pramoddutta@live.com",
    "password": "Test@4321",
    "commission": 10
}
print(api_response)
print(type(api_response))
print(api_response.get('password'))

api_response["password"] = "Pramod"
print(api_response)
print(api_response["password"])
print(api_response.get('password'))


for key, value in api_response.items():
    print(key, " => ", value)