
import streamlit as st
from openai import OpenAI
from openai import APIError, RateLimitError, APITimeoutError

from app.services.ai_assistant import AIAssistant  


client = OpenAI(api_key=st.secrets["OPEN_API_KEY"])

def ask_chatgpt_stream(messages, model="gpt-4o"):
    """Generator function that yields streaming text chunks."""
    try:
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True
        )

        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    except RateLimitError:
        yield "\n:warning: **Rate limit reached. Please try again shortly.**"

    except APITimeoutError:
        yield "\n:hourglass: **The request timed out.**"

    except APIError as api_err:
        yield f"\n:x: **API Error:** {str(api_err)}"

    except Exception as e:
        yield f"\n:rotating_light: **Unexpected error:** {str(e)}"


st.set_page_config(
    page_title=":robot:Chat GPT Assistant",
    page_icon=":speech_balloon:",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.error("You must log in first. Go to the Login page from the sidebar.")
    st.stop()

st.title(":speech_balloon: Multi AI Assistant")
st.caption("Powered by GPT-4o")


SYSTEM_PROMPT = """You are a cybersecurity expert assistant.
-Analyse incidents and threats
-Provide technical guidance
-Explain attack vectors and mitigations
-Use standard terminology (MITRE ATT&CK, CVE)
-Priortize actionable recommendations
Tone: Professional, Technical
Format: Clear, structured responses
"""

if "assistant" not in st.session_state:
    st.session_state.assistant = AIAssistant(system_prompt=SYSTEM_PROMPT)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]



with st.sidebar:
    st.subheader("Chat controls")

    msg_count = len([m for m in st.session_state.messages if m["role"] != "system"])
    st.metric("Messages", msg_count)

    if st.button(":wastebasket: Clear chat"):
        st.session_state.assistant.reset(system_prompt=SYSTEM_PROMPT)
        st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        st.rerun()

    model = st.selectbox(
        "Model",
        ["gpt-4o", "gpt-4o-mini"],
        index=0
    )



for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])




prompt = st.chat_input("Ask about cybersecurity...")

if prompt:

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.assistant.add("user", prompt)

    # Start assistant reply
    with st.chat_message("assistant"):
        container = st.empty()
        full_reply = ""

        with st.spinner("Thinking..."):
            for chunk in ask_chatgpt_stream(
                st.session_state.messages,
                model=model
            ):
                full_reply += chunk
                container.markdown(full_reply)

        container.markdown(full_reply)

    # Save final reply
    st.session_state.messages.append({
        "role": "assistant",
        "content": full_reply
    })
