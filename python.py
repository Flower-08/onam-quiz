import json
import random
import sys
try:
    with open("existing_teams.json", "r") as file:
        existing_teams = json.load(file)

except FileNotFoundError:
    existing_teams = [
    {'membership_number': '1', 'last_name': 'Sredha', 'score': '0', 'age1': '', 'player1': '', 'score1': '0', 'age2': '', 'player2': '', 'score2': '0', 'age3': '', 'player3': '', 'score3': '0', 'age4': '', 'player4': '', 'score4': '0'},
    {'membership_number': '2', 'last_name': 'Sreya', 'score': '0', 'age1': '', 'player1': '', 'score1': '0', 'age2': '', 'player2': '', 'score2': '0', 'age3': '', 'player3': '', 'score3': '0', 'age4': '', 'player4': '', 'score4': '0'},
    {'membership_number': '3', 'last_name': 'Sanchu', 'score': '0', 'age1': '', 'player1': '', 'score1': '0', 'age2': '', 'player2': '', 'score2': '0', 'age3': '', 'player3': '', 'score3': '0', 'age4': '', 'player4': '', 'score4': '0'},
    {'membership_number': '4', 'last_name': 'Smitha', 'score': '0', 'age1': '', 'player1': '', 'score1': '0', 'age2': '', 'player2': '', 'score2': '0', 'age3': '', 'player3': '', 'score3': '0', 'age4': '', 'player4': '', 'score4': '0'}
]
def save_teams():
    with open("existing_teams.json", "w") as file:
        json.dump(existing_teams, file, indent=4)

def admin():
    password = 'administrator password'
    player_password = input('Hello! What is the password?')
    if player_password == password:
        u10_scores = []
        u20_scores = []
        u20_plus_scores = []
        for team in existing_teams:
            for number in range(1, 5):
                if team[f'player{number}'] != '':
                    player_age = int(team[f'age{number}'])
                    player_score = int(team[f'score{number}'])
                    if player_age <= 10:
                        u10_scores.append((player_score, team[f'player{number}'] + " " + team['last_name']))
                    elif player_age<= 20:
                        u20_scores.append((player_score, team[f'player{number}'] + " " + team['last_name']))
                    else:
                        u20_plus_scores.append((player_score, team[f'player{number}'] + " " + team['last_name']))
        u10_scores.sort(reverse=True)
        u20_scores.sort(reverse=True)
        u20_plus_scores.sort(reverse=True)
        print("\n" + "-" * 120)
        print("\n")
        print("AKGMA EXISTING TEAMS")
        print("\n" + "-" * 120)
        
        print("Under 10 Top 5 Scores")
        for score, name in u10_scores[:5]:
            print(score, "-", name)

        print("\n" + "-" * 120)
        print("Under 20 Top 5 Scores")
        for score, name in u20_scores[:5]:
            print(score, "-", name)
        print("\n" + "-" * 120)
        print("Over 20 Top 5 Scores")
        for score, name in u20_plus_scores[:5]:
            print(score, "-", name)
        
        return
                            
    else:
        stay_or_leave = input('Incorrect password! Enter"play" to continue with the quiz or "quit" to leave. ')
        while stay_or_leave != 'play' and stay_or_leave != 'quit':
            print('Invalid input.')
            stay_or_leave = input('Incorrect password! Enter"play" to continue with the quiz or "quit" to leave. ')
        if stay_or_leave =='play':
            pass
        elif stay_or_leave == 'quit':
            return
    
        return
