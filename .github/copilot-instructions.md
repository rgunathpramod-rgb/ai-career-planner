# Rules for this project (read by GitHub Copilot)

This is a beginner's AI app built at a Techolas AI Wing weekend workshop.
The person prompting you has never coded before. Keep things simple and safe.

## Stack
- One file: `app.py`. Do not create other Python files unless the user asks.
- Only use `streamlit` and `google-genai` (already installed, versions in requirements.txt).
  Do not add libraries. Do not run `pip install` or any other terminal command.
- Keep the existing page style (the CSS block), the hero title and the footer.

## Calling Gemini (use exactly this pattern)
```python
from google import genai
from google.genai import types

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"],
    http_options=types.HttpOptions(api_version="v1beta"),  # required with google-genai 3.x
)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=...,
    config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT, temperature=0.7),
)
```
- If a model is busy (errors 429, 500, 503, 504), retry once, then try `gemini-2.5-flash-lite`.
- For structured answers use `response_mime_type="application/json"` and a `response_schema`.

## Safety rules (never break these)
- NEVER write an API key in the code. Always read it with `st.secrets["GEMINI_API_KEY"]`.
- Never print or display secrets.
- Uploaded files (like a resume PDF) stay in memory. Never save them to disk.
- The AI must never promise a job or a salary. Salaries are always labelled "indicative".

## Streamlit habits
- Save results in `st.session_state` so they stay on screen when the page reruns.
- Wrap AI calls in try/except and show a friendly `st.error` message instead of crashing.
- Show a spinner while waiting for the AI.

## How to answer
- Make the change directly in `app.py`.
- Add short comments in simple English above each new section.
- After the change, explain in 3 short lines: what you changed, and what to click to test it.
