import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_reply(user_input, mood):
    prompt = f"""You're Vibe Diary, an AI friend. The user feels {mood}.
They wrote: \"{user_input}\"
Respond with empathy, humor, or support, like a close friend."""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a friendly, funny, emotionally aware AI."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Oops! Error: {e}"
