# frontend.py
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# -------------------------------
# Helpers
# -------------------------------
def parse_skill_input(skill_text: str):
    skills = {}
    for item in skill_text.split(","):
        if ":" in item:
            k, v = item.split(":")
            skills[k.strip()] = int(v.strip())
    return skills

# -------------------------------
# Login
# -------------------------------
if 'login' not in st.session_state:
    st.session_state['login'] = False

if not st.session_state['login']:
    st.title("🔐 Login to SkillSync")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username=="admin" and password=="admin123":
            st.session_state['login'] = True
        else:
            st.error("Invalid username/password")
    st.stop()

# -------------------------------
# Background
# -------------------------------
st.markdown("""
<style>
.stApp {
    background-image: url('https://images.unsplash.com/photo-1581091215369-4f1e58a7b4b2');
    background-size: cover;
}
</style>
""", unsafe_allow_html=True)

st.title("🎯 SkillSync Hackathon Edition")
menu = st.sidebar.selectbox("Select Option", ["Add Candidate","Add Internship","Add Project","Match Internship","Match Project"])

# -------------------------------
# Add Candidate
# -------------------------------
if menu=="Add Candidate":
    st.header("👤 Add Candidate")
    cid = st.number_input("Candidate ID", min_value=1)
    name = st.text_input("Candidate Name")
    skill_text = st.text_input("Enter Skills (normal format, e.g., Python:5, SQL:3)")
    if st.button("Submit Candidate"):
        skills = parse_skill_input(skill_text)
        r = requests.post(f"{API_URL}/add_candidate", json={"id":cid,"name":name,"skills":skills})
        st.success(r.json()["message"])

# -------------------------------
# Add Internship
# -------------------------------
elif menu=="Add Internship":
    st.header("📌 Add Internship")
    iid = st.number_input("Internship ID", min_value=1)
    title = st.text_input("Internship Title")
    skill_text = st.text_input("Required Skills (e.g., Python:40, SQL:20)")
    if st.button("Submit Internship"):
        skills = parse_skill_input(skill_text)
        r = requests.post(f"{API_URL}/add_internship", json={"id":iid,"title":title,"required_skills":skills})
        st.success(r.json()["message"])

# -------------------------------
# Add Project
# -------------------------------
elif menu=="Add Project":
    st.header("🛠 Add Project")
    pid = st.number_input("Project ID", min_value=1)
    title = st.text_input("Project Title")
    skill_text = st.text_input("Required Skills (e.g., Java:30, Spring:20)")
    if st.button("Submit Project"):
        skills = parse_skill_input(skill_text)
        r = requests.post(f"{API_URL}/add_project", json={"id":pid,"title":title,"required_skills":skills})
        st.success(r.json()["message"])

# -------------------------------
# Match Internship
# -------------------------------
elif menu=="Match Internship":
    st.header("📊 Match Candidates for Internship")
    iid = st.number_input("Enter Internship ID", min_value=1)
    if st.button("Run Internship Matching"):
        r = requests.get(f"{API_URL}/match_internship/{iid}")
        if "error" in r.json():
            st.error(r.json()["error"])
        else:
            for result in r.json():
                st.subheader(f"🏅 Rank {result['rank']} - {result['name']}")
                st.progress(result['match_score']/100)
                st.markdown(f"**Score:** {result['match_score']}%  |  **Performance:** {result['category']}")
                with st.expander("Skill Explanation"):
                    for e in result["explanation"]:
                        st.write("•", e)
                if result["category"]=="Top Performer 🟢":
                    st.balloons()

# -------------------------------
# Match Project
# -------------------------------
elif menu=="Match Project":
    st.header("🏆 Match Candidates for Project")
    pid = st.number_input("Enter Project ID", min_value=1)
    if st.button("Run Project Matching"):
        r = requests.get(f"{API_URL}/match_project/{pid}")
        if "error" in r.json():
            st.error(r.json()["error"])
        else:
            for result in r.json():
                st.subheader(f"🏅 Rank {result['rank']} - {result['name']}")
                st.progress(result['match_score']/100)
                st.markdown(f"**Score:** {result['match_score']}%  |  **Performance:** {result['category']}")
                with st.expander("Skill Explanation"):
                    for e in result["explanation"]:
                        st.write("•", e)
                if result["category"]=="Top Performer 🟢":
                    st.balloons()