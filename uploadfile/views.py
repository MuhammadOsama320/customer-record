import datetime
import pandas as pd
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .models import Customer
from uploadfile.models import Customer


# Create your views here.


class UploadFileView(TemplateView):
    template_name = 'upload.html'

    def get_context_data(self, **kwargs):
        return kwargs

    def post(self, request, *args, **kwargs):
        file1 = request.FILES['upload']
        print(file1)
        read_file = pd.read_csv(file1)
        json_data = read_file.to_json()
        Customer.objects.all().delete()
        for row in read_file.to_dict(orient='records'):
            Customer.objects.update_or_create(
                consignee_name=row.get("Consignee Name") if row.get("Consignee Name") != 'nan' else '',
                pickup_address_id=row.get("Pickup Address ID") if row.get("Pickup Address ID") != 'nan' else '',
                show_information_on_air_waybill=row.get("Show Information on Air Waybill") if row.get(
                    "Show Information on Air Waybill") != 'nan' else '',
                consignee_city_name=row.get("Consignee City Name") if row.get("Consignee City Name") != 'nan' else '',
                consignee_address=row.get("Consignee Address") if row.get("Consignee Address") != 'nan' else '',
                consignee_phone_number_1=row.get("Consignee Phone Number 1 (03000000000)") if row.get(
                    "Consignee Phone Number 1 (03000000000)") != 'nan' else '',
                consignee_phone_number_2=row.get("Consignee Phone Number 2 (03000000000)") if str(
                    row.get("Consignee Phone Number 2 (03000000000)")) != 'nan' else '',
                consignee_email_address=row.get("Consignee Email Address") if str(
                    row.get("Consignee Email Address")) != 'nan' else '',
                self_collection=row.get("Self Collection") if row.get("Self Collection") != 'nan' else '',
                order_id=row.get("Order ID") if row.get("Order ID") != 'nan' else '',
                order_date=datetime.datetime.strptime(row.get("Order Date (YYYY-MM-DD)"), '%d/%m/%Y') if row.get(
                    "Order Date (YYYY-MM-DD)") != 'nan' else '',
                item_product_type_id=row.get("Item Product Type ID") if row.get(
                    "Item Product Type ID") != 'nan' else '',
                item_description=row.get("Item Description") if row.get("Item Description") != 'nan' else '',
                item_quantity=str(row.get("Item Quantity")) if str(row.get("Item Quantity")) != 'nan' else '',
                item_insurance=row.get("Item Insurance") if row.get("Item Insurance") != 'nan' else '',
                product_value=row.get("Product Value") if row.get("Product Value") != 'nan' else '',
                special_instructions=row.get("Special Instructions") if row.get(
                    "Special Instructions") != 'nan' else '',
                estimated_weight=row.get("Estimated Weight (kg)") if row.get("Estimated Weight (kg)") != 'nan' else '',
                mode_of_shipment_id=row.get("Mode of Shipment ID") if row.get("Mode of Shipment ID") != 'nan' else '',
                same_day_timing_id=row.get("Same Day Timing ID") if str(row.get("Same Day Timing ID")) != 'nan' else '',
                collection_amount=row.get("Collection Amount") if row.get("Collection Amount") != 'nan' else '',
                mode_of_payment_id=row.get("Mode of Payment ID") if row.get("Mode of Payment ID") != 'nan' else '',
                charges_mode_id=row.get("Charges Mode ID") if row.get("Charges Mode ID") != 'nan' else '',
                pieces=row.get("Pieces") if row.get("Pieces") else '',
                shipper_reference_number_1=row.get("Shipper Reference Number 1") if str(
                    row.get("Shipper Reference Number 1")) != 'nan' else '',
                shipper_reference_number_2=row.get("Shipper Reference Number 2") if str(
                    row.get("Shipper Reference Number 2")) != 'nan' else '',
                shipper_reference_number_3=row.get("Shipper Reference Number 3") != 'nan' if str(
                    row.get("Shipper Reference Number 3")) else '',
                shipper_reference_number_4=row.get("Shipper Reference Number 4") if str(
                    row.get("Shipper Reference Number 4")) != 'nan' else '',
                shipper_reference_number_5=row.get("Shipper Reference Number 5") if str(
                    row.get("Shipper Reference Number 5")) != 'nan' else ''),

        return redirect(reverse('data'))


class DataView(TemplateView):
    template_name = 'data.html'

    def get_context_data(self, **kwargs):
        kwargs['customers'] = Customer.objects.all()
        return kwargs
