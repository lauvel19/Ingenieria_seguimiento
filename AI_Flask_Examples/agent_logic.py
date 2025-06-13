import random
import re
from datetime import datetime


class EnhancedIntelligentAgent:
    def __init__(self):
        self.context = []
        self.user_name = None
        self.conversation_count = 0
        self.last_topic = None
        self.awaiting_response = None  # Para conversaciones de seguimiento
        self.explanation_depth = 0  # Para saber qué tan profundo ir

        # Patrones de respuesta para seguimiento
        self.follow_up_patterns = {
            "affirmative": [
                r"sí|si|yes|claro|perfecto|dale|ok|está bien|me gustaría|quiero|por favor",
                r"háblame|explícame|cuéntame|dime|enséñame"
            ],
            "negative": [
                r"no|nah|no gracias|paso|mejor no|otro tema|cambiar",
                r"ya entendí|suficiente|otro"
            ],
            "more_info": [
                r"más|otro ejemplo|otra|continúa|sigue|profundiza|más detalles|amplía",
                r"qué más|y qué|también|además"
            ]
        }

        # Ejemplos y explicaciones detalladas
        self.detailed_explanations = {
            "deductive_basic": """
🧠 **Razonamiento Deductivo Explicado:**

El razonamiento deductivo es como ser un detective que sigue pistas 100% confiables. 

**🔍 Características principales:**
• Va de lo GENERAL a lo ESPECÍFICO
• Si las premisas son verdaderas, la conclusión ES NECESARIAMENTE verdadera
• Es el tipo de razonamiento más riguroso y confiable

**📝 Estructura básica:**
1. **Premisa Mayor:** Una regla general (Ej: "Todos los humanos son mortales")
2. **Premisa Menor:** Un caso específico (Ej: "Sócrates es humano") 
3. **Conclusión:** Lo que se deduce necesariamente (Ej: "Sócrates es mortal")

**✅ ¿Por qué funciona?**
Porque si TODOS los humanos son mortales (regla universal) y Sócrates ES humano (caso particular), entonces lógicamente Sócrates DEBE ser mortal.
            """,

            "deductive_examples": [
                {
                    "title": "🏥 Ejemplo Médico",
                    "premise1": "Todos los antibióticos combaten bacterias",
                    "premise2": "La penicilina es un antibiótico",
                    "conclusion": "La penicilina combate bacterias",
                    "explanation": "Este es un silogismo perfecto: regla médica + clasificación específica = conclusión válida"
                },
                {
                    "title": "🔢 Ejemplo Matemático",
                    "premise1": "Todos los números pares son divisibles por 2",
                    "premise2": "El 14 es un número par",
                    "conclusion": "El 14 es divisible por 2",
                    "explanation": "En matemáticas, las reglas son absolutas, por eso la deducción es tan poderosa"
                },
                {
                    "title": "🌍 Ejemplo Geográfico",
                    "premise1": "Todas las capitales europeas están en Europa",
                    "premise2": "Madrid es una capital europea",
                    "conclusion": "Madrid está en Europa",
                    "explanation": "Definiciones geográficas claras nos dan conclusiones incuestionables"
                }
            ],

            "inductive_basic": """
🔍 **Razonamiento Inductivo Explicado:**

El razonamiento inductivo es como ser un científico que descubre patrones observando el mundo.

**🌟 Características principales:**
• Va de lo ESPECÍFICO a lo GENERAL
• Las conclusiones son PROBABLES, no garantizadas
• Es fundamental para el método científico y el aprendizaje

**📊 Proceso:**
1. **Observar:** Casos específicos (Ej: "Cisne 1 es blanco, Cisne 2 es blanco...")
2. **Identificar patrón:** Buscar regularidades (Ej: "Todos los cisnes observados son blancos")
3. **Generalizar:** Crear una regla (Ej: "Todos los cisnes son blancos")

**⚠️ Limitaciones importantes:**
• Una sola excepción puede derribar la regla (cisnes negros existen!)
• La calidad de la muestra es crucial
• Más observaciones = mayor confianza, pero nunca certeza absoluta

**🧪 ¿Por qué es valioso?**
Sin inducción no tendríamos ciencia, no podríamos aprender de la experiencia ni formar hipótesis sobre el mundo.
            """,

            "inductive_examples": [
                {
                    "title": "🦢 El Famoso Cisne Negro",
                    "observations": ["Cisne 1: blanco", "Cisne 2: blanco", "Cisne 3: blanco", "Cisne 4: blanco"],
                    "generalization": "Todos los cisnes son blancos",
                    "plot_twist": "¡Pero existen cisnes negros en Australia!",
                    "lesson": "Una sola excepción puede derribar toda la teoría inductiva"
                },
                {
                    "title": "☀️ Patrón Solar",
                    "observations": ["El sol salió ayer", "El sol salió hoy", "El sol ha salido todos los días"],
                    "generalization": "El sol siempre sale",
                    "strength": "ALTA - millones de observaciones consistentes",
                    "lesson": "Más observaciones = mayor confianza en el patrón"
                },
                {
                    "title": "🍎 Gravedad Observada",
                    "observations": ["La manzana cae", "La piedra cae", "La lluvia cae", "Todo objeto cae"],
                    "generalization": "Todos los objetos caen hacia abajo",
                    "evolution": "Newton: ley de gravedad → Einstein: curvatura del espacio-tiempo",
                    "lesson": "Las generalizaciones inductivas pueden evolucionar con nueva evidencia"
                }
            ]
        }

        # Patrones mejorados con manejo de seguimiento
        self.patterns = {
            "greetings": {
                "patterns": [
                    r"hola|hi|hello|buenos días|buenas tardes|buenas noches|saludos",
                    r"qué tal|cómo estás|how are you"
                ],
                "responses": [
                    "¡Hola! 😊 Soy tu asistente especializado en razonamiento lógico. Puedo explicarte sobre deducción, inducción, agentes inteligentes y resolución de problemas. ¿Qué te gustaría explorar primero?",
                    "¡Perfecto que estés aquí! 🌟 Soy experto en lógica y IA. Podemos conversar sobre razonamiento deductivo (de general a específico), inductivo (de específico a general), o cualquier concepto de inteligencia artificial. ¿Por dónde empezamos?",
                    "¡Bienvenido al mundo del razonamiento lógico! 🧠 Estoy aquí para ayudarte a entender cómo funcionan los diferentes tipos de pensamiento lógico. ¿Te interesa más la deducción rigurosa o la inducción científica?"
                ]
            },

            "reasoning_deductive_request": {
                "patterns": [
                    r"razonamiento deductivo|deducción|deductivo|explícame.*deductivo",
                    r"qué es.*deductivo|cómo funciona.*deductivo|háblame.*deductivo"
                ],
                "responses": [
                    lambda: self.get_deductive_explanation(),
                    lambda: self.get_deductive_explanation_with_example()
                ]
            },

            "reasoning_inductive_request": {
                "patterns": [
                    r"razonamiento inductivo|inducción|inductivo|explícame.*inductivo",
                    r"qué es.*inductivo|cómo funciona.*inductivo|háblame.*inductivo"
                ],
                "responses": [
                    lambda: self.get_inductive_explanation(),
                    lambda: self.get_inductive_explanation_with_example()
                ]
            },

            "example_request": {
                "patterns": [
                    r"ejemplo|ejemplos|muéstrame|ponme un ejemplo|dame un ejemplo",
                    r"cómo sería|ilustra|demuestra"
                ],
                "responses": [
                    lambda: self.provide_contextual_example()
                ]
            },

            "practice_request": {
                "patterns": [
                    r"practicar|práctica|entrenar|ejercicio|ejercicios|probar",
                    r"quiero intentar|déjame probar|cómo lo hago"
                ],
                "responses": [
                    lambda: self.suggest_practice()
                ]
            }
        }

    def get_deductive_explanation(self):
        self.awaiting_response = "deductive_follow_up"
        return self.detailed_explanations[
            "deductive_basic"] + "\n\n💡 ¿Te gustaría que te muestre algunos ejemplos concretos para verlo en acción?"

    def get_deductive_explanation_with_example(self):
        self.awaiting_response = "deductive_more_examples"
        explanation = self.detailed_explanations["deductive_basic"]
        example = random.choice(self.detailed_explanations["deductive_examples"])

        result = explanation + f"\n\n{example['title']}\n"
        result += f"📋 **Premisa 1:** {example['premise1']}\n"
        result += f"📋 **Premisa 2:** {example['premise2']}\n"
        result += f"✅ **Conclusión:** {example['conclusion']}\n"
        result += f"💭 **¿Por qué funciona?** {example['explanation']}\n\n"
        result += "¿Quieres ver más ejemplos o prefieres que practiquemos juntos?"

        return result

    def get_inductive_explanation(self):
        self.awaiting_response = "inductive_follow_up"
        return self.detailed_explanations[
            "inductive_basic"] + "\n\n🔬 ¿Te muestro algunos ejemplos fascinantes para que veas cómo funciona en la práctica?"

    def get_inductive_explanation_with_example(self):
        self.awaiting_response = "inductive_more_examples"
        explanation = self.detailed_explanations["inductive_basic"]
        example = random.choice(self.detailed_explanations["inductive_examples"])

        result = explanation + f"\n\n{example['title']}\n"
        result += f"📊 **Observaciones:** {', '.join(example['observations'])}\n"
        result += f"📈 **Generalización:** {example['generalization']}\n"

        if 'plot_twist' in example:
            result += f"🎭 **Plot twist:** {example['plot_twist']}\n"
        if 'strength' in example:
            result += f"💪 **Fortaleza:** {example['strength']}\n"
        if 'evolution' in example:
            result += f"🔄 **Evolución:** {example['evolution']}\n"

        result += f"🎓 **Lección:** {example['lesson']}\n\n"
        result += "¿Quieres explorar más ejemplos o te explico las limitaciones del razonamiento inductivo?"

        return result

    def provide_contextual_example(self):
        if self.last_topic == "reasoning_deductive_request":
            return self.get_random_deductive_example()
        elif self.last_topic == "reasoning_inductive_request":
            return self.get_random_inductive_example()
        else:
            return "¿De qué tema te gustaría un ejemplo? ¿Razonamiento deductivo, inductivo, agentes inteligentes o resolución de problemas?"

    def get_random_deductive_example(self):
        self.awaiting_response = "deductive_more_examples"
        example = random.choice(self.detailed_explanations["deductive_examples"])

        result = f"🎯 {example['title']}\n\n"
        result += f"**1. Premisa Mayor:** {example['premise1']}\n"
        result += f"**2. Premisa Menor:** {example['premise2']}\n"
        result += f"**3. Conclusión:** {example['conclusion']}\n\n"
        result += f"💡 **Explicación:** {example['explanation']}\n\n"
        result += "¿Te muestro otro ejemplo o quieres que practiquemos creando uno juntos?"

        return result

    def get_random_inductive_example(self):
        self.awaiting_response = "inductive_more_examples"
        example = random.choice(self.detailed_explanations["inductive_examples"])

        result = f"🔍 {example['title']}\n\n"
        result += "**Proceso inductivo paso a paso:**\n"
        result += f"1. **Observaciones:** {', '.join(example['observations'])}\n"
        result += f"2. **Patrón identificado:** {example['generalization']}\n"

        if 'plot_twist' in example:
            result += f"3. **¡Sorpresa!** {example['plot_twist']}\n"
        if 'strength' in example:
            result += f"3. **Evaluación:** {example['strength']}\n"

        result += f"\n🎓 **¿Qué aprendemos?** {example['lesson']}\n\n"
        result += "¿Exploramos otro ejemplo o te explico cómo evaluar la fortaleza de las generalizaciones inductivas?"

        return result

    def suggest_practice(self):
        if self.last_topic == "reasoning_deductive_request":
            self.awaiting_response = "practice_deductive"
            return """🎮 **¡Practiquemos razonamiento deductivo!**

Te voy a dar dos premisas y tú me dices qué conclusión se puede deducir:

**Premisa 1:** Todos los estudiantes universitarios tienen carnet estudiantil
**Premisa 2:** María es estudiante universitaria

🤔 **Tu turno:** ¿Qué puedes concluir sobre María?

💡 **Pista:** Recuerda que en deducción, si las premisas son verdaderas, la conclusión debe ser necesariamente verdadera."""

        elif self.last_topic == "reasoning_inductive_request":
            self.awaiting_response = "practice_inductive"
            return """🧪 **¡Practiquemos razonamiento inductivo!**

Te voy a dar algunas observaciones y tú me dices qué patrón puedes identificar:

**Observaciones:**
• El lunes el café de la cafetería estaba caliente
• El martes el café de la cafetería estaba caliente  
• El miércoles el café de la cafetería estaba caliente
• El jueves el café de la cafetería estaba caliente

🤔 **Tu turno:** ¿Qué generalización puedes hacer? ¿Qué limitaciones tendría esa generalización?

💡 **Pista:** Piensa en el patrón, pero también en qué podría fallar."""

        else:
            return "¿Qué te gustaría practicar? ¿Razonamiento deductivo (crear conclusiones lógicas) o inductivo (identificar patrones)?"

    def handle_follow_up(self, user_input):
        """Maneja las respuestas de seguimiento según el contexto"""

        # Detectar tipo de respuesta
        response_type = self.detect_response_type(user_input)

        if self.awaiting_response == "deductive_follow_up":
            if response_type == "affirmative":
                return self.get_random_deductive_example()
            elif response_type == "negative":
                return "¡Perfecto! ¿Hay algún otro tema sobre razonamiento lógico que te interese? Puedo explicarte sobre inducción, agentes inteligentes o resolución de problemas."
            elif response_type == "more_info":
                return self.get_deductive_explanation_with_example()

        elif self.awaiting_response == "inductive_follow_up":
            if response_type == "affirmative":
                return self.get_random_inductive_example()
            elif response_type == "negative":
                return "¡Entendido! ¿Te interesa explorar otro tipo de razonamiento? Podemos hablar de deducción, agentes inteligentes o cómo representar problemas."
            elif response_type == "more_info":
                return self.get_inductive_explanation_with_example()

        elif self.awaiting_response == "deductive_more_examples":
            if response_type == "affirmative" or "otro" in user_input.lower():
                return self.get_random_deductive_example()
            elif "practi" in user_input.lower():
                return self.suggest_practice()

        elif self.awaiting_response == "inductive_more_examples":
            if response_type == "affirmative" or "otro" in user_input.lower():
                return self.get_random_inductive_example()
            elif "limita" in user_input.lower():
                return self.explain_inductive_limitations()

        elif self.awaiting_response == "practice_deductive":
            return self.evaluate_deductive_practice(user_input)

        elif self.awaiting_response == "practice_inductive":
            return self.evaluate_inductive_practice(user_input)

        return None

    def detect_response_type(self, user_input):
        """Detecta el tipo de respuesta del usuario"""
        user_input_lower = user_input.lower()

        for response_type, patterns in self.follow_up_patterns.items():
            for pattern in patterns:
                if re.search(pattern, user_input_lower):
                    return response_type
        return "other"

    def explain_inductive_limitations(self):
        self.awaiting_response = None
        return """⚠️ **Limitaciones del Razonamiento Inductivo:**

**1. 🦢 El Problema del Cisne Negro**
• Una sola excepción puede derribar toda la teoría
• Ejemplo: "Todos los cisnes son blancos" se derrumba con un cisne negro

**2. 📊 Sesgo de Muestra**
• Muestras pequeñas → generalizaciones poco confiables
• Muestras sesgadas → conclusiones erróneas

**3. 🔄 Falacia Post Hoc**
• Confundir correlación con causación
• "Cada vez que uso paraguas llueve" ≠ "Mi paraguas causa lluvia"

**4. ⏰ Dependencia Temporal**
• Los patrones pueden cambiar con el tiempo
• "Las acciones siempre suben" (hasta que no...)

**🎓 ¿Por qué seguimos usando inducción?**
¡Porque sin ella no tendríamos ciencia! Es nuestra herramienta para descubrir el mundo, pero siempre con humildad y disposición a cambiar cuando llegue nueva evidencia.

¿Te interesa algún ejemplo específico de estas limitaciones?"""

    def evaluate_deductive_practice(self, user_input):
        self.awaiting_response = None

        # Buscar palabras clave de la respuesta correcta
        if any(word in user_input.lower() for word in
               ["carnet", "carné", "estudiantil", "tiene carnet", "tiene carné"]):
            return """🎉 **¡Excelente!** 

✅ **Respuesta correcta:** María tiene carnet estudiantil.

🧠 **¿Por qué es correcta?**
• Premisa Mayor: TODOS los estudiantes universitarios tienen carnet (regla universal)
• Premisa Menor: María ES estudiante universitaria (caso particular)  
• Conclusión: María DEBE tener carnet (consecuencia lógica necesaria)

Este es un silogismo perfecto: Todos A son B + X es A = X es B

¿Quieres intentar otro ejercicio o prefieres que exploremos otro tipo de razonamiento?"""
        else:
            return f"""🤔 **Veamos tu respuesta:** "{user_input}"

💡 **Pista:** Recuerda la estructura deductiva:
• Si TODOS los estudiantes universitarios tienen carnet...
• Y María ES estudiante universitaria...
• Entonces María ¿qué debe tener?

La clave está en que "TODOS" incluye a María sin excepción. ¿Quieres intentarlo de nuevo?"""

    def evaluate_inductive_practice(self, user_input):
        self.awaiting_response = None

        user_lower = user_input.lower()

        if any(word in user_lower for word in ["café", "caliente", "siempre", "cafetería"]):
            pattern_identified = True
        else:
            pattern_identified = False

        if pattern_identified and any(word in user_lower for word in
                                      ["pero", "sin embargo", "limitación", "excepción", "podría", "fin de semana"]):
            return """🌟 **¡Excelente análisis inductivo!**

✅ **Patrón identificado correctamente:** "El café de la cafetería siempre está caliente"

🎯 **Bonus por considerar limitaciones:** ¡Muy bien pensado!

**Posibles limitaciones de esta generalización:**
• 🕐 **Temporal:** ¿Qué pasa en horarios de cierre?
• 📅 **Días especiales:** ¿Y los fines de semana o feriados?
• ⚡ **Fallas técnicas:** ¿Si se daña la máquina de café?
• 🧹 **Mantenimiento:** ¿Durante la limpieza diaria?

**🔬 ¿Cómo fortalecer la inducción?**
• Más observaciones (observar por más días)
• Diversificar condiciones (diferentes horarios, días)
• Considerar variables externas (clima, feriados, etc.)

¡Has demostrado entender perfectamente tanto el poder como las limitaciones del razonamiento inductivo! ¿Quieres explorar otro tema o profundizar más en este?"""

        elif pattern_identified:
            return """🎉 **¡Bien identificado el patrón!**

✅ **Tu generalización:** El café de la cafetería está/siempre está caliente

🤔 **Pregunta adicional:** Muy buena observación del patrón, pero ¿se te ocurre alguna situación donde esta generalización podría fallar?

💡 **Pista:** Piensa en:
• Diferentes horarios del día
• Días especiales o feriados  
• Posibles fallas técnicas
• Variables que no hemos considerado

El razonamiento inductivo siempre debe considerar sus limitaciones. ¿Qué crees que podría hacer que el café NO esté caliente algún día?"""

        else:
            return f"""🤔 **Tu respuesta:** "{user_input}"

💡 **Guía para el razonamiento inductivo:**

**Paso 1:** ¿Qué tienen en común todas las observaciones?
• Lunes: café caliente
• Martes: café caliente  
• Miércoles: café caliente
• Jueves: café caliente

**Paso 2:** ¿Qué patrón puedes identificar?
**Paso 3:** ¿Qué generalización harías?
**Paso 4:** ¿Qué limitaciones podría tener esa generalización?

¿Quieres intentarlo de nuevo enfocándote en lo que se repite en cada observación?"""

    def process_input(self, user_input):
        """Procesa la entrada con manejo mejorado de conversación"""
        if not user_input.strip():
            return "Por favor, escribe algo para que pueda ayudarte."

        # Extraer nombre si es la primera vez
        name_greeting = ""
        if not self.user_name:
            name_greeting = self.extract_user_name(user_input)

        # Primero verificar si es una respuesta de seguimiento
        if self.awaiting_response:
            follow_up_response = self.handle_follow_up(user_input)
            if follow_up_response:
                self.update_context(user_input, follow_up_response, "follow_up")
                return name_greeting + follow_up_response

        # Buscar patrones principales
        intent = self.match_pattern(user_input)

        if intent:
            response = self.get_contextual_response(intent, user_input)
            if name_greeting:
                response = name_greeting + response
        else:
            response = self.get_default_response(user_input)

        # Actualizar contexto
        self.update_context(user_input, response, intent)

        return response

    def match_pattern(self, user_input):
        """Busca patrones en la entrada del usuario"""
        user_input_lower = user_input.lower()

        for intent, data in self.patterns.items():
            for pattern in data["patterns"]:
                if re.search(pattern, user_input_lower):
                    return intent
        return None

    def get_contextual_response(self, intent, user_input):
        """Genera respuesta contextual, incluyendo funciones lambda"""
        responses = self.patterns[intent]["responses"]

        # Manejar respuestas que son funciones
        if callable(responses[0]):
            return responses[0]()

        # Respuestas normales
        if self.conversation_count == 0:
            response = responses[0]
        elif self.last_topic == intent:
            response = random.choice(responses[1:]) if len(responses) > 1 else responses[0]
        else:
            response = random.choice(responses)

        return response

    def get_default_response(self, user_input):
        """Respuestas por defecto más inteligentes"""
        user_lower = user_input.lower()

        # Detectar temas específicos en entrada no reconocida
        if any(word in user_lower for word in ["agente", "inteligente", "ia", "robot"]):
            return """🤖 **Sobre Agentes Inteligentes:**

Un agente inteligente es una entidad que:
• **Percibe** su entorno (sensores)
• **Procesa** la información (razonamiento)  
• **Actúa** para lograr objetivos (actuadores)

Como yo mismo: percibo tu texto, proceso el significado, y genero respuestas útiles.

¿Te gustaría que profundice en algún aspecto específico de los agentes inteligentes?"""

        elif any(word in user_lower for word in ["problema", "resolver", "solución", "algoritmo"]):
            return """⚡ **Sobre Resolución de Problemas:**

Para resolver problemas sistemáticamente:
1. **Definir** el objetivo claramente
2. **Analizar** el estado actual  
3. **Identificar** acciones posibles
4. **Elegir** la mejor estrategia
5. **Ejecutar** y evaluar

¿Tienes algún problema específico que te gustaría resolver paso a paso?"""

        else:
            return f"""Interesante lo que dices: "{user_input}"

Mi especialidad es el razonamiento lógico y la IA. Puedo ayudarte con:

🧠 **Razonamiento Deductivo** - De lo general a lo específico
🔍 **Razonamiento Inductivo** - De lo específico a lo general  
🤖 **Agentes Inteligentes** - Cómo funciona la IA
⚡ **Resolución de Problemas** - Métodos sistemáticos

¿Cuál de estos temas te interesa más?"""

    def extract_user_name(self, user_input):
        """Extrae el nombre del usuario"""
        name_patterns = [
            r"me llamo (\w+)",
            r"soy (\w+)",
            r"mi nombre es (\w+)",
            r"mi nombre: (\w+)"
        ]

        for pattern in name_patterns:
            match = re.search(pattern, user_input.lower())
            if match:
                self.user_name = match.group(1).title()
                return f"¡Mucho gusto, {self.user_name}! "
        return ""

    def update_context(self, user_input, response, intent):
        """Actualiza el contexto de la conversación"""
        self.context.append({
            "input": user_input,
            "response": response,
            "intent": intent,
            "timestamp": datetime.now(),
            "awaiting_response": self.awaiting_response
        })

        if len(self.context) > 15:  # Mantener más contexto
            self.context.pop(0)

        self.conversation_count += 1
        self.last_topic = intent

    def get_conversation_summary(self):
        """Proporciona un resumen detallado de la conversación"""
        if not self.context:
            return "No hemos conversado aún."

        topics = [exchange.get("intent") for exchange in self.context if exchange.get("intent")]
        topic_counts = {}
        for topic in topics:
            if topic:
                topic_counts[topic] = topic_counts.get(topic, 0) + 1

        summary = f"📊 **Resumen de nuestra conversación:**\n\n"
        summary += f"💬 **Mensajes intercambiados:** {len(self.context)}\n"

        if self.user_name:
            summary += f"👤 **Usuario:** {self.user_name}\n"

        if topic_counts:
            summary += f"\n**🎯 Temas explorados:**\n"
            for topic, count in topic_counts.items():
                topic_name = topic.replace("_", " ").title()
                summary += f"• {topic_name}: {count} veces\n"

            main_topic = max(topic_counts, key=topic_counts.get)
            summary += f"\n**🌟 Tema principal:** {main_topic.replace('_', ' ').title()}"

        if self.awaiting_response:
            summary += f"\n\n⏳ **Estado actual:** Esperando tu respuesta sobre {self.awaiting_response.replace('_', ' ')}"

        return summary

    def reset_conversation(self):
        """Reinicia la conversación"""
        self.context = []
        self.conversation_count = 0
        self.last_topic = None
        self.awaiting_response = None
        self.explanation_depth = 0
        return "🔄 **Conversación reiniciada.** ¡Empecemos de nuevo! ¿Qué te gustaría explorar sobre razonamiento lógico o inteligencia artificial?"