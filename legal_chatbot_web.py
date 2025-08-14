
import streamlit as st


case_summaries = {
    "DK Basu Case": "DK Basu v. State of West Bengal (1997) established guidelines for arrests, custodial procedures, and the rights of detainees to prevent police excess.",
    "Maneka Gandhi Case": "Maneka Gandhi v. Union of India (1978) expanded Article 21, emphasizing personal liberty and due process.",
    "Kesavananda Bharati Case": "Kesavananda Bharati v. State of Kerala (1973) established the basic structure doctrine of the Indian Constitution.",
    "Arunachal Pradesh Case": "This case deals with the political administration and governance issues in Arunachal Pradesh, focusing on constitutional powers.",
    "Marbury v Madison": "A landmark US case establishing the principle of judicial review, allowing courts to declare laws unconstitutional.",
    "McDonald v Chicago": "A US case affirming the Second Amendment right to keep and bear arms applies to the states via the Fourteenth Amendment.",
    "Indira Gandhi Emergency Case": "The case addressed the constitutional validity of the Emergency and the suspension of fundamental rights in India.",
    "Vishaka v State of Rajasthan": "Vishaka Guidelines established procedures to prevent sexual harassment at the workplace.",
    "I.R. Coelho Case": "I.R. Coelho v. State of Tamil Nadu clarified the scope of judicial review for laws placed under the Ninth Schedule.",
    "Shreya Singhal Case": "Shreya Singhal v. Union of India (2015) struck down Section 66A of the IT Act as unconstitutional.",
    "S.R. Bommai Case": "S.R. Bommai v. Union of India defined limits of state governments under Article 356 of the Constitution.",
    "Naz Foundation Case": "Naz Foundation v. Govt. of NCT of Delhi (2009) read down Section 377 IPC, decriminalizing consensual same-sex relations.",
    "T.M.A. Pai Case": "T.M.A. Pai v. State of Karnataka dealt with rights of private educational institutions in India.",
    "Olga Tellis Case": "Olga Tellis v. Bombay Municipal Corporation recognized the right to livelihood under Article 21.",
    "Minerva Mills Case": "Minerva Mills v. Union of India reaffirmed the basic structure doctrine of the Constitution."
}



law_summaries = {
    "article 21": "Article 21 guarantees the right to life and personal liberty.",
    "article 19": "Article 19 guarantees the right to freedom of speech, expression, assembly, association, and movement.",
    "article 14": "Article 14 guarantees equality before the law and equal protection of the laws.",
    "section 420": "Section 420 of IPC deals with cheating and dishonestly inducing delivery of property.",
    "section 375": "Section 375 of IPC defines the offence of rape.",
    "section 498a": "Section 498A of IPC deals with cruelty by husband or relatives towards a married woman.",
    "section 34": "Section 34 IPC deals with acts done by several persons in furtherance of common intention.",
    "section 120b": "Section 120B IPC deals with criminal conspiracy.",
    "section 307": "Section 307 IPC deals with attempt to murder."
}


def chatbot_response(user_input):
    user_input_lower = user_input.lower().strip()
    
   
    if user_input_lower in ["hello", "hi", "hey"]:
        return "Welcome to the legal world!"
    
   
    if user_input_lower == "exit":
        return "Goodbye!"
    
   
    if user_input_lower in ["law summary", "laws"]:
        all_laws = [f"Law Summary: {summary}" for summary in law_summaries.values()]
        return "\n\n".join(all_laws)
    
    
    if user_input_lower in ["case summary", "cases"]:
        all_cases = [f"Case Summary: {summary}" for summary in case_summaries.values()]
        return "\n\n".join(all_cases)
    
    
    matching_cases = [f"Case Summary: {summary}" 
                      for key, summary in case_summaries.items()
                      if any(word in key.lower() for word in user_input_lower.split())]
    
   
    matching_laws = [f"Law Summary: {summary}" 
                     for key, summary in law_summaries.items()
                     if any(word in key.lower() for word in user_input_lower.split())]
    
   
    if matching_cases or matching_laws:
        return "\n\n".join(matching_cases + matching_laws)
    
    return "Sorry, I don't have information on that. Can you try another case or law?"



st.title("⚖️ Legal Chatbot")
st.write("Ask about Indian legal cases or laws. Type 'cases' or 'laws' to see all summaries. Type 'exit' to quit.")


user_input = st.text_input("You: ", "")

if user_input:
    response = chatbot_response(user_input)
    st.text_area("Bot:", value=response, height=300)
