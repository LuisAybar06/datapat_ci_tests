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
    current_dir = os.path.dirname(os.path.abspath(__file__))
    my_app_dir = os.path.join(current_dir, '..', 'my_app')
    ipynb_file = os.path.join(my_app_dir, 'pipeline_prediction_model_v1-2.ipynb')
    return ipynb_file

class TestMyApp(unittest.TestCase):
    def setUp(self):
        # Convertir el archivo .ipynb a .py
        self.py_file = convert_ipynb_to_py(get_ipynb_path())

        # Importar la función error_op del archivo .py generado
        spec = importlib.util.spec_from_file_location("error_op", self.py_file)
        my_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(my_module)
        
        # Asignar la función error_op a un atributo de la clase de prueba
        self.error_op = my_module.error_op

    def test_error_op(self):
        result = self.error_op("Test Message")
        self.assertTrue(isinstance(result, Exception))

    def tearDown(self):
        # Eliminar el archivo .py generado
        os.remove(self.py_file)

if __name__ == '__main__':
    unittest.main()
