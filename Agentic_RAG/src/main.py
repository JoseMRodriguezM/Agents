import os
import dotenv
from agentic_rag.crew import InformationAnalystCrew

dotenv.load_dotenv()


def run():
    inputs = {
      'question': '¿Cuál es la definición de derivada parcial?¿Cómo puedo calcularla? Además proporcionar ejemplos de calculos.',
      'file': 'C:\\Users\\jmrod\\Documentos\\Mis_Docs\\EstudioProductividad\\Facultad\\Segundo\\Análisis_Matemático_2\\Libros',
    }
    InformationAnalystCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
