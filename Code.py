import random

def poser_questions():
    questions = [
        {
            "question": "Quel est le plus grand pays du monde par superficie ?",
            "options": ["1) Chine", "2) États-Unis", "3) Russie", "4) Canada"],
            "correct": 3
        },
        {
            "question": "Qui a peint la Joconde ?",
            "options": ["1) Vincent van Gogh", "2) Léonard de Vinci", "3) Pablo Picasso", "4) Michel-Ange"],
            "correct": 2
        },
        {
            "question": "Quelle est la capitale de l'Australie ?",
            "options": ["1) Sydney", "2) Melbourne", "3) Canberra", "4) Perth"],
            "correct": 3
        },
        {
            "question": "Which company created Python?",
            "answer": "Google",
            "options": ["Microsoft", "Google", "Apple", "Facebook"],
            "correct": "B"
        },
        {
            "question": "What does HTML stand for?",
            "answer": "Hypertext Markup Language", 
            "options": ["High Tech Modern Language", "Hypertext Markup Language", "Home Tool Markup Language", "Hyperlink and Text Markup Language"],
            "correct": "B"
        }
    ]

    random.shuffle(questions)  # Mélanger les questions pour plus de variété
    score = 0

    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        for option in q["options"]:
            print(option)

        while True:
            try:
                reponse = int(input("Votre réponse (1-4) : "))
                if 1 <= reponse <= 4:
                    break
                else:
                    print("Veuillez entrer un nombre entre 1 et 4.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")

        if reponse == q["correct"]:
            print("Bonne réponse ! \n")
            score += 1
        else:
            print(f"Mauvaise réponse. La bonne réponse était {q['correct']} : {q['options'][q['correct'] - 1]}\n")

    print(f"Vous avez terminé ! Votre score est de {score}/{len(questions)}.")

if __name__ == "__main__":
    poser_questions()
