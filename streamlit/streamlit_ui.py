
import streamlit as st
import httpx

st.title("Model Evaluation Viewer")


option = st.selectbox(
    "Choose what to display:",
    ("Confusion Matrix", "Accuracy")
)

with httpx.Client() as client:
    response = client.get("http://127.0.0.1:8000/confusionMatrix")
    if response.status_code == 200:
        data = response.json()
        confusion = data["confusion"]
        accuracy = data["accuracy"]
    else:
        st.error("Failed to fetch confusion matrix.")
        st.stop()


if option == "Confusion Matrix":
    st.subheader("Confusion Matrix")
    st.json(confusion)
elif option == "Accuracy":
    st.subheader("Model Accuracy")
    st.write(f"Accuracy: {accuracy:.2f}")
