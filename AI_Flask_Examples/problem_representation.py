from typing import Dict, List, Tuple, Any
import json


class ImprovedProblemSolver:
    """
    Representación de problemas basada en los conceptos del documento:
    - Formulación del objetivo
    - Formulación del problema (acciones y estados)
    - Búsqueda (algoritmos)
    - Ejecución
    """

    def __init__(self):
        self.problems = {
            "matematico": {
                "title": "Resolver Ecuación Algebraica",
                "description": "Resolver la ecuación: 2x + 5 = 15",
                "type": "Problema Matemático",
                "objective": "Encontrar el valor de x que satisface la ecuación",
                "initial_state": "2x + 5 = 15",
                "goal_state": "x = valor numérico",
                "actions": [
                    "Restar 5 a ambos lados",
                    "Dividir ambos lados por 2",
                    "Verificar la solución"
                ],
                "solution_steps": [
                    {
                        "step": 1,
                        "action": "Restar 5 a ambos lados",
                        "state_before": "2x + 5 = 15",
                        "operation": "2x + 5 - 5 = 15 - 5",
                        "state_after": "2x = 10",
                        "explanation": "Eliminamos el término constante del lado izquierdo"
                    },
                    {
                        "step": 2,
                        "action": "Dividir ambos lados por 2",
                        "state_before": "2x = 10",
                        "operation": "(2x) ÷ 2 = 10 ÷ 2",
                        "state_after": "x = 5",
                        "explanation": "Aislamos la variable x"
                    },
                    {
                        "step": 3,
                        "action": "Verificar la solución",
                        "state_before": "x = 5",
                        "operation": "2(5) + 5 = 10 + 5 = 15 ✓",
                        "state_after": "Solución verificada",
                        "explanation": "Confirmamos que x = 5 satisface la ecuación original"
                    }
                ],
                "final_answer": "x = 5",
                "algorithm_type": "Resolución algebraica secuencial"
            },

            "logico": {
                "title": "Análisis de Conjuntos Lógicos",
                "description": "Si todos los A son B y algunos B son C, ¿qué podemos concluir sobre A y C?",
                "type": "Problema de Lógica",
                "objective": "Determinar la relación lógica entre los conjuntos A y C",
                "initial_state": "Premisa 1: ∀x(A(x) → B(x)), Premisa 2: ∃x(B(x) ∧ C(x))",
                "goal_state": "Conclusión sobre la relación A-C",
                "actions": [
                    "Representar con diagramas de Venn",
                    "Analizar intersecciones",
                    "Aplicar reglas de inferencia"
                ],
                "solution_steps": [
                    {
                        "step": 1,
                        "action": "Analizar primera premisa",
                        "state_before": "Todos los A son B",
                        "operation": "A ⊆ B (A es subconjunto de B)",
                        "state_after": "El conjunto A está completamente contenido en B",
                        "explanation": "Si todos los elementos de A están en B, entonces A es subconjunto de B"
                    },
                    {
                        "step": 2,
                        "action": "Analizar segunda premisa",
                        "state_before": "Algunos B son C",
                        "operation": "B ∩ C ≠ ∅ (intersección no vacía)",
                        "state_after": "Existe al menos un elemento que pertenece tanto a B como a C",
                        "explanation": "La intersección entre B y C contiene al menos un elemento"
                    },
                    {
                        "step": 3,
                        "action": "Evaluar relación A-C",
                        "state_before": "A ⊆ B y B ∩ C ≠ ∅",
                        "operation": "A ∩ C = ? (puede ser vacía o no vacía)",
                        "state_after": "No se puede determinar con certeza",
                        "explanation": "Es POSIBLE que algunos A sean C, pero no es necesario"
                    }
                ],
                "final_answer": "Conclusión: Es posible que algunos A sean C, pero no podemos garantizarlo",
                "algorithm_type": "Análisis de conjuntos con lógica proposicional"
            },

            "ruta_optima": {
                "title": "Búsqueda de Ruta Óptima",
                "description": "Encontrar el camino más corto del punto A al punto D en un grafo ponderado",
                "type": "Problema de Optimización",
                "objective": "Minimizar la distancia total del recorrido A → D",
                "initial_state": "Posición: A, Distancia acumulada: 0",
                "goal_state": "Posición: D, Distancia mínima encontrada",
                "graph": {
                    "nodes": ["A", "B", "C", "D"],
                    "edges": {
                        ("A", "B"): 5,
                        ("A", "C"): 3,
                        ("B", "D"): 4,
                        ("C", "D"): 2
                    }
                },
                "actions": [
                    "Explorar todas las rutas posibles",
                    "Calcular distancia total de cada ruta",
                    "Comparar y seleccionar la óptima"
                ],
                "solution_steps": [
                    {
                        "step": 1,
                        "action": "Identificar todas las rutas posibles",
                        "state_before": "Punto de partida: A",
                        "operation": "Enumerar: A→B→D, A→C→D",
                        "state_after": "2 rutas identificadas",
                        "explanation": "Exploramos todas las conexiones desde A hacia D"
                    },
                    {
                        "step": 2,
                        "action": "Calcular distancia ruta 1",
                        "state_before": "Ruta: A → B → D",
                        "operation": "5 km + 4 km = 9 km",
                        "state_after": "Ruta 1: 9 km total",
                        "explanation": "Sumamos las distancias de cada segmento"
                    },
                    {
                        "step": 3,
                        "action": "Calcular distancia ruta 2",
                        "state_before": "Ruta: A → C → D",
                        "operation": "3 km + 2 km = 5 km",
                        "state_after": "Ruta 2: 5 km total",
                        "explanation": "Sumamos las distancias de cada segmento"
                    },
                    {
                        "step": 4,
                        "action": "Comparar y seleccionar óptima",
                        "state_before": "Ruta 1: 9 km, Ruta 2: 5 km",
                        "operation": "min(9, 5) = 5",
                        "state_after": "Ruta óptima: A → C → D",
                        "explanation": "Seleccionamos la ruta con menor distancia total"
                    }
                ],
                "final_answer": "Ruta óptima: A → C → D con 5 km de distancia",
                "algorithm_type": "Búsqueda exhaustiva con comparación"
            },

            "torres_hanoi": {
                "title": "Torres de Hanoi",
                "description": "Mover 3 discos de la torre A a la torre C usando la torre B como auxiliar",
                "type": "Problema de Búsqueda en Espacio de Estados",
                "objective": "Transferir todos los discos a la torre destino respetando las reglas",
                "initial_state": "Torre A: [3,2,1], Torre B: [], Torre C: []",
                "goal_state": "Torre A: [], Torre B: [], Torre C: [3,2,1]",
                "rules": [
                    "Solo se puede mover un disco a la vez",
                    "Solo se puede mover el disco superior de una torre",
                    "No se puede colocar un disco grande sobre uno pequeño"
                ],
                "actions": [
                    "Mover disco de A a B",
                    "Mover disco de A a C",
                    "Mover disco de B a A",
                    "Mover disco de B a C",
                    "Mover disco de C a A",
                    "Mover disco de C a B"
                ],
                "solution_steps": [
                    {
                        "step": 1,
                        "action": "Mover disco 1 de A a C",
                        "state_before": "A:[3,2,1] B:[] C:[]",
                        "operation": "A→C",
                        "state_after": "A:[3,2] B:[] C:[1]",
                        "explanation": "Movemos el disco más pequeño para liberar el disco 2"
                    },
                    {
                        "step": 2,
                        "action": "Mover disco 2 de A a B",
                        "state_before": "A:[3,2] B:[] C:[1]",
                        "operation": "A→B",
                        "state_after": "A:[3] B:[2] C:[1]",
                        "explanation": "Movemos el disco 2 a la torre auxiliar"
                    },
                    {
                        "step": 3,
                        "action": "Mover disco 1 de C a B",
                        "state_before": "A:[3] B:[2] C:[1]",
                        "operation": "C→B",
                        "state_after": "A:[3] B:[2,1] C:[]",
                        "explanation": "Colocamos el disco 1 sobre el disco 2"
                    },
                    {
                        "step": 4,
                        "action": "Mover disco 3 de A a C",
                        "state_before": "A:[3] B:[2,1] C:[]",
                        "operation": "A→C",
                        "state_after": "A:[] B:[2,1] C:[3]",
                        "explanation": "Movemos el disco más grande a su posición final"
                    },
                    {
                        "step": 5,
                        "action": "Mover disco 1 de B a A",
                        "state_before": "A:[] B:[2,1] C:[3]",
                        "operation": "B→A",
                        "state_after": "A:[1] B:[2] C:[3]",
                        "explanation": "Liberamos el disco 2 para poder moverlo"
                    },
                    {
                        "step": 6,
                        "action": "Mover disco 2 de B a C",
                        "state_before": "A:[1] B:[2] C:[3]",
                        "operation": "B→C",
                        "state_after": "A:[1] B:[] C:[3,2]",
                        "explanation": "Colocamos el disco 2 sobre el disco 3"
                    },
                    {
                        "step": 7,
                        "action": "Mover disco 1 de A a C",
                        "state_before": "A:[1] B:[] C:[3,2]",
                        "operation": "A→C",
                        "state_after": "A:[] B:[] C:[3,2,1]",
                        "explanation": "Completamos la transferencia colocando el disco 1 en la cima"
                    }
                ],
                "final_answer": "Problema resuelto en 7 movimientos: 2^n - 1 donde n=3",
                "algorithm_type": "Recursión y divide y vencerás"
            }
        }

    def solve(self, problem_type: str) -> Dict[str, Any]:
        """Retorna la solución completa de un problema específico"""
        if problem_type in self.problems:
            return self.problems[problem_type]
        return {
            "title": "Problema no encontrado",
            "description": f"El tipo '{problem_type}' no está disponible",
            "type": "Error",
            "available_types": list(self.problems.keys())
        }

    def get_available_problems(self) -> List[str]:
        """Retorna lista de problemas disponibles"""
        return list(self.problems.keys())

    def get_problem_summary(self, problem_type: str) -> str:
        """Retorna un resumen textual del problema"""
        if problem_type not in self.problems:
            return f"Problema '{problem_type}' no encontrado"

        problem = self.problems[problem_type]
        summary = f"🎯 {problem['title']}\n"
        summary += f"📝 {problem['description']}\n"
        summary += f"🔍 Tipo: {problem['type']}\n"
        summary += f"🎯 Objetivo: {problem['objective']}\n"
        summary += f"📊 Algoritmo: {problem['algorithm_type']}\n"
        summary += f"✅ Solución: {problem['final_answer']}"

        return summary

    def solve_step_by_step(self, problem_type: str) -> str:
        """Retorna la solución paso a paso en formato texto"""
        if problem_type not in self.problems:
            return f"Problema '{problem_type}' no encontrado"

        problem = self.problems[problem_type]
        solution = f"🎯 **{problem['title']}**\n\n"
        solution += f"📝 **Descripción:** {problem['description']}\n\n"
        solution += f"🎯 **Objetivo:** {problem['objective']}\n\n"
        solution += f"📊 **Estado inicial:** {problem['initial_state']}\n"
        solution += f"🏁 **Estado objetivo:** {problem['goal_state']}\n\n"

        solution += "**🔧 Pasos de la solución:**\n\n"

        for step in problem['solution_steps']:
            solution += f"**Paso {step['step']}:** {step['action']}\n"
            solution += f"   📋 Estado previo: {step['state_before']}\n"
            solution += f"   ⚙️ Operación: {step['operation']}\n"
            solution += f"   📋 Estado resultante: {step['state_after']}\n"
            solution += f"   💡 Explicación: {step['explanation']}\n\n"

        solution += f"✅ **Resultado final:** {problem['final_answer']}\n"
        solution += f"🧠 **Método utilizado:** {problem['algorithm_type']}"

        return solution

    def create_custom_problem(self, title: str, description: str, steps: List[Dict]) -> str:
        """Permite crear un problema personalizado"""
        custom_key = f"custom_{len(self.problems)}"

        self.problems[custom_key] = {
            "title": title,
            "description": description,
            "type": "Problema Personalizado",
            "objective": "Resolver el problema paso a paso",
            "solution_steps": steps,
            "algorithm_type": "Definido por el usuario"
        }

        return f"Problema personalizado '{title}' creado con clave '{custom_key}'"

    def compare_algorithms(self, problem_type: str) -> str:
        """Compara diferentes enfoques algorítmicos para resolver el mismo problema"""
        if problem_type not in self.problems:
            return f"Problema '{problem_type}' no encontrado"

        problem = self.problems[problem_type]

        comparisons = {
            "matematico": {
                "current": "Resolución algebraica secuencial",
                "alternatives": [
                    "Método gráfico (representar la ecuación en un plano)",
                    "Método de ensayo y error (probar valores)",
                    "Método de sustitución (si hay más variables)"
                ],
                "efficiency": "O(1) - Tiempo constante para ecuaciones lineales"
            },
            "logico": {
                "current": "Análisis de conjuntos con lógica proposicional",
                "alternatives": [
                    "Tablas de verdad (para proposiciones complejas)",
                    "Diagramas de Venn (representación visual)",
                    "Resolución formal (sistemas de deducción)"
                ],
                "efficiency": "O(1) - Para casos simples, O(2^n) para casos complejos"
            },
            "ruta_optima": {
                "current": "Búsqueda exhaustiva con comparación",
                "alternatives": [
                    "Algoritmo de Dijkstra (para grafos más grandes)",
                    "A* (búsqueda heurística)",
                    "Algoritmo de Floyd-Warshall (todas las rutas)"
                ],
                "efficiency": "O(V!) para búsqueda exhaustiva, O(V²) para Dijkstra"
            },
            "torres_hanoi": {
                "current": "Recursión y divide y vencerás",
                "alternatives": [
                    "Método iterativo con pilas",
                    "Representación binaria de estados",
                    "Búsqueda en anchura (BFS)"
                ],
                "efficiency": "O(2^n) - exponencial en el número de discos"
            }
        }

        if problem_type in comparisons:
            comp = comparisons[problem_type]
            result = f"🔍 **Análisis de algoritmos para: {problem['title']}**\n\n"
            result += f"**Método actual:** {comp['current']}\n\n"
            result += f"**Métodos alternativos:**\n"
            for alt in comp['alternatives']:
                result += f"   • {alt}\n"
            result += f"\n**Eficiencia computacional:** {comp['efficiency']}"
            return result

        return "No hay análisis de algoritmos disponible para este problema"