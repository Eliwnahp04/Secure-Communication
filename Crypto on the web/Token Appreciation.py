import base64
import json

# The JWT string
jwt_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3J5cHRve2p3dF9jb250ZW50c19jYW5fYmVfZWFzaWx5X3ZpZXdlZH0iLCJ1c2VyIjoiQ3J5cHRvIE1jSGFjayIsImV4cCI6MjAwNTAzMzQ5M30.shKSmZfgGVvd2OSB2CGezzJ3N6WAULo3w9zCl_T47KQ"

# Split the JWT into its three parts
header, payload, signature = jwt_token.split(".")

# Base64 decode the payload (it is URL-safe base64 encoded)
# We need to pad the base64 string to make sure it's valid
padding = '=' * (4 - len(payload) % 4)
payload += padding

decoded_payload = base64.urlsafe_b64decode(payload).decode('utf-8')

# Parse the decoded payload as JSON to read the content
payload_data = json.loads(decoded_payload)

# Print the decoded payload data (this is where you'll find the flag)
print(payload_data)
