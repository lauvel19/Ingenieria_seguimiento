import re
from typing import List, Tuple, Optional


class ImprovedReasoning:

    @staticmethod
    def deductive_reasoning(premise1: str, premise2: str) -> str:
        """
        Razonamiento deductivo mejorado que maneja múltiples formatos de premisas
        """
        try:
            # Verificar premisas vacías
            if not premise1.strip() or not premise2.strip():
                return "❌ Error: Ambas premisas deben contener texto válido"

            # Normalización más agresiva
            p1 = premise1.lower().replace(".", "").replace(",", "").strip()
            p2 = premise2.lower().replace(".", "").replace(",", "").strip()

            # Patrones más flexibles para detectar premisas
            def extract_logical_elements(premise):
                """Extrae sujeto y predicado de una premisa con mayor flexibilidad"""

                # Patrón 1: "Todos los X son Y"
                match = re.search(r"todos?\s+los?\s+(.+?)\s+son\s+(.+)", premise)
                if match:
                    return ("todos", match.group(1).strip(), match.group(2).strip())

                # Patrón 2: "Todo X es Y"
                match = re.search(r"todo\s+(.+?)\s+es\s+(.+)", premise)
                if match:
                    return ("todos", match.group(1).strip(), match.group(2).strip())

                # Patrón 3: "Los X son Y"
                match = re.search(r"los?\s+(.+?)\s+son\s+(.+)", premise)
                if match:
                    return ("los", match.group(1).strip(), match.group(2).strip())

                # Patrón 4: "X es Y" (para casos específicos)
                match = re.search(r"(.+?)\s+es\s+(.+)", premise)
                if match:
                    subject = match.group(1).strip()
                    predicate = match.group(2).strip()
                    # Verificar si es un caso específico (nombre propio o artículo definido)
                    if any(word in subject for word in ["el ", "la ", "un ", "una "]) or subject[0].isupper():
                        return ("es", subject, predicate)

                # Patrón 5: "Si X entonces Y"
                match = re.search(r"si\s+(.+?)\s+entonces\s+(.+)", premise)
                if match:
                    return ("si-entonces", match.group(1).strip(), match.group(2).strip())

                # Patrón 6: "Ningún X es Y"
                match = re.search(r"ningún\s+(.+?)\s+es\s+(.+)", premise)
                if match:
                    return ("ningún", match.group(1).strip(), match.group(2).strip())

                # Patrón 7: "Algunos X son Y"
                match = re.search(r"algunos?\s+(.+?)\s+son\s+(.+)", premise)
                if match:
                    return ("algunos", match.group(1).strip(), match.group(2).strip())

                return None

            # Extraer elementos de ambas premisas
            elements1 = extract_logical_elements(p1)
            elements2 = extract_logical_elements(p2)

            if not elements1 or not elements2:
                return (f"🔍 **Formato no reconocido.** Intenta con:\n\n"
                        f"**Formatos válidos:**\n"
                        f"• 'Todos los humanos son mortales'\n"
                        f"• 'Sócrates es humano'\n"
                        f"• 'Los perros son animales'\n"
                        f"• 'Si llueve entonces está mojado'\n"
                        f"• 'Ningún reptil es mamífero'\n\n"
                        f"**Lo que recibí:**\n"
                        f"• Premisa 1: '{premise1}'\n"
                        f"• Premisa 2: '{premise2}'")

            quantifier1, subj1, pred1 = elements1
            quantifier2, subj2, pred2 = elements2

            # Normalizar términos para comparación (eliminar artículos)
            def normalize_term(term):
                # Eliminar artículos y espacios extra
                normalized = re.sub(r'^(el|la|los|las|un|una)\s+', '', term.strip())
                return normalized

            norm_subj1 = normalize_term(subj1)
            norm_pred1 = normalize_term(pred1)
            norm_subj2 = normalize_term(subj2)
            norm_pred2 = normalize_term(pred2)

            # Lógica de inferencia mejorada
            conclusion = None

            # Caso 1: Silogismo Barbara - Todos A son B, Todos B son C → Todos A son C
            if (quantifier1 == "todos" and quantifier2 == "todos" and
                    (norm_pred1 == norm_subj2 or pred1 == subj2)):
                conclusion = f"✅ **Conclusión válida:** Todos los {subj1} son {pred2}"
                explanation = f"📚 **Tipo:** Silogismo categórico (Barbara)\n🔗 **Conexión:** {pred1} = {subj2}"

            # Caso 2: Silogismo con caso específico - Todos A son B, X es A → X es B
            elif (quantifier1 == "todos" and quantifier2 == "es" and
                  (norm_subj2 in norm_subj1 or norm_subj1 in norm_subj2 or subj1 in subj2)):
                conclusion = f"✅ **Conclusión válida:** {subj2} es {pred1}"
                explanation = f"📚 **Tipo:** Silogismo con caso particular\n🔗 **Conexión:** {subj2} pertenece a {subj1}"

            # Caso 3: Inverso - X es A, Todos A son B → X es B
            elif (quantifier1 == "es" and quantifier2 == "todos" and
                  (norm_subj1 in norm_subj2 or norm_subj2 in norm_subj1 or subj2 in subj1)):
                conclusion = f"✅ **Conclusión válida:** {subj1} es {pred2}"
                explanation = f"📚 **Tipo:** Silogismo con caso particular\n🔗 **Conexión:** {subj1} pertenece a {subj2}"

            # Caso 4: Modus Ponens - Si A entonces B, A → B
            elif (quantifier1 == "si-entonces" and
                  (subj1 in p2 or any(word in subj1 for word in p2.split()))):
                conclusion = f"✅ **Conclusión válida:** {pred1}"
                explanation = f"📚 **Tipo:** Modus Ponens\n🔗 **Se confirma:** {subj1}"

            # Caso 5: Conexión por predicado común
            elif (quantifier1 in ["todos", "los"] and quantifier2 in ["todos", "los"] and
                  (norm_pred1 == norm_pred2 or pred1 == pred2)):
                conclusion = f"✅ **Conexión identificada:** Tanto {subj1} como {subj2} son {pred1}"
                explanation = f"📚 **Tipo:** Relación por predicado común\n🔗 **Característica compartida:** {pred1}"

            # Caso 6: Ningún + Todos (Celarent)
            elif (quantifier1 == "ningún" and quantifier2 == "todos" and
                  (norm_pred1 == norm_subj2 or pred1 == subj2)):
                conclusion = f"✅ **Conclusión válida:** Ningún {subj2} es {subj1}"
                explanation = f"📚 **Tipo:** Silogismo categórico (Celarent)\n🔗 **Conexión:** {pred1} = {subj2}"

            else:
                # Verificar si hay alguna relación
                all_terms1 = {norm_subj1, norm_pred1, subj1, pred1}
                all_terms2 = {norm_subj2, norm_pred2, subj2, pred2}
                common_terms = all_terms1 & all_terms2

                if common_terms:
                    return (f"⚠️ **Relación detectada pero no forma silogismo válido**\n\n"
                            f"**Términos en común:** {', '.join(common_terms)}\n\n"
                            f"**Premisas analizadas:**\n"
                            f"• **Premisa 1:** {quantifier1} {subj1} → {pred1}\n"
                            f"• **Premisa 2:** {quantifier2} {subj2} → {pred2}\n\n"
                            f"💡 **Sugerencia:** Reorganiza las premisas para crear una cadena lógica clara.")
                else:
                    return (f"❌ **No hay conexión lógica entre las premisas**\n\n"
                            f"**Análisis:**\n"
                            f"• **Premisa 1:** {quantifier1} {subj1} → {pred1}\n"
                            f"• **Premisa 2:** {quantifier2} {subj2} → {pred2}\n\n"
                            f"💡 **Para razonamiento deductivo válido, necesitas:**\n"
                            f"• Premisas que compartan términos comunes\n"
                            f"• Una estructura lógica clara (A→B, B→C)")

            return f"{conclusion}\n\n{explanation}"

        except Exception as e:
            return f"❌ Error al procesar: {str(e)}"

    @staticmethod
    def inductive_reasoning(observations: List[str]) -> str:
        """
        Razonamiento inductivo mejorado con mejor reconocimiento de patrones
        """
        try:
            # Filtrar observaciones vacías
            cleaned_obs = [obs.strip() for obs in observations if obs.strip()]

            if len(cleaned_obs) < 2:
                return "⚠️ Se necesitan al menos 2 observaciones para identificar un patrón"

            if len(cleaned_obs) < 3:
                return "⚠️ Con solo 2 observaciones la generalización es muy débil. Añade más observaciones para mayor confianza."

            # Análisis de patrones mejorado
            def extract_pattern_elements(observation):
                """Extrae componentes de una observación"""
                obs_clean = observation.lower().strip()

                # Patrones de análisis más flexibles
                patterns = [
                    r"(.+?)\s+(es|son|está|están|tiene|tienen|hace|hacen|puede|pueden)\s+(.+)",
                    r"(.+?)\s+(.+)"  # Patrón más general
                ]

                for pattern in patterns:
                    match = re.search(pattern, obs_clean)
                    if match:
                        if len(match.groups()) >= 3:
                            return {
                                "subject": match.group(1).strip(),
                                "verb": match.group(2).strip(),
                                "predicate": match.group(3).strip(),
                                "full": obs_clean
                            }
                        else:
                            # Dividir en dos partes
                            parts = obs_clean.split()
                            mid = len(parts) // 2
                            return {
                                "subject": " ".join(parts[:mid]),
                                "verb": "",
                                "predicate": " ".join(parts[mid:]),
                                "full": obs_clean
                            }

                return {"subject": "", "verb": "", "predicate": obs_clean, "full": obs_clean}

            # Extraer elementos de todas las observaciones
            elements = [extract_pattern_elements(obs) for obs in cleaned_obs]

            # Encontrar patrones comunes en sujetos
            subjects = [elem["subject"] for elem in elements if elem["subject"]]
            subject_pattern = None

            if subjects:
                # Buscar palabras comunes en sujetos
                subject_words = []
                for subj in subjects:
                    subject_words.extend(subj.split())

                # Encontrar la palabra más frecuente que aparece en la mayoría
                word_counts = {}
                for word in subject_words:
                    if len(word) > 2:  # Ignorar palabras muy cortas
                        word_counts[word] = word_counts.get(word, 0) + 1

                # Buscar palabra que aparezca en al menos la mitad de las observaciones
                for word, count in word_counts.items():
                    if count >= len(cleaned_obs) * 0.5:
                        subject_pattern = word
                        break

                # Si no encuentra patrón específico, inferir categoría
                if not subject_pattern:
                    if any(word in " ".join(subjects) for word in ["perro", "gato", "animal"]):
                        subject_pattern = "animales"
                    elif any(word in " ".join(subjects) for word in ["pájaro", "ave", "cisne"]):
                        subject_pattern = "aves"
                    elif any(word in " ".join(subjects) for word in ["persona", "humano", "gente"]):
                        subject_pattern = "personas"
                    else:
                        subject_pattern = "elementos observados"

            # Encontrar patrones comunes en predicados
            predicates = [elem["predicate"] for elem in elements if elem["predicate"]]
            predicate_pattern = None

            if predicates:
                # Buscar palabras que aparezcan en la mayoría de predicados
                predicate_words = []
                for pred in predicates:
                    predicate_words.extend(pred.split())

                common_predicate_words = []
                word_counts = {}
                for word in predicate_words:
                    if len(word) > 2:
                        word_counts[word] = word_counts.get(word, 0) + 1

                for word, count in word_counts.items():
                    if count >= len(cleaned_obs) * 0.6:  # Aparece en al menos 60% de observaciones
                        common_predicate_words.append(word)

                if common_predicate_words:
                    predicate_pattern = ", ".join(sorted(common_predicate_words))

            # Encontrar verbo común
            verbs = [elem["verb"] for elem in elements if elem["verb"]]
            verb_pattern = None
            if verbs:
                verb_counts = {}
                for verb in verbs:
                    verb_counts[verb] = verb_counts.get(verb, 0) + 1

                if verb_counts:
                    verb_pattern = max(verb_counts, key=verb_counts.get)

            # Generar conclusión inductiva
            confidence = min(len(cleaned_obs) * 15 + 10, 85)  # Máximo 85% de confianza

            if subject_pattern and predicate_pattern:
                if verb_pattern:
                    conclusion = f"🔍 **Generalización inductiva** (Confianza: {confidence}%):\n"
                    conclusion += f"Los {subject_pattern} {verb_pattern} {predicate_pattern}"
                else:
                    conclusion = f"🔍 **Patrón identificado** (Confianza: {confidence}%):\n"
                    conclusion += f"Los {subject_pattern} tienen la característica: {predicate_pattern}"
            elif subject_pattern:
                conclusion = f"🔍 **Patrón en sujetos identificado** (Confianza: {confidence}%)\n"
                conclusion += f"Patrón detectado en: {subject_pattern}"
            else:
                conclusion = f"⚠️ **Patrón débil** identificado en {len(cleaned_obs)} observaciones"

            # Añadir advertencias y sugerencias
            warning = ("\n\n⚠️ **Importante sobre razonamiento inductivo:**\n"
                       f"• Las generalizaciones NO garantizan certeza\n"
                       f"• Una excepción puede invalidar la regla\n"
                       f"• Basado en {len(cleaned_obs)} observación{'es' if len(cleaned_obs) > 1 else ''}\n")

            if len(cleaned_obs) < 5:
                warning += f"• 💡 **Sugerencia:** Añade más observaciones para mayor confianza\n"

            if confidence < 50:
                warning += f"• ⚠️ **Confianza baja:** El patrón necesita más evidencia\n"

            return conclusion + warning

        except Exception as e:
            return f"❌ Error al procesar observaciones: {str(e)}"

    @staticmethod
    def analyze_argument_strength(premise1: str, premise2: str, conclusion: str) -> str:
        """Analiza la fortaleza de un argumento completo"""
        try:
            # Verificar si es deductivo válido
            deductive_result = ImprovedReasoning.deductive_reasoning(premise1, premise2)

            if "Conclusión válida" in deductive_result:
                return f"💪 **Argumento DEDUCTIVO VÁLIDO**\n{deductive_result}\n\n✅ La conclusión se sigue necesariamente de las premisas."
            else:
                return f"⚠️ **Argumento DEDUCTIVO INVÁLIDO**\n{deductive_result}\n\n❌ La conclusión no se sigue necesariamente de las premisas."

        except Exception as e:
            return f"❌ Error en el análisis: {str(e)}"