def game():

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
    {"question": "What is a traditional Onam meal called?", "answer": "Sadya"},
    {"question": "Which fruit is commonly used to make banana chips?", "answer": "Banana"},
    {"question": "What is the Malayalam word for a boat?", "answer": "Vallam"},
    {"question": "What is the main decoration people make outside their homes during Onam?", "answer": "Pookalam"},
    {"question": "Which king is believed to visit his people during Onam?", "answer": "Mahabali"},
    {"question": "What is Payasam usually eaten as?", "answer": "Dessert"},
    {"question": "What is commonly placed on the floor to create a Pookalam?", "answer": "Flowers"},
    {"question": "What is the traditional Kerala garment worn around the waist by men?", "answer": "Mundu"},
    {"question": "What is a Kasavu saree traditionally worn by?", "answer": "Women"},
    {"question": "What food is Sadya traditionally served on?", "answer": "Banana leaf"},
    {"question": "Which celebration includes colourful flower designs?", "answer": "Onam"},
    {"question": "What do people usually eat together during an Onam Sadya?", "answer": "Food"},
    {"question": "Which famous Kerala art form uses colourful costumes and makeup?", "answer": "Kathakali"},
    {"question": "Which instrument is commonly used in Kerala festivals?", "answer": "Chenda"},
    {"question": "What vegetable dish made with different vegetables is served during Sadya?", "answer": "Avial"},
    {"question": "What dish made with lentils and vegetables is often served during Sadya?", "answer": "Sambar"},
    {"question": "What crispy snack made from banana is often served during Sadya?", "answer": "Banana chips"},
    {"question": "What sweetener is used to make Sharkara Varatti?", "answer": "Jaggery"},
    {"question": "What is the traditional swing used during Onam celebrations called?", "answer": "Oonjal"},
    {"question": "What is the Malayalam name for the traditional Kerala boat race?", "answer": "Vallam Kali"},
    {"question": "What is the traditional white clothing worn by many men in Kerala called?", "answer": "Mundu"},
    {"question": "What is the traditional Kerala meal with many different dishes called?", "answer": "Sadya"},
    {"question": "Which festival celebrates the visit of Mahabali?", "answer": "Onam"},
    {"question": "Which avatar of Vishnu is connected to the Onam story?", "answer": "Vamana"},
    {"question": "What did Vamana ask Mahabali for?", "answer": "Three steps of land"},
    {"question": "How many steps of land did Vamana ask Mahabali for?", "answer": "Three"},
    {"question": "What is the name of the day before Thiruvonam?", "answer": "Uthradam"},
    {"question": "Which day marks the beginning of the ten main days of Onam?", "answer": "Atham"},
    {"question": "What is the name of the colourful flower carpet made during Onam?", "answer": "Pookalam"},
    {"question": "What is the famous Kerala festival celebrated with Sadya and Pookalam?", "answer": "Onam"},
    {"question": "What is the legendary king remembered during Onam?", "answer": "Mahabali"},
    {"question": "What is the biggest festival celebrated in Kerala?", "answer": "Onam"}
    ]
    	
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
    {"question": "What crispy banana snack is commonly served during Sadya?", "answer": "Banana chips"},
    {"question": "What is the Malayalam word for a boat?", "answer": "Vallam"},
    {"question": "What sweetener is used in Sharkara Varatti?", "answer": "Jaggery"},
    {"question": "What is the traditional swing used during Onam celebrations called?", "answer": "Oonjal"},
    {"question": "How many steps of land did Vamana ask Mahabali for?", "answer": "Three"},
    {"question": "What is the day before Thiruvonam called?", "answer": "Uthradam"},
    {"question": "What is the traditional Kerala martial art called?", "answer": "Kalaripayattu"},
    {"question": "What is the Malayalam calendar called?", "answer": "Kollavarsham"},
    {"question": "Which river hosts the famous Nehru Trophy Boat Race?", "answer": "Punnamada River"},
    {"question": "What is the famous annual boat race held on Punnamada Lake called?", "answer": "Nehru Trophy Boat Race"},
    {"question": "What is the Malayalam word commonly used for a grand traditional feast?", "answer": "Sadya"},
    {"question": "Which ingredient is commonly used as the base of Payasam?", "answer": "Rice"},
    {"question": "Which fruit is traditionally offered with an Onam Sadya?", "answer": "Banana"},
    {"question": "What dish made with yoghurt and vegetables is served during Sadya?", "answer": "Kaalan"},
    {"question": "What is the name of the jaggery-coated banana snack served during Sadya?", "answer": "Sharkara Varatti"},
    {"question": "Which day comes immediately after Atham?", "answer": "Chithira"},
    {"question": "Which day comes immediately after Chithira?", "answer": "Chodhi"},
    {"question": "Which day comes immediately after Chodhi?", "answer": "Vishakam"},
    {"question": "Which day comes immediately after Vishakam?", "answer": "Anizham"},
    {"question": "Which day comes immediately after Anizham?", "answer": "Thriketta"},
    {"question": "Which day comes immediately after Thriketta?", "answer": "Moolam"},
    {"question": "Which day comes immediately after Moolam?", "answer": "Pooradam"},
    {"question": "What festival marks the annual homecoming of King Mahabali?", "answer": "Onam"},
    {"question": "What does the name Pulikali literally refer to?", "answer": "Tiger dance"},
    {"question": "Which district is famous for the Pulikali celebrations during Onam?", "answer": "Thrissur"},
    {"question": "What is the traditional flower arrangement made over several days during Onam?", "answer": "Pookalam"},
    {"question": "Which legendary ruler is remembered for a time of prosperity and equality?", "answer": "Mahabali"},
    {"question": "Which festival is known as Kerala's harvest festival?", "answer": "Onam"}
    ]

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
    {"question": "What sweetener is used to make Sharkara Varatti?", "answer": "Jaggery"},
    {"question": "What traditional Kerala martial art is one of the oldest in India?", "answer": "Kalaripayattu"},
    {"question": "What classical Kerala dance-drama is famous for elaborate makeup?", "answer": "Kathakali"},
    {"question": "What traditional drum is commonly used in Kerala festivals?", "answer": "Chenda"},
    {"question": "What traditional white garment is commonly worn by men in Kerala?", "answer": "Mundu"},
    {"question": "What traditional garment with a gold border is often worn by women?", "answer": "Kasavu saree"},
    {"question": "What is the Malayalam calendar system called?", "answer": "Kollavarsham"},
    {"question": "How many steps of land did Vamana ask Mahabali for?", "answer": "Three"},
    {"question": "Which river is associated with the Nehru Trophy Boat Race?", "answer": "Punnamada River"},
    {"question": "What famous boat race takes place on Punnamada Lake?", "answer": "Nehru Trophy Boat Race"},
    {"question": "What is the traditional swing associated with Onam celebrations called?", "answer": "Oonjal"},
    {"question": "Which day comes immediately after Atham?", "answer": "Chithira"},
    {"question": "Which day comes immediately after Chithira?", "answer": "Chodhi"},
    {"question": "Which day comes immediately after Chodhi?", "answer": "Vishakam"},
    {"question": "Which day comes immediately after Vishakam?", "answer": "Anizham"},
    {"question": "Which day comes immediately after Anizham?", "answer": "Thriketta"},
    {"question": "Which day comes immediately after Thriketta?", "answer": "Moolam"},
    {"question": "Which day comes immediately after Moolam?", "answer": "Pooradam"},
    {"question": "Which day comes immediately after Pooradam?", "answer": "Uthradam"},
    {"question": "What is the Sanskrit name for the star associated with the main day of Onam?", "answer": "Shravana"},
    {"question": "What Malayalam month is Onam mainly celebrated in?", "answer": "Chingam"},
    {"question": "What is the traditional name for the day before Uthradam?", "answer": "Pooradam"},
    {"question": "Which district is especially famous for Pulikali celebrations?", "answer": "Thrissur"},
    {"question": "Which ingredient gives Sharkara Varatti its characteristic sweetness?", "answer": "Jaggery"},
    {"question": "What legendary quality is Mahabali's kingdom traditionally remembered for?", "answer": "Prosperity"},
    {"question": "Which avatar of Vishnu is traditionally considered the fifth avatar?", "answer": "Vamana"},
    {"question": "What does the word Sadya refer to in Kerala culture?", "answer": "Feast"},
    {"question": "Which festival is considered the biggest cultural festival of Kerala?", "answer": "Onam"},
    {"question": "What is the flower carpet created during Onam celebrations called?", "answer": "Pookalam"},
    {"question": "What is the annual visit of Mahabali celebrated through?", "answer": "Onam"},
    {"question": "Which traditional feast contains many vegetarian dishes served together?", "answer": "Sadya"},
    {"question": "Which festival celebrates Mahabali's return to Kerala?", "answer": "Onam"}
    ]


    

    print('Welcome to the quiz! Once you have entered your membership number and last name, you will be asked for your age and first name. At any point, if you enter "exit" you will leave the program.')
    print('This information will be used to keep score and choose your questions. For any queries, please email flowerpetals080808@gmail.com.')
    membership_number = input('Please enter your membership number.')
    

    if membership_number.lower().strip() == 'admin':
        admin()
        return
    
    elif membership_number.lower().strip()=='exit':
        print("Exiting now .....")
        return

    else:    
        while membership_number not in [team['membership_number'] for team in existing_teams]:
            print("The membership number you entered was not found.. To add a team, contact @flowerpetals080808@gmail.com")
            membership_number = input('Please enter your membership number.')
            if membership_number.lower().strip() == 'admin':
                admin()
                return
    last_name = input('Please confirm your last name.')
    while last_name not in [team['last_name'] for team in existing_teams]:
        if last_name.lower().strip() == 'admin':
            admin()
        elif last_name.lower().strip()== 'exit':
            print("Exiting now .....")
            return
        else:
            print('The membership number you entered did not match the last name. To add a team, contact @flowerpetals080808@gmail.com')
            last_name = input('Please confirm your last name.')
    print('Welcome to the 2026 AKGMA Onam Quiz!')
    current_team = next(
    team for team in existing_teams
    if team['membership_number'] == membership_number
    )
            
    print(r'''
          ____   _   _    _    __  __
         / __ \ | \ | |  / \  |  \/  |
        | |  | ||  \| | //_\\ | |\/| |
        | |__| || |\  |/ ___ \| |  | |
         \____/ |_| \_/_/   \_\_|  |_|
        ''')
    
    first_name = input('What is your first name? Your age and first name will be used to keep score of your family total.')

    
    if first_name.isalpha():
        if first_name.lower().strip() == 'admin':
            admin()
            return

        elif first_name.lower().strip() == 'exit':
            print("Exiting now .....")
            return
        else:
            print('Your name has been accepted.')
            
    else:
        print('Your name has been recieved as digits. Please try again.')
        first_name = input('What is your first name?')
        
    age = input('What is your age? Based on this information, you will be given the appropriate set of questions.')
    if age.isalpha():
        if age.lower().strip() == 'admin':
            admin()
            return

        elif age.lower().strip() == 'exit':
            print("Exiting now .....")
            return
        else:
            print('Your age has not been accepted.')
    else:
        print('Your age has been received.')
    for team in existing_teams:
        if team['membership_number'] == membership_number:
            for number in range(1, 5):
                if team[f'player{number}'].lower() == first_name.lower():
                    print('You have already played the game once! Unfortunately, that is the maximum but I hope you enjoyed it.')
                    return
    player_number = None
    for team in existing_teams:

        if (team['membership_number'] == membership_number
                and team['last_name'].strip().lower() == last_name.lower()):
        
            for number in range(1, 5):
        
                if team[f'player{number}'] == '':
                    team[f'player{number}'] = first_name
                    team[f'age{number}'] = age
                    player_number = number
                    save_teams()
                    break
    
    age = int(age)
                
    if age <= 10:
            print('You will be given 10 questions, one by one. You will not see your score at the end but it will add to your team total.')
            quiz_questions = random.sample(quiz_dict_10,10)
            score = 0

            current_team = next(team for team in existing_teams if team['membership_number'] == membership_number)
            for question in quiz_questions:
                    
                    
                answer = input(question['question'])
                if answer.lower().strip() == question['answer'].lower().strip():
                    print ('Correct!')
                    score = score + 1

                elif answer.lower().strip() == 'admin':
                    admin()
                    return

                elif answer.lower().strip() == 'exit':
                    print("Exiting now .....")
                    return
                    
                else:
                    print ('Incorrect!')
                    print('The correct answer was: '+ question['answer'])
            print('Your questions have finished. You cannot play again as the same player.')
            current_team[f'score{player_number}'] = str(score)
            current_team['score'] = int(current_team['score']) + score
            save_teams()
                    
        
        
    elif age <= 20:
            print('You will be given 10 questions, one by one. You will not see your score at the end but it will add to your team total.')
            quiz_questions = random.sample(quiz_dict_20,10)
            score = 0
            for question in quiz_questions:
                    
                    
                answer = input(question['question'])
                if answer.lower() == question['answer'].lower():
                    print ('Correct!')
                    score = score + 1

                elif answer.lower().strip() == 'admin':
                    admin()
                    return
                            

                elif answer.lower().strip() == 'exit':
                    print("Exiting now .....")
                    return
                
                else:
                    print ('Incorrect!')
                    print('The correct answer was:'+ question['answer'])
            print('Your questions have finished. You cannot play again as the same player.')
            current_team[f'score{player_number}'] = str(score)
            current_team['score'] = int(current_team['score']) + score
            save_teams()
            
    else:
            print('You will be given 10 questions, one by one. You will not see your score at the end but it will add to your team total.')
            quiz_questions = random.sample(quiz_dict_20_plus,10)
            score = 0
            for question in quiz_questions:
                    
                    
                answer = input(question['question'])
                if answer.lower() == question['answer'].lower():
                    print ('Correct!')
                    score = score + 1

                elif answer.lower().strip() == 'admin':
                    admin()
                    return

                elif answer.lower().strip() == 'exit':
                    print("Exiting now .....")
                    return                
                else:
                    print ('Incorrect!')
                    print('The correct answer was:'+ question['answer'])
            print('Your questions have finished. You cannot play again as the same player.')
            current_team[f'score{player_number}'] = str(score)
            current_team['score'] = int(current_team['score']) + score
            save_teams()
            
game()
