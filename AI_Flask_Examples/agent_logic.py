import random


class IntelligentAgent:
    def __init__(self):
        self.context = []
        self.responses = {
            "greetings": {
                "patterns": ["hola", "hi", "buenos días", "saludos"],
                "answers": [
                    "¡Hola! 😊 ¿En qué puedo ayudarte hoy?",
                    "¡Buenos días! 🌞 ¿Qué te gustaría explorar hoy?",
                    "¡Saludos! Estoy aquí para ayudarte con razonamiento lógico."
                ]
            },
            "how_are_you": {
                "patterns": ["cómo estás", "qué tal", "how are you"],
                "answers": [
                    "¡Estoy funcionando al 100%! Listo para ayudarte.",
                    "Como un programa de IA puede estar, ¡excelente!",
                    "Siempre bien cuando puedo ayudar a alguien como tú."
                ]
            },
            "help": {
                "patterns": ["ayuda", "puedes ayudarme", "qué puedes hacer"],
                "answers": [
                    "Claro que sí. Puedo ayudarte con:\n- Razonamiento deductivo\n- Razonamiento inductivo\n- Solución de problemas\n¿Qué necesitas?",
                    "Puedo asistirte con análisis lógico. Por ejemplo:\n1. Si A=B y B=C, entonces A=C\n2. Identificar patrones en observaciones\n¿En qué te ayudo?",
                    "Mis capacidades incluyen:\n• Analizar premisas\n• Encontrar patrones\n• Guiarte en problemas\nDime qué necesitas."
                ]
            },
            "thanks": {
                "patterns": ["gracias", "thank you", "te lo agradezco"],
                "answers": [
                    "¡De nada! Siempre es un placer ayudar.",
                    "No hay de qué. ¿Necesitas algo más?",
                    "¡Gracias a ti por usar mis servicios! 😊"
                ]
            },
            "default": [
                "No estoy seguro de entender. ¿Podrías reformular?",
                "Interesante pregunta. Sobre razonamiento lógico puedo ayudarte mejor.",
                "Puedo explicarte sobre deducción, inducción o resolver problemas. ¿Qué prefieres?"
            ]
        }

    def process_input(self, user_input):
        user_input = user_input.lower().strip(",.!?")
        response = None

        # Verificar patrones especiales primero
        for intent, data in self.responses.items():
            if any(pattern in user_input for pattern in data["patterns"]):
                response = random.choice(data["answers"])
                break

        # Respuesta por defecto si no coincide con patrones
        if not response:
            response = random.choice(self.responses["default"])

        # Mantener contexto de conversación
        self.context.append((user_input, response))
        if len(self.context) > 5:  # Limitar el historial
            self.context.pop(0)

        return response