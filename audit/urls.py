from django.urls import path
from . import views
urlpatterns = [
	path('', views.AuditListView.as_view(),name='audits'),
	path('<int:pk>/',views.AuditDetailView.as_view(),name='rules'),
	path('<int:audit_pk>/<int:pk>/',views.RuleDetailView.as_view(),name='numerals'),
	path('<int:audit_pk>/<int:rule_pk>/<int:pk>/',views.NumeralDetailView.as_view(),name='questions'),
		
]