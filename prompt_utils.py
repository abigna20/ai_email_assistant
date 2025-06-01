def generate_prompt(user_input, tone):
    tone_instructions = {
        "formal": "Use a formal and professional tone.",
        "friendly": "Use a warm and friendly tone.",
        "apologetic": "Use a polite and apologetic tone.",
        "assertive": "Use a confident and direct tone.",
        "Happy": "Use an excited and joyful tone", 
        "Sad": "Use a depressed tone", 
        "Condolence": "Use a sorrowful tone", 
        "Angry": "Use a tone that's direct and shows anger"
    }

    tone_instruction = tone_instructions.get(tone.lower(), "")
    
    prompt = (
        f"Write a professional email based on the following instruction:\n"
        f"{user_input}\n\n"
        f"{tone_instruction}\n"
        f"Structure it with subject, greeting, body, and sign-off."
    )

    return prompt
