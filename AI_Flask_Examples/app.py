from flask import Flask, render_template, request
from agent_logic import IntelligentAgent
from reasoning import deductive_reasoning, inductive_reasoning
from problem_representation import ProblemSolver
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__, static_folder='static', static_url_path='/static')

ai_agent = IntelligentAgent()
problem_solver = ProblemSolver()

# Configuración de ejemplos para el razonamiento inductivo
inductive_examples = [
    ["El pájaro 1 vuela", "El pájaro 2 vuela", "El pájaro 3 vuela"],
    ["La manzana es roja", "La fresa es roja", "El tomate es rojo"],
    ["El coche usa gasolina", "La moto usa gasolina", "El camión usa gasolina"]
]


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/deductive', methods=['GET', 'POST'])
def deductive():
    conclusion = None
    if request.method == 'POST':
        premise1 = request.form.get('premise1', '')
        premise2 = request.form.get('premise2', '')
        conclusion = deductive_reasoning(premise1, premise2)

    return render_template('deductive.html',
                           conclusion=conclusion,
                           example={
                               "premise1": "Todos los humanos son mortales",
                               "premise2": "Sócrates es humano",
                               "conclusion": "Sócrates es mortal"
                           })


@app.route('/inductive', methods=['GET', 'POST'])
def inductive():
    conclusion = None
    if request.method == 'POST':
        observations = [
            request.form.get(f'observation{i}', '')
            for i in range(1, 4)
        ]
        conclusion = inductive_reasoning(observations)

    return render_template('inductive.html',
                           conclusion=conclusion,
                           examples=inductive_examples)


@app.route('/agent', methods=['GET', 'POST'])
def agent():
    agent_response = None
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        agent_response = ai_agent.process_input(user_input)

    return render_template('agent.html',
                           agent_response=agent_response)


@app.route('/problem')
def problem():
    problem_types = ["mate", "logica", "ruta"]
    solutions = {pt: problem_solver.solve(pt) for pt in problem_types}
    return render_template('problem_visualization.html',
                           solutions=solutions)


@app.route('/combined', methods=['GET', 'POST'])
def combined():
    response = {
        'agent': None,
        'deductive': None,
        'inductive': None,
        'problem': None
    }

    if request.method == 'POST':
        # Procesar interacción con el agente
        if 'agent_input' in request.form:
            user_input = request.form['agent_input'].lower()
            # ... (tu lógica existente para el agente)

        # Procesar razonamiento deductivo
        if all(key in request.form for key in ['premise1', 'premise2']):
            response['deductive'] = deductive_reasoning(
                request.form['premise1'],
                request.form['premise2']
            )

        # Procesar razonamiento inductivo (CORRECCIÓN CLAVE)
        if any(f'observation{i}' in request.form for i in range(1, 4)):
            observations = [
                request.form.get(f'observation{i}', '')
                for i in range(1, 4)
            ]
            response['inductive'] = inductive_reasoning(observations)

            # Si no hay respuesta del agente, agregar una genérica
            if not response['agent'] and response['inductive']:
                response['agent'] = "He analizado tus observaciones inductivas. ¿Quieres probar con otras?"

    return render_template('combined.html', **response)


if __name__ == '__main__':
    app.run(debug=True)