import streamlit as st


st.title("Legal Chatbot")
st.subheader("Created by Anish LS. Tamang – Your Legal AI Assistant")


cases_and_laws = {
    "maneka gandhi": "Maneka Gandhi vs Union of India (1978): Landmark judgment on personal liberty under Article 21.",
    "kesavananda bharati": "Kesavananda Bharati vs State of Kerala (1973): Introduced the Basic Structure Doctrine.",
    "golaknath": "Golaknath vs State of Punjab (1967): Parliament cannot amend Fundamental Rights.",
    "indira gandhi vs raj narain": "Indira Gandhi vs Raj Narain (1975): Election petition case.",
    "article 21": "Article 21 of the Indian Constitution: Protection of life and personal liberty.",
    "article 19": "Article 19: Freedom of speech, expression, assembly, and association.",
    "section 420": "Section 420 IPC: Cheating and dishonestly inducing delivery of property.",
    "section 406": "Section 406 IPC: Punishment for criminal breach of trust.",
    "section 375": "Section 375 IPC: Defines rape and consent.",
    "section 302": "Section 302 IPC: Punishment for murder.",
    "section 307": "Section 307 IPC: Attempt to murder.",
    "section 34": "Section 34 IPC: Acts done by several persons in furtherance of common intention.",
    "section 498a": "Section 498A IPC: Cruelty by husband or relatives of husband towards a woman.",
    "section 138": "Section 138 NI Act: Dishonor of cheque for insufficiency of funds.",
    "section 3": "Section 3 PDPP Act: Damage to public property."
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in cases_and_laws:
        if key in user_input:
            return cases_and_laws[key]
    return "I don't have information on that. Ask me about judgments or laws."


user_input = st.text_input("You:")
if user_input:
    response = chatbot_response(user_input)
    st.text("Bot: " + response)

 About Creator button
if st.button("About Creator"):
    st.info("This Legal Chatbot was created by Anish Tamang, an Advocate and AI enthusiast.")
