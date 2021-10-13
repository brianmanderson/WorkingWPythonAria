from PyESAPI import pyesapi
import atexit
import os

app = pyesapi.CustomScriptExecutable.CreateApplication('python_demo')
atexit.register(app.Dispose)
fid = open(os.path.join('.', 'PatientID'))
line = fid.readline()
line = fid.readline()
fid.close()
MRN = line.strip('\n')
app.ClosePatient()
patient = app.OpenPatientById(MRN)
plan = patient.CoursesLot(0).PlanSetupsLot(0)
pat = app.OpenPatientById('')
xxx = 1