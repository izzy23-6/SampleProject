from django.urls import re_path, path, include
from rest_framework.routers import DefaultRouter
# from rest_framework_jwt import views as jwt_views
from apis.views import *

router = DefaultRouter()
router.register(r'Charges', ChargesViewSet, base_name='charges')
router.register(r'chargessupply', ChargesSupplyViewSet, base_name='chargessupply')
router.register(r'patientid', IdPatientViewset, base_name='patientid')
router.register(r'patientidsearch', IdPatientSearchViewset, base_name='patientidsearch')
router.register(r'patientidattr', IdPatientAttrViewset)
router.register(r'ContractPrice', ContractPriceViewset, base_name='contractprice')
router.register(r'contractpricesearchdetail', ContractPriceSearchDetailViewset, base_name='contractpricesearchdetail')
router.register(r'Custparent', CustparentViewset, base_name='custparent')
router.register(r'User', UserViewset, basename='user')
router.register(r'employeerelation', EmployeeRelationViewset, basename='employeerelation')
router.register(r'residentbillingsummary', ResidentBillingSummaryViewset, base_name='residentbillingsummary')



