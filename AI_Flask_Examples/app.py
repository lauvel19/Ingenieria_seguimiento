from flask import Flask, render_template, request, jsonify
from agent_logic import EnhancedIntelligentAgent  # Usar el agente mejorado
from reasoning import ImprovedReasoning
from problem_representation import ImprovedProblemSolver

app = Flask(__name__, static_folder='static', static_url_path='/static')

# Instanciar las clases mejoradas
ai_agent = EnhancedIntelligentAgent()  # Agente mejorado
reasoning = ImprovedReasoning()
problem_solver = ImprovedProblemSolver()

# EJEMPLOS EXPANDIDOS PARA RAZONAMIENTO DEDUCTIVO
deductive_examples = [
    # Ejemplos clásicos
    {
        "premise1": "Todos los humanos son mortales",
        "premise2": "Sócrates es humano",
        "conclusion": "Sócrates es mortal",
        "type": "Silogismo clásico"
    },
    {
        "premise1": "Todos los artistas son banqueros",
        "premise2": "Todos los banqueros son cantantes",
        "conclusion": "Todos los artistas son cantantes",
        "type": "Silogismo categórico"
    },
    {
        "premise1": "Si llueve entonces el suelo está mojado",
        "premise2": "Está lloviendo",
        "conclusion": "El suelo está mojado",
        "type": "Modus Ponens"
    },

    # Ejemplos de animales
    {
        "premise1": "Todos los mamíferos tienen sangre caliente",
        "premise2": "Todos los perros son mamíferos",
        "conclusion": "Todos los perros tienen sangre caliente",
        "type": "Cadena lógica"
    },
    {
        "premise1": "Todos los pájaros tienen plumas",
        "premise2": "El águila es un pájaro",
        "conclusion": "El águila tiene plumas",
        "type": "Clasificación"
    },
    {
        "premise1": "Ningún reptil es mamífero",
        "premise2": "Todos los cocodrilos son reptiles",
        "conclusion": "Ningún cocodrilo es mamífero",
        "type": "Silogismo negativo"
    },

    # Ejemplos matemáticos
    {
        "premise1": "Todos los números pares son divisibles por 2",
        "premise2": "El 8 es un número par",
        "conclusion": "El 8 es divisible por 2",
        "type": "Matemático"
    },
    {
        "premise1": "Si un número es primo mayor que 2, entonces es impar",
        "premise2": "El 7 es primo mayor que 2",
        "conclusion": "El 7 es impar",
        "type": "Condicional matemático"
    },

    # Ejemplos de profesiones
    {
        "premise1": "Todos los médicos han estudiado medicina",
        "premise2": "Ana es médica",
        "conclusion": "Ana ha estudiado medicina",
        "type": "Profesional"
    },
    {
        "premise1": "Todos los estudiantes universitarios tienen carnet estudiantil",
        "premise2": "Carlos es estudiante universitario",
        "conclusion": "Carlos tiene carnet estudiantil",
        "type": "Institucional"
    },

    # Ejemplos tecnológicos
    {
        "premise1": "Todos los smartphones tienen pantalla táctil",
        "premise2": "El iPhone es un smartphone",
        "conclusion": "El iPhone tiene pantalla táctil",
        "type": "Tecnológico"
    },
    {
        "premise1": "Si un dispositivo tiene WiFi entonces puede conectarse a internet",
        "premise2": "Mi laptop tiene WiFi",
        "conclusion": "Mi laptop puede conectarse a internet",
        "type": "Condicional tecnológico"
    },

    # Ejemplos geográficos
    {
        "premise1": "Todas las capitales europeas están en Europa",
        "premise2": "París es una capital europea",
        "conclusion": "París está en Europa",
        "type": "Geográfico"
    },
    {
        "premise1": "Todos los países de América del Sur están en el hemisferio sur",
        "premise2": "Brasil es un país de América del Sur",
        "conclusion": "Brasil está en el hemisferio sur",
        "type": "Continental"
    }
]

