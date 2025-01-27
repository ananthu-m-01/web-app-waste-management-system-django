"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from WasteManagementSystem import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.log),
    path('login_post', views.login_post),
    path('logout', views.logout),
    path('admin_home', views.admin_home),
    path('add_material_post', views.add_material_post),
    path('update_material/<id>', views.update_material),
    path('update_material_POST/<id>', views.update_material_POST),
    path('delete_material/<id>', views.delete_material),
    path('view_material', views.view_material),
    path('add_krishibhavan', views.add_krishibhavan),
    path('add_krishibhavan_post', views.add_krishibhavan_post),
    path('update_krishibhavan/<id>', views.update_krishibhavan),
    path('update_krishibhavan_post/<id>', views.update_krishibhavan_post),
    path('delete_krishibhavan/<id>', views.delete_krishibhavan),
    path('view_krishibhavan', views.view_krishibhavan),
    path('add_area', views.add_area),
    path('add_area_post', views.add_area_post),
    path('update_area/<id>', views.update_area),
    path('update_area_post/<id>', views.update_area_post),
    path('delete_area/<id>', views.delete_area),
    path('view_area', views.view_area),
    path('add_pickupVehicle', views.add_pickupVehicle),
    path('add_pickupVehicle_post', views.add_pickupVehicle_post),
    path('update_pickupVehicle/<id>', views.update_pickupVehicle),
    path('update_pickupVehicle_post/<id>', views.update_pickupVehicle_post),
    path('delete_pickupVehicle/<id>', views.delete_pickupVehicle),
    path('view_pickupVehicle', views.view_pickupVehicle),
    path('view_registeredUser', views.view_registeredUser),
    path('view_pickupReports', views.view_pickupReports),
    path('view_payment', views.view_payment),
    path('add_notification', views.add_notification),
    path('add_notification_post', views.add_notification_post),
    path('update_notification/<id>', views.update_notification),
    path('update_notification_post/<id>', views.update_notification_post),
    path('delete_notification/<id>', views.delete_notification),
    path('view_notification', views.view_notification),
    path('view_complaint', views.view_complaint),
    path('send_reply/<id>', views.send_reply),
    path('send_reply_post/<id>', views.send_reply_post),
    path('view_feedback', views.view_feedback),
    path('area_allocate/<id>', views.area_allocate),
    path('area_allocate_post/<id>', views.area_allocate_post),
    path('view_allocated_area', views.view_allocated_area),
    path('delete_allocated_area/<id>', views.delete_allocated_area),
    path('change_password', views.change_password),
    path('change_password_post', views.change_password_post),
    path('pickup_vehicle_home', views.pickup_vehicle_home),
    path('allocated_area_pickup', views.allocated_area_pickup),
    path('view_wasteDetails_pickup', views.view_wasteDetails_pickup),
    path('set_collection_date/<id>', views.set_collection_date),
    path('add_wasteEntry/<id>/<uid>', views.add_wasteEntry),
    path('add_waste_Entry_post', views.add_waste_Entry_post),
    path('view_wasteEntry', views.view_wasteEntry),
    path('view_cashEntry', views.view_cashEntry),
    path('view_notification_Pickup', views.view_notification_Pickup),
    path('change_password_pickup', views.change_password_pickup),
    path('change_password_pickup_post', views.change_password_pickup_post),
    path('set_collection_date_post/<id>', views.set_collection_date_post),
    path('todayCollection', views.todayCollection),
    path('KrishibhavanHome', views.KrishibhavanHome),
    path('ViewProfile', views.ViewProfile),
    path('AddMaterial', views.AddMaterial),
    path('ViewMaterial', views.ViewMaterial),
    path('ViewMaterilOrder', views.ViewMaterilOrder),
    path('ViewVegetablesOfUsers', views.ViewVegetablesOfUsers),
    path('ViewRequestStatus', views.ViewRequestStatus),
    path('ViewVegetableStock', views.ViewVegetableStock),
    path('ViewVegetableOrders', views.ViewVegetableOrders),
    path('ViewNotification', views.ViewNotification),
    path('changePassword', views.changePassword),
    path('sendCollectionRequest/<id>', views.sendCollectionRequest),
    path('changePassword_POST_KR', views.changePassword_POST_KR),
    path('sendCollectionRequestPOST', views.sendCollectionRequestPOST),
    path('ViewVegetableItems/<id>', views.ViewVegetableItems),
    path('ViewMaterilOrderItems/<id>', views.ViewMaterilOrderItems),
    path('todayApprovedRequest', views.todayApprovedRequest),
    path('deleteRequest/<id>', views.deleteRequest),
    path('updateVegetableStock/<id>/<q>/<p>', views.updateVegetableStock),
    path('updatevegetableStockPOST/<id>', views.updatevegetableStockPOST),
    path('ViewVegetablesOfUsersPOST', views.ViewVegetablesOfUsersPOST),
    path('and_login', views.and_login),
    path('and_add_vegetable', views.and_add_vegetable),
    path('and_add_waste', views.and_add_waste),
    path('and_change_password', views.and_change_password),
    path('and_register', views.and_register),
    path('and_send_complaint', views.and_send_complaint),
    path('and_send_feedback', views.and_send_feedback),
    path('and_viewApprovedRequest', views.and_viewApprovedRequest),
    path('and_viewCollectionRequest', views.and_viewCollectionRequest),
    path('and_viewMaterial', views.and_viewMaterial),
    path('and_viewReply', views.and_viewReply),
    path('and_viewVegetable', views.and_viewVegetable),
    path('and_viewWaste', views.and_viewWaste),
    path('and_viewProfile', views.and_viewProfile),
    path('and_editProfile', views.and_editProfile),
    path('and_vegetableOrder', views.and_vegetableOrder),
    path('and_materialOrder', views.and_materialOrder),
    path('and_viewVegetableOrder', views.and_viewVegetableOrder),
    path('and_viewMaterialOrder', views.and_viewMaterialOrder),
    path('and_approveCollectionRequest', views.and_approveCollectionRequest),
    path('and_rejectCollectionRequest', views.and_rejectCollectionRequest),
    path('and_cancelWaste', views.and_cancelWaste),
    path('and_viewCollectedWaste', views.and_viewCollectedWaste),
    path('view_supercoins', views.view_supercoins),
    path('and_waste_payment', views.and_waste_payment),
    path('claim_amount', views.claim_amount),
    path('wastePayment', views.wastePayment),
    path('wasteP_entry1', views.wasteP_entry1),
    path('finish_payment', views.finish_payment),
]
