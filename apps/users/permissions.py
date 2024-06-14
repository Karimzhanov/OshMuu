from rest_framework import permissions
from apps.users.models import User, Employee

class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            user_employee = request.user.user_employee
            return user_employee.employee_position == Employee.EmployeePositionChoice.TEACHER
        except Exception as e:
            return False

    def has_object_permission(self, request, view, obj):
        try:
            user_employee = request.user.user_employee
            return user_employee.employee_position == Employee.EmployeePositionChoice.TEACHER
        except Exception as e:
            return False

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            user_employee = request.user.user_employee
            return user_employee.employee_position == Employee.EmployeePositionChoice.STUDENT
        except Exception as e:
            return False

    def has_object_permission(self, request, view, obj):
        try:
            user_employee = request.user.user_employee
            return user_employee.employee_position == Employee.EmployeePositionChoice.STUDENT
        except Exception as e:
            return False
