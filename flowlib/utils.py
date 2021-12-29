# -*- coding: utf-8 -*-
import uuid

def resolve_uuids_in_processor_properties(processor_properties: dict, controller_services: dict) -> dict:
    for property in processor_properties:
        value = processor_properties[property]
        if is_valid_uuid(value):
            found_service = next((service for service in controller_services['controller_services'] if service["config"]["id"] == value), None)
            if found_service is not None:
                processor_properties[property] = "{{ controller('" + found_service["name"] + "') }}"

    return processor_properties

def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


