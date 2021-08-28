import os
import re

from django.conf import settings
from django.http import HttpRequest

from examsystemapp.api.base_controller import BaseController
from examsystemapp.services.base_service import BaseService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType
from examsystemapp.utils.helpers.request_helper import ParamsObject, RequestConfig


class ProcedureGenerator(BaseController):

    def __init__(self, request: HttpRequest):
        BaseController.__init__(self, request)
        self.code_root_dir_name = "examsystemapp"

    @staticmethod
    def camel_case_to_snake_case(name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def check_session(self, request):
        pass

    def generate_code(self, request: HttpRequest):
        base_service: BaseService = BaseService()

        params_config = [
            {"table_name": RequestConfig(from_session=False, nullable=True, default="",
                                         datatype=DataTypes.STRING)}
        ]
        params_object: ParamsObject = self.convert_params(request, HttpMethodType.get, params_config)

        table_data: list = base_service.get_direct("sGetTableDetail", params_object, False)
        for table_detail in table_data:
            table_name = table_detail.get("TABLE_NAME")
            columns = table_detail.get("Columns")
            columns_type = table_detail.get("Columns_Type")

            self.generate_proc(table_name, columns, columns_type)
        return self.send_response("success")

    def generate_proc(self, table_name, columns, columns_type):
        try:
            template_file = open(
                os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "assets", "procedures.txt"),
                "r")
            template_r = template_file.read()
            template: str = template_r
            name = table_name.replace("t", "", 1)
            proc_file_name = self.camel_case_to_snake_case(name)
            template = template.replace('<Table_Name>',name)
            if not os.path.exists(
                    os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "sql", "master", "procedures",
                                 proc_file_name
                                + ".sql")):

                template = template.replace("< Table_Name >", name)
                columns: list = columns.split(",")
                columns_type: list = columns_type.split(",")
                input_procedure_col_detail = ''
                input_column_list = ''
                update_columns_detail = ''
                input_column_list_as_values = ''
                for i in range(len(columns)):
                    if columns_type[i] == 'datetime':
                        input_procedure_col_detail += "IN P" + columns[i] + ' ' + 'varchar(24)' + ', '
                    else:
                        input_procedure_col_detail += "IN P" + columns[i] + ' ' + columns_type[i] + ', '

                    input_column_list += columns[i] + ', '
                    input_column_list_as_values += 'P' + columns[i] + ', '
                    update_columns_detail += columns[i] + ' = P' + columns[i]+', '

                input_procedure_col_detail = input_procedure_col_detail.rstrip(', ')
                template = template.replace('<input_procedure_column_detail>', input_procedure_col_detail)

                update_columns_detail = update_columns_detail.rstrip(', ')
                template = template.replace('<Update_columns_detail>', update_columns_detail)

                input_column_list = input_column_list.rstrip(', ')
                template = template.replace('<input_column_list>', input_column_list)

                input_column_list_as_values = input_column_list_as_values.rstrip(', ')
                template = template.replace('<input_column_list_as_values>', input_column_list_as_values)

                template = template.replace('datetime', 'varchar(24)')



                proc_file_name = open(
                    os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "sql", "master", "procedures",
                                proc_file_name + ".sql"), "w+")
                proc_file_name.write(template)
                template_file.close()
                proc_file_name.close()
        except Exception as ex:
            print(str(ex))


