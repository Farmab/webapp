import streamlit as st
import os

# Streamlit app
st.set_page_config(page_title="Photo Upload App", page_icon="📸", layout="centered")

# Custom CSS for modern UI
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom right, #f9f9f9, #e3f2fd);
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #6200ea;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 8px 16px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #3700b3;
    }
    .stMarkdown h1 {
        color: #1a237e;
        font-size: 2.5rem;
        font-weight: bold;
    }
    .uploaded-photo-preview {
        border: 2px solid #2196f3;
        border-radius: 8px;
        margin-top: 10px;
        padding: 10px;
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("📸 Photo Upload App")
st.markdown(
    """
    <div style="text-align: center; margin-top: -10px;">
        Welcome to the **Photo Upload App**! 🎉<br>
        Upload your favorite photos in JPG or PNG format.<br>
        Save them locally with just a click.
    </div>
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
    st.markdown("<div class='uploaded-photo-preview'>", unsafe_allow_html=True)
    st.image(uploaded_file, caption="Uploaded Photo", use_column_width=True, output_format="auto")
    st.markdown("</div>", unsafe_allow_html=True)

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
    <div style="text-align: center; margin-top: 50px;">
        <hr>
        <p>Made with ❤️ using <a href="https://streamlit.io/" target="_blank" style="color: #1a237e; text-decoration: none; font-weight: bold;">Streamlit</a></p>
    </div>
    """,
    unsafe_allow_html=True
)

