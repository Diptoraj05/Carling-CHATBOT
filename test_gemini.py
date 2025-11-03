import google.generativeai as genai

# Replace with your actual API key
genai.configure(api_key="AIzaSyAIOAPSW-r7xEOOgJDNcjTOEsxVE4tKFrE")

print("Listing available models...\n")

for m in genai.list_models():
    print(m.name)