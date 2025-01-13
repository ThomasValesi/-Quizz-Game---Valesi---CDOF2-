import time

def quiz_game():
    print("Welcome to the Quiz Game!\n")

    # Liste des questions et réponses
    questions = [
        {"question": "What is the capital of France?", "answer": "paris"},
        {"question": "How many legs does a spider have?", "answer": "8"},
        {"question": "What is the chemical symbol for water?", "answer": "h2o"},
        {"question": "Who wrote 'Romeo and Juliet'?", "answer": "shakespeare"},
        {"question": "What is 5 + 7?", "answer": "12"},
    ]

    score = 0  # Points de base
    bonus_points = 0  # Points bonus accumulés
    consecutive_correct = 0  # Compteur de bonnes réponses consécutives
    time_limit = 10  # Temps limite en secondes par question

    for idx, q in enumerate(questions, 1):
        print(f"Question {idx}: {q['question']} (You have {time_limit} seconds to answer)")

        start_time = time.time()  # Enregistre l'heure de début
        user_answer = None

        while True:
            user_answer = input("Your answer: ").strip().lower()
            elapsed_time = time.time() - start_time  # Temps écoulé
            if elapsed_time > time_limit:
                print("Time's up! You didn't answer in time.\n")
                consecutive_correct = 0  # Réinitialise les bonus en cas d'échec
                break
            if user_answer:  # Une réponse a été donnée
                break

        if elapsed_time <= time_limit and user_answer == q['answer']:
            print("Correct!\n")
            score += 1
            consecutive_correct += 1

            # Calcul des points bonus
            if consecutive_correct > 1:
                earned_bonus = consecutive_correct - 1  # Bonus progressif
                bonus_points += earned_bonus
                print(f"Bonus! You earned {earned_bonus} additional point(s) for consecutive correct answers!\n")
        else:
            if elapsed_time <= time_limit:
                print(f"Wrong! The correct answer was: {q['answer']}\n")
            consecutive_correct = 0  # Réinitialise le compteur de bonnes réponses consécutives

    # Résultat final
    print(f"You finished the quiz! Your final score breakdown:")
    print(f" - Base points: {score}")
    print(f" - Bonus points: {bonus_points}")
    print(f" - Total score: {score + bonus_points}\n")

    if score == len(questions):
        print("Congratulations! You answered all questions correctly!")
    elif score > 0:
        print("Good job! Keep practicing to improve your score.")
    else:
        print("Better luck next time!")

# Lancer le jeu
if __name__ == "__main__":
    quiz_game()
