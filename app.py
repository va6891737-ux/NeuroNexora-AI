import streamlit as st

st.set_page_config(
    page_title="NeuroNexora AI",
    page_icon="🧠",
    layout="centered"
)
# 🌌 Futuristic AI Background

st.markdown("""
<style>
/* 🌈 Unique Topic Colors */

h1 {
    color: #00E5FF !important;
    text-shadow: 0 0 15px #00E5FF;
}

h2 {
    color: #8B5CF6 !important;
    text-shadow: 0 0 12px #8B5CF6;
}

h3 {
    color: #22D3EE !important;
}

/* Topic headings */
.topic-profile {
    color: #38BDF8;
}

.topic-analysis {
    color: #A78BFA;
}

.topic-recommendation {
    color: #34D399;
}

.topic-comparison {
    color: #FBBF24;
}

.topic-explainability {
    color: #F472B6;
}

.topic-score {
    color: #60A5FA;
}

.topic-dashboard {
    color: #C084FC;
}

.stApp {
    background:
        radial-gradient(circle at 80% 20%, rgba(0, 120, 255, 0.18), transparent 30%),
        radial-gradient(circle at 20% 80%, rgba(120, 0, 255, 0.15), transparent 30%),
        linear-gradient(135deg, #020617, #050b24, #020617);
    color: white;
}

/* Main headings */
h1, h2, h3 {
    color: #ffffff !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, #020617, #07132f, #020617);
    border-right: 1px solid rgba(0, 150, 255, 0.35);
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: #dbeafe !important;
}

/* Cards */
div.stAlert {
    background: rgba(10, 25, 60, 0.75);
    border: 1px solid rgba(0, 180, 255, 0.4);
    border-radius: 15px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #006eff, #7c3aed);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 24px;
    font-weight: bold;
    box-shadow: 0 0 15px rgba(0, 120, 255, 0.35);
}

.stButton > button:hover {
    box-shadow: 0 0 25px rgba(0, 180, 255, 0.7);
    transform: scale(1.02);
}

/* Metrics */
[data-testid="stMetric"] {
    background: rgba(10, 25, 60, 0.65);
    border: 1px solid rgba(0, 150, 255, 0.3);
    border-radius: 15px;
    padding: 15px;
}

/* Divider */
hr {
    border-color: rgba(0, 150, 255, 0.3);
}

</style>
""", unsafe_allow_html=True)

st.title("🧠 NeuroNexora AI")
st.subheader("Human-Centric Intelligent Decision Platform")

st.write(
    "An AI-assisted platform that helps users compare options "
    "and make informed decisions."
)

st.divider()

st.header("👤 User Profile")

education = st.selectbox(
    "Education",
    ["BCA", "BSc Computer Science", "B.Tech", "Other"]
)

budget = st.number_input(
    "Your Budget (₹)",
    min_value=0,
    value=50000,
    step=5000
)

time_available = st.slider(
    "Available Learning Time (Months)",
    1,
    24,
    6
)

skills = st.multiselect(
    "Your Skills",
    ["Python", "Java", "SQL", "HTML/CSS", "Data Analysis"]
)

goal = st.selectbox(
    "Your Career Goal",
    [
        "Software Engineer",
        "Data Analyst",
        "Web Developer"
    ]
)

if st.button("🔍 Analyze Decision"):

    if goal == "Software Engineer":
        recommendation = "Software Engineering"

    elif goal == "Data Analyst":
        recommendation = "Data Analytics"

    else:
        recommendation = "Web Development"

    st.success("Decision analysis completed!")

    st.header("🎯 Recommended Option")

    st.subheader(recommendation)

    st.write("### Why this recommendation?")

    if "Python" in skills:
        st.write("✓ Your Python skill supports this career path.")

    if "SQL" in skills:
        st.write("✓ Your SQL skill is useful for this option.")

    if time_available >= 6:
        st.write("✓ Your available learning time is suitable.")

    if budget <= 50000:
        st.write("✓ This option can be planned within your budget.")

    st.info(
        "NeuroNexora AI provides decision support. "
        "The final decision remains with the user."
    )
    # Step 4: Comparison Feature
st.header("📊 Compare Career Options")

