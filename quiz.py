import streamlit as st
import random
from supabase import create_client

SUPABASE_URL = "https://nfuzcvjkjniwnbaorsjp.supabase.co"

SUPABASE_KEY = "sb_publishable_udgXeZZ8k-IqjAB7Nzpqng_M_RSMOAw"


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)
# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="2026 AKGMA Onam Quiz",
    page_icon="🌸",
    layout="centered"
)


# =========================================================
# CUTE ONAM THEME
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #fffaf0;
}

h1, h2, h3 {
    text-align: center;
}

.quiz-box {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    border: 2px solid #f4c542;
    margin-top: 20px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# QUIZ QUESTIONS - UNDER 10
# =========================================================

quiz_dict_10 = [
    {"question": "Which festival is celebrated in Kerala in honour of King Mahabali?", "answer": "Onam"},
    {"question": "Who is the king associated with Onam?", "answer": "Mahabali"},
    {"question": "What is the flower decoration made during Onam called?", "answer": "Pookalam"},
    {"question": "What is the traditional Onam feast called?", "answer": "Sadya"},
    {"question": "Which state is famous for celebrating Onam?", "answer": "Kerala"},
    {"question": "What leaf is Sadya usually served on?", "answer": "Banana leaf"},
    {"question": "Which animal is painted on performers during Pulikali?", "answer": "Tiger"},
    {"question": "What sweet dish is commonly eaten during Onam?", "answer": "Payasam"},
    {"question": "What type of decoration is a Pookalam made from?", "answer": "Flowers"},
    {"question": "Which god is connected with the story of Mahabali?", "answer": "Vishnu"},
    {"question": "What was the name of Vishnu's form that visited Mahabali?", "answer": "Vamana"},
    {"question": "What is the traditional boat race of Kerala called?", "answer": "Vallam Kali"},
    {"question": "What are Kerala's long racing boats often called?", "answer": "Snake boats"},
    {"question": "What is the most important day of Onam called?", "answer": "Thiruvonam"},
    {"question": "What is the first day of Onam called?", "answer": "Atham"},
    {"question": "What colour is commonly associated with traditional Kerala clothing?", "answer": "White"},
    {"question": "What colour is the border of a traditional Kasavu saree?", "answer": "Gold"},
    {"question": "What traditional Kerala dance has performers dressed as tigers?", "answer": "Pulikali"},
    {"question": "Which fruit is commonly used to make banana chips?", "answer": "Banana"},
    {"question": "What is the Malayalam word for a boat?", "answer": "Vallam"},
    {"question": "Which famous Kerala art form uses colourful costumes and makeup?", "answer": "Kathakali"},
    {"question": "Which instrument is commonly used in Kerala festivals?", "answer": "Chenda"},
    {"question": "What vegetable dish made with different vegetables is served during Sadya?", "answer": "Avial"},
    {"question": "What dish made with lentils and vegetables is often served during Sadya?", "answer": "Sambar"},
    {"question": "What crispy snack made from banana is often served during Sadya?", "answer": "Banana chips"},
    {"question": "What sweetener is used to make Sharkara Varatti?", "answer": "Jaggery"},
    {"question": "What is the traditional swing used during Onam celebrations called?", "answer": "Oonjal"},
    {"question": "What did Vamana ask Mahabali for?", "answer": "Three steps of land"},
    {"question": "What is the name of the day before Thiruvonam?", "answer": "Uthradam"},
    {"question": "What is the biggest festival celebrated in Kerala?", "answer": "Onam"}
]


# =========================================================
# QUIZ QUESTIONS - UNDER 20
# =========================================================

quiz_dict_20 = [
    {"question": "Which festival is celebrated in Kerala in honour of King Mahabali?", "answer": "Onam"},
    {"question": "Who is the legendary king associated with Onam?", "answer": "Mahabali"},
    {"question": "What is the flower decoration made during Onam called?", "answer": "Pookalam"},
    {"question": "What is the traditional feast eaten during Onam called?", "answer": "Sadya"},
    {"question": "Which Indian state is most famous for celebrating Onam?", "answer": "Kerala"},
    {"question": "What leaf is an Onam Sadya traditionally served on?", "answer": "Banana leaf"},
    {"question": "Which sweet dish is commonly served during an Onam Sadya?", "answer": "Payasam"},
    {"question": "Which god is connected to the story of King Mahabali?", "answer": "Vishnu"},
    {"question": "What avatar of Vishnu is associated with the story of Onam?", "answer": "Vamana"},
    {"question": "What type of decoration is a Pookalam?", "answer": "Flower carpet"},
    {"question": "What traditional Kerala boat race is famous during the Onam season?", "answer": "Vallam Kali"},
    {"question": "What are the long boats used in Kerala boat races called?", "answer": "Snake boats"},
    {"question": "What is the most important day of Onam called?", "answer": "Thiruvonam"},
    {"question": "What is the first day of the main ten-day Onam celebration called?", "answer": "Atham"},
    {"question": "Which traditional performance features people painted like tigers?", "answer": "Pulikali"},
    {"question": "What traditional garment is commonly worn by men in Kerala?", "answer": "Mundu"},
    {"question": "What traditional garment is commonly worn by women during Onam?", "answer": "Kasavu saree"},
    {"question": "What colour is traditionally associated with the border of a Kasavu saree?", "answer": "Gold"},
    {"question": "Which Kerala dance form is known for elaborate costumes and face makeup?", "answer": "Kathakali"},
    {"question": "What traditional Kerala drum is often played during festivals?", "answer": "Chenda"},
    {"question": "What mixed vegetable dish is commonly served during Sadya?", "answer": "Avial"},
    {"question": "What lentil-based dish is commonly served during Sadya?", "answer": "Sambar"},
    {"question": "What is the Malayalam word for a boat?", "answer": "Vallam"},
    {"question": "What traditional Kerala martial art is called?", "answer": "Kalaripayattu"},
    {"question": "What is the Malayalam calendar called?", "answer": "Kollavarsham"},
    {"question": "Which river hosts the famous Nehru Trophy Boat Race?", "answer": "Punnamada River"},
    {"question": "What is the famous annual boat race held on Punnamada Lake called?", "answer": "Nehru Trophy Boat Race"},
    {"question": "What dish made with yoghurt and vegetables is served during Sadya?", "answer": "Kaalan"},
    {"question": "Which day comes immediately after Atham?", "answer": "Chithira"},
    {"question": "Which day comes immediately after Chithira?", "answer": "Chodhi"}
]


# =========================================================
# QUIZ QUESTIONS - OVER 20
# =========================================================

quiz_dict_20_plus = [
    {"question": "Which festival is celebrated in Kerala in honour of King Mahabali?", "answer": "Onam"},
    {"question": "Who is the legendary king associated with Onam?", "answer": "Mahabali"},
    {"question": "What is the flower decoration made during Onam called?", "answer": "Pookalam"},
    {"question": "What is the traditional feast eaten during Onam called?", "answer": "Sadya"},
    {"question": "Which Indian state is most famous for celebrating Onam?", "answer": "Kerala"},
    {"question": "What leaf is a traditional Sadya served on?", "answer": "Banana leaf"},
    {"question": "Which god took the form of Vamana?", "answer": "Vishnu"},
    {"question": "What avatar of Vishnu is associated with Mahabali?", "answer": "Vamana"},
    {"question": "What is the most important day of Onam called?", "answer": "Thiruvonam"},
    {"question": "What is the first day of the ten-day Onam celebration?", "answer": "Atham"},
    {"question": "What is the day before Thiruvonam called?", "answer": "Uthradam"},
    {"question": "What traditional Kerala performance features tiger-painted performers?", "answer": "Pulikali"},
    {"question": "What is the traditional Kerala boat race called?", "answer": "Vallam Kali"},
    {"question": "What are the long racing boats of Kerala commonly called?", "answer": "Snake boats"},
    {"question": "What is the Malayalam word for a boat?", "answer": "Vallam"},
    {"question": "What sweet dessert is traditionally served during Onam?", "answer": "Payasam"},
    {"question": "What mixed vegetable dish is served during Sadya?", "answer": "Avial"},
    {"question": "What lentil and vegetable dish is commonly served during Sadya?", "answer": "Sambar"},
    {"question": "What yoghurt-based vegetable dish is served during Sadya?", "answer": "Kaalan"},
    {"question": "What traditional Kerala martial art is one of the oldest in India?", "answer": "Kalaripayattu"},
    {"question": "What classical Kerala dance-drama is famous for elaborate makeup?", "answer": "Kathakali"},
    {"question": "What traditional drum is commonly used in Kerala festivals?", "answer": "Chenda"},
    {"question": "What traditional white garment is commonly worn by men in Kerala?", "answer": "Mundu"},
    {"question": "What is the Malayalam calendar system called?", "answer": "Kollavarsham"},
    {"question": "How many steps of land did Vamana ask Mahabali for?", "answer": "Three"},
    {"question": "Which river is associated with the Nehru Trophy Boat Race?", "answer": "Punnamada River"},
    {"question": "What famous boat race takes place on Punnamada Lake?", "answer": "Nehru Trophy Boat Race"},
    {"question": "What is the traditional swing associated with Onam celebrations called?", "answer": "Oonjal"},
    {"question": "What Malayalam month is Onam mainly celebrated in?", "answer": "Chingam"},
    {"question": "What does the word Sadya refer to in Kerala culture?", "answer": "Feast"}
]


# =========================================================
# SUPABASE DATABASE
# =========================================================

def get_teams():

    response = (
        supabase
        .table("teams")
        .select("*")
        .execute()
    )

    return response.data


def save_team(team):

    (
        supabase
        .table("teams")
        .update({
            "membership_number": team["membership_number"],
            "last_name": team["last_name"],
            "score": int(team["score"] or 0),

            "player1": team["player1"] or None,
            "age1": int(team["age1"]) if team["age1"] else None,
            "score1": int(team["score1"] or 0),

            "player2": team["player2"] or None,
            "age2": int(team["age2"]) if team["age2"] else None,
            "score2": int(team["score2"] or 0),

            "player3": team["player3"] or None,
            "age3": int(team["age3"]) if team["age3"] else None,
            "score3": int(team["score3"] or 0),

            "player4": team["player4"] or None,
            "age4": int(team["age4"]) if team["age4"] else None,
            "score4": int(team["score4"] or 0)
        })
        .eq("id", team["id"])
        .execute()
    )

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "login"

if "membership_number" not in st.session_state:
    st.session_state.membership_number = ""

if "last_name" not in st.session_state:
    st.session_state.last_name = ""

if "first_name" not in st.session_state:
    st.session_state.first_name = ""

if "age" not in st.session_state:
    st.session_state.age = 0

if "player_number" not in st.session_state:
    st.session_state.player_number = None

if "questions" not in st.session_state:
    st.session_state.questions = []

if "question_number" not in st.session_state:
    st.session_state.question_number = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "score_saved" not in st.session_state:
    st.session_state.score_saved = False


# =========================================================
# HEADER
# =========================================================

st.markdown("# 🌸🌼 2026 AKGMA ONAM QUIZ 🌼🌸")
st.markdown("### 🪷 Welcome! Test your Onam knowledge! 🪷")
st.markdown("## 🌸 🛶 🌼 👑 🥭 🌺 🍌 🥥 🌼 🛶 🌸")
st.divider()


# =========================================================
# LOGIN PAGE
# =========================================================

if st.session_state.page == "login":

    existing_teams = get_teams()
    
    st.markdown("## 🌼 Enter Your Team Details")

    st.info(
        "🌸 Enter your membership number and last name, "
        "then CLICK the CONTINUE button below. 🌸"
    )

    with st.form("login_form"):

        membership_number = st.text_input(
            "🔢 Membership Number",
            placeholder="Enter your membership number",
            key="login_membership"
        )

        last_name = st.text_input(
            "👨‍👩‍👧‍👦 Confirm Your Last Name",
            placeholder="Enter your last name",
            key="login_last_name"
        )

        submitted = st.form_submit_button(
            "🌸 CONTINUE 🌸",
            use_container_width=True
        )

    if submitted:

        membership_number = membership_number.strip()
        last_name = last_name.strip()

        if membership_number.lower() == "admin":

            st.session_state.page = "admin"
            st.rerun()

        elif membership_number == "" or last_name == "":

            st.warning(
                "🌼 Please enter BOTH your membership number "
                "and last name, then click CONTINUE."
            )

        else:

            current_team = next(
            (
                team for team in existing_teams
                if str(team["membership_number"]).strip()
                == str(membership_number).strip()
                and str(team["last_name"]).strip().lower()
                == str(last_name).strip().lower()
            ),
            None
        )

            if current_team is None:

                st.error(
                    "❌ The membership number and last name "
                    "did not match."
                )

            else:

                st.session_state.membership_number = membership_number
                st.session_state.last_name = last_name
                st.session_state.page = "player"

                st.rerun()
# =========================================================
# PLAYER DETAILS PAGE
# =========================================================

elif st.session_state.page == "player":
    existing_teams = get_teams()
    st.markdown("## 🌸 Player Details 🌸")

    st.info(
        "🌼 Enter your first name and age, "
        "then CLICK the START QUIZ button."
    )

    first_name = st.text_input(
        "👤 What is your first name?"
    )

    age = st.number_input(
        "🎂 What is your age?",
        min_value=1,
        max_value=120,
        step=1
    )

    if st.button(
        "🌼 START QUIZ 🌼",
        use_container_width=True
    ):

        first_name = first_name.strip()

        if first_name == "":
            st.warning(
                "Please enter your first name, then click START QUIZ."
            )

        else:

            current_team = next(
                team for team in existing_teams
                if team["membership_number"]
                == st.session_state.membership_number
            )

            already_played = False

            for number in range(1, 5):
                if (
                    current_team[f"player{number}"]
                    .strip()
                    .lower()
                    == first_name.lower()
                ):
                    already_played = True

            if already_played:

                st.error(
                    "🚫 You have already played the quiz!"
                )

            else:

                player_number = None

                for number in range(1, 5):
                    if not current_team[f"player{number}"]:

                        current_team[f"player{number}"] = first_name
                        current_team[f"age{number}"] = age

                        player_number = number
                        break

                if player_number is None:

                    st.error(
                        "🚫 This team already has four players."
                    )

                else:

                    save_team(current_team)

                    st.session_state.first_name = first_name
                    st.session_state.age = age
                    st.session_state.player_number = player_number

                    if age <= 10:
                        question_list = quiz_dict_10

                    elif age <= 20:
                        question_list = quiz_dict_20

                    else:
                        question_list = quiz_dict_20_plus

                    st.session_state.questions = random.sample(
                        question_list,
                        10
                    )

                    st.session_state.question_number = 0
                    st.session_state.score = 0
                    st.session_state.score_saved = False
                    st.session_state.page = "quiz"

                    st.rerun()


# =========================================================
# QUIZ PAGE
# =========================================================

elif st.session_state.page == "quiz":

    questions = st.session_state.questions
    question_number = st.session_state.question_number

    if question_number >= len(questions):
        st.session_state.page = "finished"
        st.rerun()

    question = questions[question_number]

    st.subheader(
        f"🌼 Question {question_number + 1} of 10 🌼"
    )

    st.progress(question_number / 10)

    st.markdown(
        f"""
        <div class="quiz-box">
            <h3>🌸 {question["question"]}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    answer = st.text_input(
        "✏️ Your answer",
        key=f"answer_{question_number}"
    )

    st.info("🌼 Type your answer, then CLICK SUBMIT ANSWER.")

    if st.button(
        "🌼 SUBMIT ANSWER 🌼",
        use_container_width=True
    ):

        if answer.strip() == "":

            st.warning(
                "Please enter an answer, then click SUBMIT ANSWER."
            )

        else:

            if (
                answer.lower().strip()
                == question["answer"].lower().strip()
            ):

                st.success(
                    "🎉 Correct! Well done! 🌸"
                )

                st.session_state.score += 1

            else:

                st.error(
                    f"❌ Incorrect! The correct answer was: "
                    f"{question['answer']}"
                )

            st.session_state.question_number += 1
            st.rerun()


# =========================================================
# FINISHED PAGE
# =========================================================

elif st.session_state.page == "finished":
    existing_teams = get_teams()
    current_team = next(
        team for team in existing_teams
        if team["membership_number"]
        == st.session_state.membership_number
    )

    player_number = st.session_state.player_number

    if not st.session_state.score_saved:

        current_team[f"score{player_number}"] = st.session_state.score

        current_team["score"] = (
            int(current_team["score"] or 0)
            + st.session_state.score
        )

        save_team(current_team)

        st.session_state.score_saved = True

    st.balloons()

    st.markdown(
        "# 🌸🌼 QUIZ FINISHED! 🌼🌸"
    )

    st.success(
        "🎉 Your score has been added to your team total!"
    )

    st.write(
        "Thank you for playing the 2026 AKGMA Onam Quiz! 🪷"
    )

    st.markdown(
        "## 🌸 🛶 🌼 👑 🥭 🌺 🍌 🥥 🌼 🛶 🌸"
    )


# =========================================================
# ADMIN PAGE
# =========================================================

elif st.session_state.page == "admin":
    
    
    existing_teams = get_teams()
    st.markdown("# 👑 ADMIN AREA 👑")

    st.info(
        "Enter the administrator password, "
        "then CLICK LOGIN."
    )

    password = st.text_input(
        "Enter administrator password",
        type="password"
    )

    if st.button(
        "🔐 LOGIN",
        use_container_width=True
    ):

        if password == "administrator password":

            st.success(
                "Welcome, Administrator! 🌸"
            )

            u10_scores = []
            u20_scores = []
            u20_plus_scores = []

            for team in existing_teams:

                for number in range(1, 5):

                    if team[f"player{number}"]:

                        player_age = int(
                            team[f"age{number}"]
                        )

                        player_score = int(
                            team[f"score{number}"]
                        )

                        player_name = (
                            team[f"player{number}"]
                            + " "
                            + team["last_name"]
                        )

                        if player_age <= 10:

                            u10_scores.append(
                                (player_score, player_name)
                            )

                        elif player_age <= 20:

                            u20_scores.append(
                                (player_score, player_name)
                            )

                        else:

                            u20_plus_scores.append(
                                (player_score, player_name)
                            )

            u10_scores.sort(reverse=True)
            u20_scores.sort(reverse=True)
            u20_plus_scores.sort(reverse=True)

            st.divider()

            st.subheader("🌼 UNDER 10 TOP 5 🌼")

            if u10_scores:
                for score, name in u10_scores[:5]:
                    st.write(f"🏆 {name} — {score}")
            else:
                st.write("No scores yet.")

            st.divider()

            st.subheader("🌼 UNDER 20 TOP 5 🌼")

            if u20_scores:
                for score, name in u20_scores[:5]:
                    st.write(f"🏆 {name} — {score}")
            else:
                st.write("No scores yet.")

            st.divider()

            st.subheader("🌼 OVER 20 TOP 5 🌼")

            if u20_plus_scores:
                for score, name in u20_plus_scores[:5]:
                    st.write(f"🏆 {name} — {score}")
            else:
                st.write("No scores yet.")

        else:

            st.error(
                "❌ Incorrect password."
            )


