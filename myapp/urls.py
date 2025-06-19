from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('register/', views.register, name='register'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_record, name='add_record'),
    path('delete/<int:pk>/', views.delete_record, name='delete_record'),
    path('export/', views.export_csv, name='export_csv'),
    path('next/', views.next, name='next'),
    path('add2/', views.add_record2, name='add_record2'),
    path('delete2/<int:pk>/', views.delete_record2, name='delete_record2'),
    path('export2/', views.export_csv2, name='export_csv2'),
    path('next2/', views.next2, name='next2'),
    path('add3/', views.add_record3, name='add_record3'),
    path('delete3/<int:pk>/', views.delete_record3, name='delete_record3'),
    path('export3/', views.export_csv3, name='export_csv3'),
    path('next3/', views.next3, name='next3'),
    path('add4/', views.add_record4, name='add_record4'),
    path('delete4/<int:pk>/', views.delete_record4, name='delete_record4'),
    path('export4/', views.export_csv4, name='export_csv4'),
    path('aggregate/', views.aggregate_marks, name='aggregate_marks'),
    path('export_aggregate/', views.export_aggregate_csv, name='export_aggregate_csv'),  # New URL pattern for exporting aggregated marks
    path('export_aggregate_pdf/', views.export_aggregate_pdf, name='export_aggregate_pdf'),
]