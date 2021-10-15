from PyESAPI import pyesapi
import atexit
import os
import SimpleITK as sitk


def get_direction(varian_image):
    x_direction = [varian_image.get_XDirection()[i] for i in range(3)]
    y_direction = [varian_image.get_YDirection()[i] for i in range(3)]
    z_direction = [varian_image.get_ZDirection()[i] for i in range(3)]
    direction = x_direction + y_direction + z_direction
    return tuple(direction)

def get_spacing(varian_image):
    return (varian_image.get_XRes(), varian_image.get_YRes(), varian_image.get_ZRes())

def get_origin(potential_image):
    return tuple([potential_image.get_Origin()[i] for i in range(3)])


def create_sitk_Image(varian_image):
    intercept = varian_image.VoxelToDisplayValue(0)
    image_array = varian_image.np_array_like().transpose()
    image_handle = sitk.GetImageFromArray(image_array + intercept)
    image_handle.SetSpacing(get_spacing(varian_image))
    image_handle.SetDirection(get_direction(varian_image))
    image_handle.SetOrigin(get_origin(varian_image))
    return image_handle

app = pyesapi.CustomScriptExecutable.CreateApplication('python_demo')
atexit.register(app.Dispose)
fid = open(os.path.join('.', 'PatientID'))
line = fid.readline()
line = fid.readline()
fid.close()
MRN = line.strip('\n')
app.ClosePatient()
patient = app.OpenPatientById(MRN)
plan = patient.CoursesLot(1).PlanSetupsLot(0)
image_handle = create_sitk_Image(plan.StructureSet.Image)
xxx = 1
# sitk.WriteImage(image_handle, r'K:\Image.nii.gz')