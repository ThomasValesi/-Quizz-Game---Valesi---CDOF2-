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

    score = 0  # Score total
    bonus_points = 0  # Points bonus cumulés
    correct_streak = 0  # Série de bonnes réponses consécutives
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
                break
            if user_answer:  # Une réponse a été donnée
                break

        if elapsed_time <= time_limit and user_answer == q['answer']:
            print("Correct!\n")
            score += 1
            correct_streak += 1  # Incrémenter la série de bonnes réponses
            
            # Ajouter des points bonus en fonction de la série
            if correct_streak > 1:  # Bonus seulement pour au moins 2 bonnes réponses consécutives
                streak_bonus = correct_streak - 1
                bonus_points += streak_bonus
                print(f"Bonus! You've earned {streak_bonus} extra points for a streak of {correct_streak} correct answers!\n")
        else:
            if elapsed_time <= time_limit:
                print(f"Wrong! The correct answer was: {q['answer']}\n")
            correct_streak = 0  # Réinitialiser la série en cas de mauvaise réponse ou de dépassement de temps

    # Résultat final
    total_score = score + bonus_points
    print(f"You finished the quiz!")
    print(f"Base score: {score}")
    print(f"Bonus points: {bonus_points}")
    print(f"Total score: {total_score}/{len(questions) + bonus_points}")

    if score == len(questions):
        print("Congratulations! You answered all questions correctly!")
    elif score > 0:
        print("Good job! Keep practicing to improve your score.")
    else:
        print("Better luck next time!")

# Lancer le jeu
if __name__ == "__main__":
    quiz_game()
