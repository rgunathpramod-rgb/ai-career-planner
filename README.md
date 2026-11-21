# 🎯 AI Career Planner — Build your first AI product

Techolas AI Wing weekend build. By Sunday 2 PM this will be **your** live AI app,
built by you and an AI coding assistant (GitHub Copilot).

## Day 1 setup (Checkpoint 1)
1. Click the green **Code** button → **Codespaces** → **Create codespace on main**. Wait ~2 minutes.
2. A preview of your app opens on the right. You should see "Hello!".
   No preview? Open the **Ports** tab at the bottom and click the globe next to port 8501.
   App not running? In the terminal type: `python -m streamlit run app.py --server.headless true`
3. Open **Copilot Chat** (the chat icon at the top or in the side bar) and switch it to **Agent** mode.
   Paste **Card 1** from `PROMPTS.md`. Press **Keep** to accept the change.
4. Get a free key at https://aistudio.google.com/apikey (sign in with Gmail → **Create API key** → copy).
5. In the file list, open `.streamlit/`, copy `secrets.toml.example`, rename the copy to `secrets.toml`,
   and paste your key between the quotes. Save (Ctrl+S). **Never paste your key into the Copilot chat.**

## How we build
- `PROMPTS.md` has a prompt card for every step. Copy a card into Copilot Chat (Agent mode).
- Test after every answer. **Two tries, then ask your helper to reset you.**
- `.github/copilot-instructions.md` holds the rules Copilot follows in this project. Don't delete it.

## Checkpoints (your reset buttons)
| Checkpoint | File | What works |
|---|---|---|
| 1 | `checkpoints/cp1_hello.py` (= starting `app.py`) | Hello page runs |
| 2 | `checkpoints/cp2_form.py` | The form collects your profile |
| 3 | `checkpoints/cp3_ai.py` | The AI writes your career plan as text |
| 4 | `checkpoints/cp4_product.py` | Resume upload, visual dashboard, download, follow-up chat |

Stuck? Copy the checkpoint file's contents into `app.py` and carry on from there.

## Day 2: go live (Checkpoint 5)
1. In the codespace, open **Source Control** (left bar), type a message like `ready to launch`,
   press **Commit**, then **Sync Changes**. Your code is now on GitHub (your key is not).
2. Go to https://share.streamlit.io and sign in with GitHub.
3. **Create app** → pick your `ai-career-planner` repo → main file `app.py`.
4. Open **Advanced settings → Secrets**, paste the same line as your `secrets.toml`:
   `GEMINI_API_KEY = "your-key"` → **Deploy**.
5. Open the link on your phone. That's your live AI product.
6. After you add your own feature (Card 6), Commit and Sync again: the live app updates by itself.

## Never share your key
`secrets.toml` is ignored by Git, so it is never pushed. Don't zip or email this folder with
`secrets.toml` inside. If a key is ever shared by mistake, delete it in AI Studio and make a new one.
