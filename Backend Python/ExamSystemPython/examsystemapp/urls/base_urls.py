from django.urls import path, include

urlpatterns = [
    path('code-gen/', include('examsystemapp.urls.code_gen')),
    path('bssubject/', include('examsystemapp.urls.bs_subject_hdr')),
    path('branch/', include('examsystemapp.urls.branch')),
    path('state/', include('examsystemapp.urls.state')),
    path('city/', include('examsystemapp.urls.city')),
    path('college/', include('examsystemapp.urls.college')),
    path('college-branch/', include('examsystemapp.urls.college_branch')),
    path('semester/', include('examsystemapp.urls.semester')),
    path('staff/', include('examsystemapp.urls.staff')),
    path('student/', include('examsystemapp.urls.student')),
    path('student-ay/', include('examsystemapp.urls.student_ay')),
    path('university/', include('examsystemapp.urls.university')),
    path('university-ay/', include('examsystemapp.urls.university_ay')),
    path('subject/', include('examsystemapp.urls.subject')),
    path('menu/', include('examsystemapp.urls.category')),
    path('product/', include('examsystemapp.urls.product')),
    path('cart/', include('examsystemapp.urls.cart')),
    path('order/', include('examsystemapp.urls.order')),
    path('customer/', include('examsystemapp.urls.customer')),
    path('customer_address/', include('examsystemapp.urls.customer_address')),

]
