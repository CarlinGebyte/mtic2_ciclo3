from rest_framework import routers
from .api import NurseViewSet, DoctorViewSet, PatientViewSet, KindredViewSet, MedicalHistoryViewSet, AssistantViewSet, UserViewSet

router = routers.DefaultRouter()

router.register('api/nurse', NurseViewSet, 'nurse')
router.register('api/doctor', DoctorViewSet, 'doctor')
router.register('api/patient', PatientViewSet, 'patient')
router.register('api/kindred', KindredViewSet, 'kindred')
router.register('api/medical_history', MedicalHistoryViewSet, 'medical_history')
router.register('api/assistant', AssistantViewSet, 'assistant')
router.register('api/user', UserViewSet, 'user')

urlpatterns = router.urls