comparison_data = {
    "Option": [
        "Software Engineering",
        "Data Analytics",
        "Web Development"
    ],
    "Required Skills": [
        "Python, SQL, DSA",
        "Python, SQL, Excel",
        "HTML, CSS, JavaScript"
    ],
    "Learning Time": [
        "6+ hours/week",
        "4–6 hours/week",
        "4–6 hours/week"
    ],
    "Difficulty": [
        "Medium",
        "Medium",
        "Beginner–Medium"
    ],
    "Career Scope": [
        "Software & IT",
        "Data & Business",
        "Web & IT"
    ]
}

st.dataframe(
    comparison_data,
    use_container_width=True,
    hide_index=True
)

st.info(
    "NeuroNexora AI helps users compare available options "
    "using multiple factors. The final decision remains with the user."
)
# Step 4 - Comparison Feature

st.header("📊 Compare Career Options")

st.write("Compare Software Engineering, Data Analytics, and Web Development side-by-side.")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("💻 Software Engineering")
    st.write("**Skills:** Python, Java, SQL, DSA")
    st.write("**Career:** Software Engineer")
    st.write("**Learning:** Medium to High")
    st.write("**Opportunities:** Software & IT Companies")

with col2:
    st.subheader("📈 Data Analytics")
    st.write("**Skills:** Python, SQL, Excel, Power BI")
    st.write("**Career:** Data Analyst")
    st.write("**Learning:** Medium")
    st.write("**Opportunities:** Analytics & Business")

with col3:
    st.subheader("🌐 Web Development")
    st.write("**Skills:** HTML, CSS, JavaScript")
    st.write("**Career:** Web Developer")
    st.write("**Learning:** Beginner to Medium")
    st.write("**Opportunities:** Websites & Web Apps")

st.subheader("📋 Side-by-Side Comparison")

comparison = {
    "Feature": [
        "Main Skills",
        "Career Role",
        "Learning Level",
        "Common Tools",
        "Project Type"
    ],
    "Software Engineering": [
        "Python / Java / SQL / DSA",
        "Software Engineer",
        "Medium–High",
        "VS Code, Git, GitHub",
        "Applications & Software"
    ],
    "Data Analytics": [
        "Python / SQL / Excel",
        "Data Analyst",
        "Medium",
        "Power BI, Excel",
        "Data & Reports"
    ],
    "Web Development": [
        "HTML / CSS / JavaScript",
        "Web Developer",
        "Beginner–Medium",
        "VS Code, Browser",
        "Websites & Web Apps"
    ]
}

st.table(comparison)
# Step 5 - Explainable AI

st.header("💡 Why This Recommendation?")

st.write(
    "NeuroNexora AI explains the factors considered "
    "before generating a recommendation."
)

reasons = []

if "Python" in skills:
    reasons.append("Your Python skill matches the selected career.")

if "SQL" in skills:
    reasons.append("Your SQL skill is useful for software and data-related roles.")

if time_available >= 6:
    reasons.append("Your available learning time supports regular skill development.")

if budget <= 50000:
    reasons.append("The selected option can be planned within a moderate budget.")

if not reasons:
    reasons.append(
        "The recommendation is based mainly on your selected career goal."
    )

for reason in reasons:
    st.write("✓", reason)

st.info(
    "The recommendation is generated from the information provided "
    "by the user. Users can review the comparison and make their own final decision."
)
# Step 6 - Decision Summary

st.header("📝 Decision Summary")

st.write("### 👤 Your Profile")

st.write("**Education:**", education)
st.write("**Budget:** ₹", budget)
st.write("**Learning Time:**", time_available)
st.write("**Skills:**", ", ".join(skills) if skills else "Not selected")
st.write("**Career Goal:**", goal)

st.write("### 🎯 AI-Assisted Decision")

if goal == "Software Engineer":
    final_option = "Software Engineering"
elif goal == "Data Analyst":
    final_option = "Data Analytics"
else:
    final_option = "Web Development"

st.success(
    f"Based on the information provided, "
    f"NeuroNexora AI suggests exploring **{final_option}**."
)

st.info(
    "This is an AI-assisted recommendation, not a mandatory decision. "
    "The user can review the factors and choose the option that best fits their needs."
)
# Step 6 - Decision Summary

st.header("📝 Decision Summary")

st.write("### 👤 Your Profile")

st.write("**Education:**", education)
st.write("**Budget:** ₹", budget)
st.write("**Learning Time:**", time_available)
st.write("**Skills:**", ", ".join(skills) if skills else "Not selected")
st.write("**Career Goal:**", goal)

