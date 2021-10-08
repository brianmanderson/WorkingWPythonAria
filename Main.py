import pyesapi
import atexit

app = pyesapi.CustomScriptExecutable.CreateApplication('python_demo')
atexit.register(app.Dispose)

pat = app.OpenPatientById('')
xxx = 1