# EJEMPLOS EXPANDIDOS PARA RAZONAMIENTO INDUCTIVO
inductive_examples = [
    # Ejemplos clásicos
    ["El cisne 1 es blanco", "El cisne 2 es blanco", "El cisne 3 es blanco", "El cisne 4 es blanco"],
    ["La manzana es roja", "La fresa es roja", "El tomate es rojo", "La cereza es roja"],
    ["El pájaro 1 vuela", "El pájaro 2 vuela", "El pájaro 3 vuela", "El pájaro 4 vuela"],

    # Ejemplos de comportamiento animal
    ["El perro 1 ladra", "El perro 2 ladra", "El perro 3 ladra", "El perro 4 ladra"],
    ["El gato 1 maúlla", "El gato 2 maúlla", "El gato 3 maúlla", "El gato 4 maúlla"],
    ["El delfín 1 es inteligente", "El delfín 2 es inteligente", "El delfín 3 es inteligente"],

    # Ejemplos de fenómenos naturales
    ["El sol sale por el este el lunes", "El sol sale por el este el martes", "El sol sale por el este el miércoles"],
    ["En enero hace frío", "En febrero hace frío", "En marzo hace frío"],
    ["Las plantas necesitan agua para crecer", "Los árboles necesitan agua para crecer",
     "Las flores necesitan agua para crecer"],

    # Ejemplos de comportamiento humano
    ["Los estudiantes estudian para los exámenes", "Los estudiantes repasan antes de los exámenes",
     "Los estudiantes se preparan para los exámenes"],
    ["Los niños juegan en el parque", "Los niños corren en el parque", "Los niños se divierten en el parque"],
    ["Los médicos ayudan a los pacientes", "Los médicos curan a los enfermos", "Los médicos salvan vidas"],

    # Ejemplos tecnológicos
    ["Mi teléfono se carga con USB", "Mi tablet se carga con USB", "Mi cámara se carga con USB"],
    ["Google es rápido", "Google es preciso", "Google es útil"],
    ["Las computadoras procesan datos", "Las computadoras almacenan información",
     "Las computadoras ejecutan programas"],

    # Ejemplos de comida
    ["Las naranjas son dulces", "Las manzanas son dulces", "Las uvas son dulces"],
    ["El café es caliente", "El té es caliente", "El chocolate es caliente"],
    ["El pan es nutritivo", "El arroz es nutritivo", "La pasta es nutritiva"],

    # Ejemplos de materiales
    ["El hierro es fuerte", "El acero es fuerte", "El titanio es fuerte"],
    ["El agua es transparente", "El cristal es transparente", "El aire es transparente"],
    ["El oro es valioso", "Los diamantes son valiosos", "La plata es valiosa"],

    # Ejemplos de transporte
    ["Los autos tienen ruedas", "Los camiones tienen ruedas", "Las motocicletas tienen ruedas"],
    ["Los aviones vuelan", "Los helicópteros vuelan", "Los drones vuelan"],
    ["Los barcos flotan", "Los botes flotan", "Las balsas flotan"],

    # Ejemplos de emociones
    ["Cuando llueve me siento triste", "Cuando está nublado me siento triste", "Cuando hace frío me siento triste"],
    ["Los cumpleaños me alegran", "Las fiestas me alegran", "Las vacaciones me alegran"],
    ["La música clásica me relaja", "Los sonidos de la naturaleza me relajan", "La meditación me relaja"]
]


# En tu app.py, reemplaza la función home() con esta:

@app.route('/')
def home():
    """Página principal que usa el template base.html correctamente"""
    return render_template('base.html',
                         available_problems=problem_solver.get_available_problems())

@app.route('/deductive', methods=['GET', 'POST'])
def deductive():
    """Página de razonamiento deductivo con ejemplos expandidos"""
    conclusion = None
    analysis = None

    if request.method == 'POST':
        premise1 = request.form.get('premise1', '').strip()
        premise2 = request.form.get('premise2', '').strip()

        if premise1 and premise2:
            conclusion = reasoning.deductive_reasoning(premise1, premise2)

            # Análisis adicional si el usuario proporciona una conclusión
            user_conclusion = request.form.get('conclusion', '').strip()
            if user_conclusion:
                analysis = reasoning.analyze_argument_strength(premise1, premise2, user_conclusion)

    return render_template('deductive.html',
                           conclusion=conclusion,
                           analysis=analysis,
                           examples=deductive_examples)


