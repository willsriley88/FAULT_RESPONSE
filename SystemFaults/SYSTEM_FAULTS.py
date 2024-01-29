import requests
import json


class DBFaultResponse:
    response = {
        "CELL_NAME": "",
        "SYSTEM_NAME": "",
        "FAULT": ""
    }


class SystemFaults:
    def __init__(self, system_name="", cell_name="", fault_url=""):
        self.system_name = system_name
        self.cell_name = cell_name
        self.fault_url = fault_url
        self.fault_response = DBFaultResponse()
        self.fault_response.response["CELL_NAME"] = self.cell_name
        self.fault_response.response["SYSTEM_NAME"] = self.system_name

    def update_response(self, fault):
        try:
            self.fault_response.response["FAULT"] = fault
            requests.post(url=self.fault_url, json=self.fault_response.response)
        except Exception as e:
            return None
