import streamlit as st

# Set up the page style
st.set_page_config(page_title="My Unlimited Routine Tracker", page_icon="⚡", layout="centered")
st.title("⚡ My Personal Routine Dashboard")
st.write("100% Free, Unlimited Tasks & Routines")

# 1. DEFINE YOUR UNLIMITED ROUTINES HERE
# You can add as many routines and tasks as you want!
ROUTINES = {
    "Morning Glow & Brain": [
        "Lavage doux (CeraVe Vert) sur peau humide 🧼",
        "Sérum Vitamine C + Crème hydratante légère ☀️",
        "Chess.com Daily Puzzle (Train your mind) 🧩"
    ],
    "Evening Chill": [
        "CeraVe Vert + Heavy Moisturizer on cheeks 🧴",
        "Crochet session / TikTok content prep 🧶",
        "Review chess mistakes or play a beginner bot 🤖"
    ],
    "Workout Day": [
        "Pre-workout hydration & stretch 💧",
        "Weightlifting session (Progressive overload focus) 🏋️‍♀️",
        "Post-workout protein refuel 🍗"
    ]
}

# 2. Routine Selection Dropdown
selected_routine = st.selectbox("Choose a routine to run:", list(ROUTINES.keys()))
tasks = ROUTINES[selected_routine]

st.divider()

# 3. Track progress using Streamlit's session state
if "checked_tasks" not in st.session_state or st.session_state.get("current_routine") != selected_routine:
    st.session_state["checked_tasks"] = {task: False for task in tasks}
    st.session_state["current_routine"] = selected_routine

# Display the checklist and calculate score
completed_count = 0
for task in tasks:
    # Checkbox logic
    is_checked = st.checkbox(task, value=st.session_state["checked_tasks"][task], key=f"{selected_routine}_{task}")
    st.session_state["checked_tasks"][task] = is_checked
    if is_checked:
        completed_count += 1

# 4. Math & Visual Progress Bars
total_tasks = len(tasks)
progress_percentage = int((completed_count / total_tasks) * 100) if total_tasks > 0 else 0

st.divider()
st.subheader("Progress")
st.progress(progress_percentage / 100)
st.write(f"📊 **{progress_percentage}% Completed** ({completed_count}/{total_tasks} tasks)")

# Success Celebration Logic
if completed_count == total_tasks:
    st.balloons()
    st.success("🔥 Sequence Complete! Level up!")
