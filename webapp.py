import streamlit as st
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Authenticate Google Drive
def authenticate_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication
    return GoogleDrive(gauth)

def upload_to_drive(file, drive, folder_id):
    """
    Upload a file to a specific Google Drive folder.
    :param file: The file object.
    :param drive: Authenticated GoogleDrive instance.
    :param folder_id: Google Drive folder ID where the file will be uploaded.
    """
    file_drive = drive.CreateFile({"parents": [{"id": folder_id}]})
    file_drive.SetContentFile(file)
    file_drive.Upload()
    return file_drive['id']

# Streamlit app
st.title("Photo Upload App")
st.write("Upload your photos, and they will be saved to a secure Google Drive folder.")

uploaded_file = st.file_uploader("Choose a photo to upload", type=["jpg", "jpeg", "png"])

google_drive_folder_id = "1t3DT5hxalNSHKbTAyOIFm0jDxZTdZLJQ"  # Replace with your Google Drive folder ID

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Photo", use_column_width=True)
    with st.spinner("Uploading to Google Drive..."):
        # Save the uploaded file locally
        local_file_path = os.path.join("temp", uploaded_file.name)
        with open(local_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Authenticate and upload to Google Drive
        drive = authenticate_drive()
        try:
            file_id = upload_to_drive(local_file_path, drive, google_drive_folder_id)
            st.success("Photo uploaded successfully!")
            st.write(f"File ID: {file_id}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
        finally:
            # Remove the temporary local file
            os.remove(local_file_path)
