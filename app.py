from flask import Flask, request, render_template
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.ai.inference.models import TextContentItem, ImageContentItem, ImageUrl
from azure.storage.blob import BlobServiceClient, ContentSettings
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

api_key = os.getenv('AZURE_API_KEY')
endpoint = os.getenv('AZURE_ENDPOINT')

connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = os.getenv('AZURE_STORAGE_CONTAINER_NAME')

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(api_key)
)

def upload_image_to_blob(blob_service_client, container_name, image):
    try:
        container_client = blob_service_client.create_container(container_name)
    except Exception:
        container_client = blob_service_client.get_container_client(container_name)

    blob_name = image.filename
    blob_client = container_client.get_blob_client(blob_name)

    
    content_type = "image/jpeg" if blob_name.endswith(".jpg") or blob_name.endswith(".jpeg") else "image/png"

    blob_client.upload_blob(image, overwrite=True, content_settings=ContentSettings(content_type=content_type))

    return blob_client.url

def get_image_description(image_url, context=""):
    system_message = SystemMessage(content="You are an AI assistant that generates detailed step-by-step testing instructions based on images provided.")
    
    user_message = [
        TextContentItem(text=f"Please generate test cases for the following image. The test case should follow this format:\n"
                             "1. Description: What is the test case about?\n"
                             "2. Pre-conditions: What needs to be set up or ensured before testing?\n"
                             "3. Testing Steps: Clear, step-by-step instructions on how to perform the test.\n"
                             "4. Expected Result: What should happen if the feature works correctly.\n"
                             f"{context}")
    ]
    
    user_message.append(ImageContentItem(image_url=ImageUrl(url=image_url)))
    
    response = client.complete(
        messages=[
            system_message,
            UserMessage(content=user_message)
        ],
        temperature=0,
        top_p=1,
        max_tokens=2048
    )
    
    return response.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        context = request.form.get('context', "")
        uploaded_files = request.files.getlist("images")
        
        # list to store results for each image
        all_responses = []
        
        
        for image in uploaded_files:
            # Upload the image to Azure Blob Storage and get the URL
            image_url = upload_image_to_blob(blob_service_client, container_name, image)
            
            
            response = get_image_description(image_url, context)
        
            # Store the result for each image
            all_responses.append(f"Result for {image.filename}:\n{response}\n")
        
        final_response = "\n".join(all_responses)
        
        return render_template("index.html", response=final_response)
    
    return render_template("index.html", response="")

if __name__ == "__main__":
    app.run(debug=True)
