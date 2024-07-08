from django.urls import path
from . import views

urlpatterns = [
  path('place/', views.place_borrowing, name = 'place-borrowing'),
  path('report/', views.BorrowingReportView.as_view(), name = 'borrowing-report'),
  path('return/<int:borrow_id>/', views.ReturnBorrowedBookView.as_view(), name = 'return-book'),
]