@app.route('/inductive', methods=['GET', 'POST'])
def inductive():
    """Página de razonamiento inductivo con ejemplos expandidos"""
    conclusion = None

    if request.method == 'POST':
        observations = []
        for i in range(1, 6):  # Hasta 5 observaciones
            obs = request.form.get(f'observation{i}', '').strip()
            if obs:
                observations.append(obs)

        if observations:
            conclusion = reasoning.inductive_reasoning(observations)

    return render_template('inductive.html',
                           conclusion=conclusion,
                           examples=inductive_examples)


@app.route('/agent', methods=['GET', 'POST'])
def agent():
    """Página del agente inteligente mejorado"""
    agent_response = None
    conversation_summary = None

    if request.method == 'POST':
        action = request.form.get('action', '')

        if action == 'reset':
            agent_response = ai_agent.reset_conversation()
        elif action == 'summary':
            conversation_summary = ai_agent.get_conversation_summary()
        else:
            user_input = request.form.get('user_input', '').strip()
            if user_input:
                agent_response = ai_agent.process_input(user_input)

    return render_template('agent.html',
                           agent_response=agent_response,
                           conversation_summary=conversation_summary,
                           user_name=ai_agent.user_name,
                           conversation_count=ai_agent.conversation_count)


@app.route('/problem')
def problem():
    """Página de representación de problemas"""
    problem_type = request.args.get('type', 'matematico')
    show_comparison = request.args.get('compare', 'false') == 'true'

    problem_data = problem_solver.solve(problem_type)
    step_by_step = problem_solver.solve_step_by_step(problem_type)
    comparison = None

    if show_comparison:
        comparison = problem_solver.compare_algorithms(problem_type)

    return render_template('problem_visualization.html',
                           problem=problem_data,
                           step_by_step=step_by_step,
                           comparison=comparison,
                           available_problems=problem_solver.get_available_problems(),
                           current_type=problem_type)


@app.route('/combined', methods=['GET', 'POST'])
def combined():
    """Página combinada con todas las funcionalidades"""
    response = {
        'agent': None,
        'deductive': None,
        'inductive': None,
        'problem': None,
        'problem_summary': None
    }

    if request.method == 'POST':
        # Procesar interacción con el agente
        if 'agent_input' in request.form and request.form['agent_input'].strip():
            user_input = request.form['agent_input'].strip()
            response['agent'] = ai_agent.process_input(user_input)

        # Procesar razonamiento deductivo
        if all(key in request.form and request.form[key].strip()
               for key in ['premise1', 'premise2']):
            response['deductive'] = reasoning.deductive_reasoning(
                request.form['premise1'].strip(),
                request.form['premise2'].strip()
            )

        # Procesar razonamiento inductivo
        observations = []
        for i in range(1, 6):
            obs = request.form.get(f'observation{i}', '').strip()
            if obs:
                observations.append(obs)

        if observations:
            response['inductive'] = reasoning.inductive_reasoning(observations)

        # Mostrar información de problema
        problem_type = request.form.get('problem_type', 'matematico')
        if problem_type:
            response['problem'] = problem_solver.solve(problem_type)
            response['problem_summary'] = problem_solver.get_problem_summary(problem_type)

    return render_template('combined.html',
                           **response,
                           available_problems=problem_solver.get_available_problems(),
                           inductive_examples=inductive_examples)


# API endpoints (mantener los mismos)
@app.route('/api/agent', methods=['POST'])
def api_agent():
    """API endpoint para el agente inteligente"""
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Mensaje requerido'}), 400

    response = ai_agent.process_input(data['message'])
    return jsonify({
        'response': response,
        'conversation_count': ai_agent.conversation_count,
        'user_name': ai_agent.user_name
    })


if __name__ == '__main__':
    print("🚀 Iniciando aplicación de IA con Flask...")
    print("📚 Funcionalidades disponibles:")
    print("   • Razonamiento Deductivo mejorado con", len(deductive_examples), "ejemplos")
    print("   • Razonamiento Inductivo con", len(inductive_examples), "ejemplos")
    print("   • Agente Inteligente conversacional mejorado")
    print("   • Representación de Problemas paso a paso")
    print("\n🌐 Accede a http://localhost:5000")

    app.run(debug=True, host='0.0.0.0', port=5000)