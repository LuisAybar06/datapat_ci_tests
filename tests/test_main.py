import os
import nbformat
from nbconvert import PythonExporter
import importlib.util
import unittest

# Función para convertir un archivo .ipynb a .py
def convert_ipynb_to_py(ipynb_file):
    py_exporter = PythonExporter()
    with open(ipynb_file, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)
        py_code, _ = py_exporter.from_notebook_node(notebook)
    py_file = os.path.splitext(ipynb_file)[0] + '.py'
    with open(py_file, 'w', encoding='utf-8') as f:
        f.write(py_code)
    return py_file

def get_ipynb_path():
    # Ruta al directorio actual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Ruta al directorio my_app
    my_app_dir = os.path.join(current_dir, '..', 'my_app')
    # Ruta al archivo .ipynb dentro de my_app
    ipynb_file = os.path.join(my_app_dir, 'pipeline_prediction_model_v1-2.ipynb')
    return ipynb_file

class TestMyApp(unittest.TestCase):
    def setUp(self):
        # Convertir el archivo .ipynb a .py
        self.py_file = convert_ipynb_to_py(get_ipynb_path())

        # Importar las funciones del archivo .py generado
        spec = importlib.util.spec_from_file_location("my_app", self.py_file)
        self.my_app = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.my_app)

    def test_error_op(self):
        result = self.my_app.error_op("Test Message")
        self.assertTrue(isinstance(result, Exception))

    def tearDown(self):
        # Eliminar el archivo .py generado
        os.remove(self.py_file)

    # def test_validate_data(self):
    #     result = self.my_app.validate_data("table_name")
    #     self.assertTrue(isinstance(result, tuple))

if __name__ == '__main__':
    unittest.main()
