from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from configApp.views import CourseApiView
from .views import course_statistics


router = DefaultRouter()
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'students', StudentViewSet)
router.register(r'department', DepartmentsApiView)
router.register(r'room', RoomAPIView)
router.register(r'day', DayAPIView)
router.register(r'group', GroupApiView)
router.register(r'tableType', TableTypeApi)
router.register(r'table', TableApi)
router.register(r'groupHome', GroupHomeWorkApi)
router.register(r'topic', TopicsApi)
router.register(r'homeWork', HomeWorkApi)
router.register(r'attendanceLevel', AttendanceLevelApi)
router.register(r'course', CourseApiView, basename='unique_course')


urlpatterns = [
    path('', include(router.urls)),
    path('userApi/', RegisterUserApi.as_view()),
    path('statistics/', course_statistics, name='course_statistics'),

    path('refresh_password/', ChangePasswordView.as_view()),
    path('sentOTP/', PhoneSendOTP.as_view()),
    path('sentOTP_and_phone/', VerifySms.as_view()),
    
    path('teacherAPI/', TeacherApiView.as_view()),
    path('workerAPI/', WorkerApiView.as_view()),
    path('workerId/<int:pk>/', WorkerApiViewId.as_view()),
    
    path('student/', StudentApiView.as_view()),
    path('student/<int:pk>/', StudentApiViewId.as_view()),
    path('group_get/', GroupApi.as_view()),
]
