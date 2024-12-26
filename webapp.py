import streamlit as st
import os

# Streamlit app
st.title("Photo Upload App")
st.write("Upload your photos and save them locally.")

uploaded_file = st.file_uploader("Choose a photo to upload", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Photo", use_column_width=True)

    if st.button("Save Photo"):
        with st.spinner("Saving..."):
            # Save the uploaded file locally
            local_file_path = os.path.join("uploaded_photos", uploaded_file.name)
            os.makedirs("uploaded_photos", exist_ok=True)  # Create directory if it doesn't exist
            with open(local_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"Photo saved successfully! File saved at: {local_file_path}")
