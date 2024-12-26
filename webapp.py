import streamlit as st
import os

# Streamlit app
st.set_page_config(page_title="Photo Upload App", page_icon="📸", layout="centered")

# Title and description
st.title("📸 Photo Upload App")
st.markdown(
    """
    Welcome to the **Photo Upload App**! 🎉
    - Upload your favorite photos in JPG or PNG format.
    - Save them locally with just a click.
    """,
    unsafe_allow_html=True
)

# Upload section
uploaded_file = st.file_uploader(
    "Drag and drop or click to upload a photo:", type=["jpg", "jpeg", "png"],
    label_visibility="collapsed"
)

if uploaded_file is not None:
    st.markdown("### Preview of Your Photo")
    st.image(uploaded_file, caption="Uploaded Photo", use_column_width=True, output_format="auto")

    # Save button
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("**Photo Name:** " + uploaded_file.name)
    with col2:
        if st.button("💾 Save Photo"):
            with st.spinner("Saving your photo..."):
                # Save the uploaded file locally
                local_file_path = os.path.join("uploaded_photos", uploaded_file.name)
                os.makedirs("uploaded_photos", exist_ok=True)  # Create directory if it doesn't exist
                with open(local_file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.success(f"✅ Photo saved successfully! \n📁 Location: `{local_file_path}`")

# Footer
st.markdown(
    """
    ---
    Made with ❤️ using [Streamlit](https://streamlit.io/)
    """,
    unsafe_allow_html=True
)
