def generar_prompt(mental_clarity, emotional_state):
    if mental_clarity > 80 and emotional_state < 20:
        return "Un roble majestuoso con hojas verdes brillantes, erguido con fuerza y estabilidad, en un campo soleado."
    elif mental_clarity < 40 and emotional_state > 60:
        return "Un roble con ramas torcidas y hojas marchitas, rodeado de niebla, en un paisaje oscuro y ventoso."
    else:
        return "Un roble frondoso con algunas hojas en transición de verde a amarillo, en un bosque tranquilo con luz tenue."

prompt = generar_prompt(mental_clarity, emotional_state)
print(f"Prompt generado: {prompt}")
