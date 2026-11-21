# CHECKPOINT 3 — "Connect the AI"  (Day 1, 12:10 session)
# The form now sends the profile to Gemini with a carefully written prompt
# and shows the plan as text. Day 2 turns this into a visual product (Checkpoint 4).
# It uses the same page layout as the final app, so the look never changes.

import streamlit as st
from google import genai
from google.genai import errors, types

MODEL = "gemini-2.5-flash"  # Check in AI Studio the week before; swap if a newer free Flash model is listed.

SYSTEM_PROMPT = """You are a friendly, honest career counsellor for students and job seekers in India.
Given a person's profile, reply in Markdown with exactly these sections:

## 3 roles that fit you
For each role: the title, one line on why it fits this person, and a typical entry-level
salary range in India in LPA, labelled "indicative".

## Your skill gaps
A table with columns: Skill | Why it matters | Free resource to start.
List 4 to 6 skills, most important first.

## Your 90-day roadmap
Three blocks: Days 1-30, Days 31-60, Days 61-90. Each block has 3 concrete weekly tasks
that fit the hours per week they gave, and ends with one small project to build.

## One thing to do today
A single action they can finish in under 30 minutes.

Rules: be encouraging but realistic, never promise a job or a salary, use simple English,
and keep the whole answer under 450 words."""

st.set_page_config(page_title="AI Career Planner", page_icon="🎯", layout="centered")

# A little CSS (page styling), the same as every checkpoint.
st.markdown(
    """
    <style>
    [data-testid="stMainBlockContainer"] { max-width: 1000px; padding-top: 2.5rem; }
    .hero { text-align: center; margin-bottom: 1.5rem; }
    .hero h1 { font-size: 2.6rem; margin-bottom: 0.2rem; }
    .hero p { color: #475569; font-size: 1.1rem; margin: 0; }
    .step { color: #2563EB; font-weight: 600; font-size: 0.85rem;
            letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 0.3rem; }
    .footer { text-align: center; color: #64748B; font-size: 0.85rem; padding: 0.5rem 0 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
      <h1>🎯 AI Career Planner</h1>
      <p>Tell me about yourself. I'll suggest roles, skill gaps and a 90-day plan.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# The profile form, laid out in two columns
with st.form("profile"):
    st.markdown('<div class="step">About you</div>', unsafe_allow_html=True)
    left, right = st.columns(2)
    name = left.text_input("Your name")
    education = right.selectbox(
        "Highest education",
        ["Plus Two / 12th", "Diploma", "B.Tech / B.E.", "B.Sc / BCA",
         "B.Com / BBA", "BA", "Master's degree", "Other"],
    )
    status = st.radio(
        "Where are you right now?",
        ["Student", "Graduate looking for a job", "Working, want to switch", "Career break"],
        horizontal=True,
    )
    left, right = st.columns(2)
    skills = left.text_area("Skills you already have", placeholder="Excel, basic Python, communication...")
    interests = right.text_area("What do you enjoy?", placeholder="Solving puzzles, design, talking to people...")
    goal = st.text_input("Your goal", placeholder="Get my first job in tech within 6 months")
    hours = st.slider("Hours per week you can study", 2, 40, 10)
    submitted = st.form_submit_button("🚀 Plan my career", type="primary", width="stretch")


def build_profile():
    return (
        f"Name: {name}\nEducation: {education}\nCurrent status: {status}\n"
        f"Skills: {skills}\nInterests: {interests}\nGoal: {goal}\n"
        f"Hours per week available: {hours}"
    )


def ask_ai(profile):
    """Send the profile and the prompt to Gemini and return its answer as text."""
    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"],
        # google-genai 3.x defaults to the v1 API, which rejects system_instruction.
        http_options=types.HttpOptions(api_version="v1beta"),
    )
    response = client.models.generate_content(
        model=MODEL,
        contents=profile,
        config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT, temperature=0.7),
    )
    return response.text


def friendly_error(e):
    """Turn a technical error into a message a beginner can act on."""
    if isinstance(e, KeyError):
        return "No API key found. Check .streamlit/secrets.toml (Checkpoint 1 step 4)."
    if isinstance(e, errors.APIError) and e.code in (429, 500, 503, 504):
        return "Gemini is very busy or the free limit is reached. Wait a minute and try again."
    return f"Something went wrong: {e}"


if submitted:
    missing = []
    if not name.strip():
        missing.append("**Your name**")
    if not goal.strip():
        missing.append("**Your goal**")
    if not skills.strip():
        missing.append("**Skills you already have**")
    if missing:
        st.warning("Please fill in: " + ", ".join(missing) + ". The grey example text does not count.")
    else:
        error = None
        with st.spinner("Thinking about your career..."):
            try:
                plan = ask_ai(build_profile())
            except Exception as e:
                error = friendly_error(e)
        if error:
            st.error(error)
        else:
            with st.container(border=True):
                st.markdown(plan)

st.divider()
st.markdown(
    '<div class="footer">Built at the Techolas AI Wing weekend · AI suggestions, not guarantees.</div>',
    unsafe_allow_html=True,
)