st.write("### 🎯 AI-Assisted Decision")

# Step 11 - Improved Recommendation Logic

career_scores = {
    "Software Engineering": 0,
    "Data Analytics": 0,
    "Web Development": 0
}

# Goal
if goal == "Software Engineer":
    career_scores["Software Engineering"] += 40
elif goal == "Data Analyst":
    career_scores["Data Analytics"] += 40
else:
    career_scores["Web Development"] += 40

# Skills
if "Python" in skills:
    career_scores["Software Engineering"] += 20
    career_scores["Data Analytics"] += 20

if "Java" in skills:
    career_scores["Software Engineering"] += 20

if "SQL" in skills:
    career_scores["Software Engineering"] += 10
    career_scores["Data Analytics"] += 20

if "HTML/CSS" in skills:
    career_scores["Web Development"] += 25

if "Data Analysis" in skills:
    career_scores["Data Analytics"] += 25

# Select highest score
recommendation = max(
    career_scores,
    key=career_scores.get
)

st.success(
    f"Based on the information provided, "
    f"NeuroNexora AI suggests exploring **{final_option}**."
)

st.info(
    "This is an AI-assisted recommendation, not a mandatory decision. "
    "The user can review the factors and choose the option that best fits their needs."
)
# Step 8 - Final Decision Dashboard

st.header("🚀 NeuroNexora AI Dashboard")

st.write(
    "A complete overview of the user's profile, "
    "recommendation, comparison and decision score."
)

st.divider()

# Profile Summary
st.subheader("👤 User Profile")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Education", education)

with col2:
    st.metric("Career Goal", goal)

with col3:
    st.metric("Budget", f"₹{budget:,}")

st.divider()

# Recommendation
st.subheader("🎯 Recommended Path")

st.success(f"Recommended Option: {final_option}")

# Best score
best_score=90

st.metric(
    "Compatibility Score",
    f"{best_score}%"
)

st.progress(min(best_score, 100))

st.divider()

# Skills
st.subheader("🛠️ Selected Skills")

if skills:
    for skill in skills:
        st.write("✓", skill)
else:
    st.write("No skills selected.")

st.divider()

# Final message
st.subheader("💡 Final Decision Support")

st.info(
    "NeuroNexora AI combines user context, "
    "option comparison, explainability and scoring "
    "to support informed decision-making."
)

st.caption(
    "The platform provides decision support. "
    "The final decision always remains with the user."
)
# Step 9 - Professional Sidebar

with st.sidebar:
    st.header("🧠 NeuroNexora AI")

    st.write("### Human-Centric Intelligent Decision Platform")

    st.divider()

    st.write("**Platform Features**")

    st.write("👤 Personal Context")
    st.write("🔍 Decision Analysis")
    st.write("📊 Option Comparison")
    st.write("💡 Explainable AI")
    st.write("📈 Decision Scoring")
    st.write("🚀 Decision Dashboard")

    st.divider()

    st.write("### 🎯 Purpose")

    st.write(
        "To help users understand different options "
        "and make informed decisions using AI-assisted analysis."
    )

    st.divider()

    st.caption("NeuroNexora AI | Conference Project")
    # Step 12 - Visual Career Score Chart

st.header("📊 Career Compatibility Analysis")

st.write(
    "The chart shows the indicative compatibility score "
    "for each career option."
)

st.bar_chart(career_scores)

st.caption(
    "Scores are based on the information provided by the user "
    "and are intended only as decision-support information."
)
# Step 13 - Final Professional Dashboard

st.divider()

st.header("🏆 NeuroNexora AI – Final Decision Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎯 Recommended Path", recommendation)

with col2:
    st.metric("📊 Top Score", f"{max(career_scores.values())}%")

with col3:
    st.metric("🛠️ Skills Selected", len(skills))

st.divider()

st.subheader("📌 Decision Summary")

st.write("**Career Goal:**", goal)
st.write("**Recommended Option:**", recommendation)

st.write("### 📊 Career Scores")

for career, score in career_scores.items():
    st.write(f"**{career}: {score}%**")
    st.progress(min(score, 100))

st.success(
    "✅ NeuroNexora AI has completed the decision-support analysis."
)

st.info(
    "🧠 The platform analyzes user context, compares options, "
    "provides explainability and presents an indicative compatibility score. "
    "The final decision remains with the user."
)

