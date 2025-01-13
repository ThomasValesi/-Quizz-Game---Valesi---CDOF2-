import time
from colorama import Fore, Style

def quiz_game():
    print(Fore.BLUE + "Welcome to the Quiz Game!\n" + Style.RESET_ALL)

    # Liste des questions et réponses
    questions = [
        {"question": "What is the capital of France?", "answer": "paris"},
        {"question": "How many legs does a spider have?", "answer": "8"},
        {"question": "What is the chemical symbol for water?", "answer": "h2o"},
        {"question": "Who wrote 'Romeo and Juliet'?", "answer": "shakespeare"},
        {"question": "What is 5 + 7?", "answer": "12"},
    ]

    score = 0  # Initialisation du score
    time_limit = 10  # Temps limite en secondes par question

    for idx, q in enumerate(questions, 1):
        print(Fore.CYAN + f"Question {idx}: {q['question']} (You have {time_limit} seconds to answer)" + Style.RESET_ALL)

        start_time = time.time()  # Enregistre l'heure de début
        user_answer = None

        while True:
            user_answer = input("Your answer: ").strip().lower()
            elapsed_time = time.time() - start_time  # Temps écoulé
            if elapsed_time > time_limit:
                print(Fore.RED + "Time's up! You didn't answer in time.\n" + Style.RESET_ALL)
                break  # Temps écoulé, on sort de la boucle
            if user_answer:  # Une réponse a été donnée
                break

        if elapsed_time <= time_limit and user_answer == q['answer']:
            print(Fore.GREEN + "Great job! Correct!\n" + Style.RESET_ALL)
            score += 1
        elif elapsed_time <= time_limit:
            print(Fore.RED + f"Oops, better luck next time! The correct answer was: {q['answer']}\n" + Style.RESET_ALL)

    # Résultat final
    print(Fore.YELLOW + f"You finished the quiz! Your final score is: {score}/{len(questions)}" + Style.RESET_ALL)
    
    if score == len(questions):
        print(Fore.GREEN + "Congratulations! You answered all questions correctly!" + Style.RESET_ALL)
    elif score > 0:
        print(Fore.BLUE + "Good job! Keep practicing to improve your score." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Better luck next time!" + Style.RESET_ALL)

# Lancer le jeu
if __name__ == "__main__":
    quiz_game()
