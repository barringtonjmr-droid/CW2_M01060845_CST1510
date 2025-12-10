
class AIAssistant:
    """
    Manages message history only.
    (API calls handled by Streamlit app for streaming response.)
    """
    def __init__(self, system_prompt=None):
        self.__messages = []

        if system_prompt:
            self.__messages.append({
                "role": "system",
                "content": system_prompt
            })

    def add(self, role, content):
        self.__messages.append({"role": role, "content": content})

    def reset(self, system_prompt=None):
        self.__messages = []
        if system_prompt:
            self.__messages.append({"role": "system", "content": system_prompt})
