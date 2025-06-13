class ProblemSolver:
    def __init__(self):
        self.problems = {
            "mate": {
                "description": "Resolver ecuación 2x + 5 = 15",
                "steps": [
                    ("Restar 5 a ambos lados", "2x = 10"),
                    ("Dividir por 2", "x = 5")
                ]
            },
            "logica": {
                "description": "Si todos los A son B y algunos B son C, ¿qué podemos concluir?",
                "steps": [
                    ("Analizar primera premisa", "Todos los A están contenidos en B"),
                    ("Analizar segunda premisa", "Algunos elementos de B están en C"),
                    ("Concluir", "Por lo tanto, algunos A pueden ser C")
                ]
            },
            "ruta": {
                "description": "Encontrar la ruta más corta del punto A al D",
                "steps": [
                    ("Analizar opciones", "A->B->D (10km), A->C->D (8km)"),
                    ("Comparar distancias", "La ruta A->C->D es más corta"),
                    ("Seleccionar", "Tomar la ruta A->C->D")
                ]
            }
        }

    def solve(self, problem_type):
        if problem_type in self.problems:
            return self.problems[problem_type]
        return {"description": "Problema no reconocido", "steps": []}