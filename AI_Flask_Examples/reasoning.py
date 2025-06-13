def deductive_reasoning(premise1, premise2):
    try:
        # Verificar premisas vacías
        if not premise1.strip() or not premise2.strip():
            return "Error: Ambas premisas deben contener texto"

        # Normalización
        p1 = premise1.lower().replace(".", "").strip()
        p2 = premise2.lower().replace(".", "").strip()

        # Función mejorada para extraer elementos
        def extract_elements(premise):
            words = premise.split()
            if len(words) < 4:
                return None

            # Manejar formato "Todos los X son Y"
            if words[0] == "todos" and words[1] == "los":
                subject = " ".join(words[2:-2])
                predicate = words[-1]
                return ("todos", subject, predicate)
            # Manejar formato "Los X son Y"
            elif words[0] == "los" and words[-2] == "son":
                subject = " ".join(words[1:-2])
                predicate = words[-1]
                return ("los", subject, predicate)
            return None

        # Extraer elementos de ambas premisas
        elements1 = extract_elements(p1)
        elements2 = extract_elements(p2)

        if not elements1 or not elements2:
            return "Formato no válido. Ejemplo: 'Todos los artistas son banqueros'"

        type1, subj1, pred1 = elements1
        type2, subj2, pred2 = elements2

        # Lógica de conexión mejorada
        if pred1 == subj2:
            return f"Conclusión válida: Todos los {subj1} son {pred2}"
        elif subj1 == pred2:
            return f"Conclusión válida: Algunos {subj2} son {pred1}"
        else:
            return "No hay conexión lógica directa entre las premisas"

    except Exception as e:
        return f"Error al procesar: {str(e)}"


def inductive_reasoning(observations):
    # Filtrar observaciones vacías
    cleaned_obs = [obs.strip() for obs in observations if obs.strip()]

    if len(cleaned_obs) < 3:
        return "Se necesitan al menos 3 observaciones válidas para generalizar"

    # Encontrar palabras comunes
    words_list = [set(obs.lower().split()) for obs in cleaned_obs]
    common_words = set(words_list[0])

    for word_set in words_list[1:]:
        common_words.intersection_update(word_set)

    if not common_words:
        return "No se encontraron patrones comunes en las observaciones"

    # Identificar el sujeto (primera palabra no común)
    sample_words = cleaned_obs[0].lower().split()
    subject = next((word for word in sample_words if word not in common_words), "elementos")

    return (
        f"Conclusión inductiva: Los {subject} comparten estas características: "
        f"{', '.join(sorted(common_words))}. "
        f"Basado en {len(cleaned_obs)} observaciones."
    )