"""
Created By : Nikesh
Created On : 
Reviewed By :
Reviewed On :
Version :
"""
import os
import re

from django.conf import settings
from django.http import HttpRequest

from examsystemapp.api.base_controller import BaseController
from examsystemapp.services.base_service import BaseService
from examsystemapp.utils.constants.constants import DataTypes, HttpMethodType
from examsystemapp.utils.helpers.request_helper import ParamsObject, RequestConfig


class CodeGenerator(BaseController):

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

        if params_object.get_params_dict().get("table_name") != "" and params_object.get_params_dict().get(
                "table_name") is not None:
            table_data: list = base_service.get_direct("sGetTableDetail", params_object, False)

            for table_detail in table_data:
                table_name = table_detail.get("TABLE_NAME")
                columns = table_detail.get("Columns")
                columns_type = table_detail.get("Columns_Type")
                is_nullable = table_detail.get("Is_Nullable")
                default_value = table_detail.get("Default_Value")

                self.generate_model(table_name, columns, columns_type, is_nullable, default_value)
                self.generate_api(table_name, columns, columns_type, is_nullable, default_value)
                self.generate_service(table_name, columns, columns_type, is_nullable, default_value)
                self.generate_repo(table_name, columns, columns_type, is_nullable, default_value)
                self.generate_url_mapping(table_name, columns, columns_type, is_nullable, default_value)
                self.generate_proc(table_name, columns, columns_type, is_nullable, default_value)
                # self.generate_api_list(table_name, columns, columns_type, is_nullable, default_value)

        return self.send_response("success")

    def generate_model(self, table_name, columns, columns_type, is_nullable, default_value):
        try:
            tab_space = "        "
            template_file = open(
                os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "assets", "model_template.txt"),
                "r")
            template_r = template_file.read()
            template: str = template_r

            name = table_name.replace("t", "", 1)
            model_file_name = self.camel_case_to_snake_case(name)

            if not os.path.exists(
                    os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "models", model_file_name + ".py")):

                template = template.replace("<Class_Name>", name + "Model")
                template = template.replace("<App_Name>", self.code_root_dir_name)

                columns: list = columns.split(",")
                constructor_params = ""
                constructor_body = ""
                cnt = 1
                for column_name in columns:
                    name = column_name.lower()
                    constructor_params = constructor_params + name + "=None,"
                    if cnt == 1:
                        constructor_body = constructor_body + "self." + name + " = " + name + "\n"
                        cnt = cnt + 1
                    else:
                        constructor_body = constructor_body + tab_space + "self." + name + " = " + name + "\n"

                constructor_params = constructor_params[:-1]
                template = template.replace("<Constructor_Parameters>", constructor_params)
                template = template.replace("<Constructor_Body>", constructor_body)

                model_file = open(
                    os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "models",
                                 model_file_name + ".py"), "w+")
                model_file.write(template)
                template_file.close()
                model_file.close()
        except Exception as ex:
            print(str(ex))

    def generate_api(self, table_name, columns, columns_type, is_nullable, default_value):
        try:
            double_tab_space = "        "
            single_tab_space = "    "

            template_file = open(
                os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "assets", "api_template.txt"),
                "r")
            template_r = template_file.read()
            template: str = template_r

            name = table_name.replace("t", "", 1)
            api_file_name = self.camel_case_to_snake_case(name)
            api_class_name = name

            if not os.path.exists(
                    os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "api", api_file_name + ".py")):

                model_file_name = self.camel_case_to_snake_case(name)
                model_class_name = name + "Model"
                model_variable_name = self.camel_case_to_snake_case(name) + "_model"

                service_file_name = self.camel_case_to_snake_case(name) + "_service"
                service_class_name = name + "Service"
                service_variable_name = self.camel_case_to_snake_case(name) + "_service"

                json_name = self.camel_case_to_snake_case(name) + "_json"
                object_name = self.camel_case_to_snake_case(name) + "_object"

                template = template.replace("<App_Name>", self.code_root_dir_name)

                template = template.replace("<Model_File_Name>", model_file_name)
                template = template.replace("<Model_Class_Name>", model_class_name)

                template = template.replace("<Service_File_Name>", service_file_name)
                template = template.replace("<Service_Class_Name>", service_class_name)
                template = template.replace("<Service_Variable>", service_variable_name)

                template = template.replace("<Api_Class_Name>", api_class_name)
                template = template.replace("<Json_Name>", json_name)
                template = template.replace("<Object_Name>", object_name)

                columns: list = columns.split(",")
                json_to_model = ""
                cnt = 1
                for column_name in columns:
                    cln_name = column_name.lower()
                    if cnt == 1:
                        json_to_model = json_to_model + object_name + "." + cln_name + " = " + json_name + ".get(\"" + cln_name + "\")\n"
                        cnt = cnt + 1
                    else:
                        json_to_model = json_to_model + double_tab_space + object_name + "." + cln_name + " = " + json_name + ".get(\"" + cln_name + "\")\n"

                template = template.replace("<Json_To_Model_Data>", json_to_model)

                api_file = open(
                    os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "api", api_file_name + ".py"), "w+")
                api_file.write(template)
                template_file.close()
                api_file.close()

        except Exception as ex:
            print(str(ex))

    def generate_service(self, table_name, columns, columns_type, is_nullable, default_value):
        try:
            double_tab_space = "        "
            single_tab_space = "    "

            template_file = open(
                os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "assets", "service_template.txt"),
                "r")
            template_r = template_file.read()
            template: str = template_r

            name = table_name.replace("t", "", 1)

            service_file_name = self.camel_case_to_snake_case(name) + "_service"
            service_class_name = name + "Service"
            service_variable_name = self.camel_case_to_snake_case(name) + "_service"

            if not os.path.exists(
                    os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "services",
                                 service_file_name + ".py")):
                model_file_name = self.camel_case_to_snake_case(name)
                model_class_name = name + "Model"
                model_variable_name = self.camel_case_to_snake_case(name) + "_model"

                repo_file_name = self.camel_case_to_snake_case(name) + "_repository"
                repo_class_name = name + "Repo"
                repo_variable_name = self.camel_case_to_snake_case(name) + "_repo"

                template = template.replace("<App_Name>", self.code_root_dir_name)

                template = template.replace("<Repo_File_Name>", repo_file_name)
                template = template.replace("<Repo_Class_Name>", repo_class_name)
                template = template.replace("<Repo_Variable>", repo_variable_name)

                template = template.replace("<Model_File_Name>", model_file_name)
                template = template.replace("<Model_Class_Name>", model_class_name)

                template = template.replace("<Service_File_Name>", service_file_name)
                template = template.replace("<Service_Class_Name>", service_class_name)
                template = template.replace("<Service_Variable>", service_variable_name)

                service_file = open(
                    os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "services", service_file_name + ".py"),
                    "w+")
                service_file.write(template)
                template_file.close()
                service_file.close()

        except Exception as ex:
            print(str(ex))

    def generate_repo(self, table_name, columns, columns_type, is_nullable, default_value):
        try:
            double_tab_space = "        "
            single_tab_space = "    "

            template_file = open(
                os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "assets", "repo_template.txt"),
                "r")
            template_r = template_file.read()
            template: str = template_r

            name = table_name.replace("t", "", 1)

            repo_file_name = self.camel_case_to_snake_case(name) + "_repository"
            repo_class_name = name + "Repo"
            repo_variable_name = self.camel_case_to_snake_case(name) + "_repo"

            if not os.path.exists(
                    os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "repository", repo_file_name + ".py")):

                model_file_name = self.camel_case_to_snake_case(name)
                model_class_name = name + "Model"
                model_variable_name = self.camel_case_to_snake_case(name) + "_model"

                object_name = name

                template = template.replace("<App_Name>", self.code_root_dir_name)

                template = template.replace("<Repo_File_Name>", repo_file_name)
                template = template.replace("<Repo_Class_Name>", repo_class_name)
                template = template.replace("<Repo_Variable>", repo_variable_name)

                template = template.replace("<Object_Name>", object_name)

                template = template.replace("<Model_File_Name>", model_file_name)
                template = template.replace("<Model_Class_Name>", model_class_name)
                template = template.replace("<Model_Variable_Name>", model_variable_name)

                columns: list = columns.split(",")
                post_get_data = ""
                proc_params = ""
                cnt = 1
                for column_name in columns:
                    cln_name = column_name.lower()
                    proc_params = proc_params + "object." + cln_name + ","
                    if cnt == 1:
                        post_get_data = post_get_data + model_variable_name + "." + cln_name + " = " + "each_tuple[" + str(
                            cnt - 1) + "]\n"
                    else:
                        post_get_data = post_get_data + double_tab_space + double_tab_space + model_variable_name + "." + cln_name + " = " + "each_tuple[" + str(
                            cnt - 1) + "]\n"
                    cnt = cnt + 1

                proc_params = proc_params[:-1]
                template = template.replace("<Proc_Params>", proc_params)
                template = template.replace("<Post_Get_Data>", post_get_data)

                repo_file = open(
                    os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "repository", repo_file_name + ".py"),
                    "w+")
                repo_file.write(template)
                template_file.close()
                repo_file.close()

        except Exception as ex:
            print(str(ex))

    def generate_url_mapping(self, table_name, columns, columns_type, is_nullable, default_value):
        global url_file
        try:
            double_tab_space = "        "
            single_tab_space = "    "

            template_file = open(
                os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "assets", "url_mapping_template.txt"),
                "r")
            template_r = template_file.read()
            template: str = template_r

            name = table_name.replace("t", "", 1)

            url_mapping_file_name = self.camel_case_to_snake_case(name) + "_mapping"

            if not os.path.exists(
                    os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "urls", "url_mapping",
                                 url_mapping_file_name + ".py")):
                api_file_name = name.lower()
                api_file_name = self.camel_case_to_snake_case(name)
                api_class_name = name

                template = template.replace("<App_Name>", self.code_root_dir_name)
                template = template.replace("<Api_File_Name>", api_file_name)
                template = template.replace("<Api_Class_Name>", api_class_name)

                url_mapping_file = open(
                    os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "urls", "url_mapping",
                                 url_mapping_file_name + ".py"),
                    "w+")
                url_mapping_file.write(template)
                template_file.close()
                url_mapping_file.close()

            # URL
            url_template_file = open(
                os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "assets", "url_template.txt"),
                "r")
            url_template_r = url_template_file.read()
            url_template: str = url_template_r

            url_template = url_template.replace("<Url_Mapping_File_Name>", url_mapping_file_name)
            if not os.path.exists(os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "urls",
                                               self.camel_case_to_snake_case(name) + ".py")):
                url_file = open(
                    os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "urls",
                                 self.camel_case_to_snake_case(name) + ".py"), "w+")
                url_file.write(url_template)
                url_template_file.close()
                url_file.close()

        except Exception as ex:
            print(str(ex))

    def generate_proc(self, table_name, columns, columns_type, is_nullable, default_value):
        try:
            template_file = open(
                os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "assets", "procedures.txt"),
                "r")
            template_r = template_file.read()
            template: str = template_r
            name = table_name.replace("t", "", 1)
            proc_file_name = self.camel_case_to_snake_case(name)
            template = template.replace('<Table_Name>', name)
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
                    update_columns_detail += columns[i] + ' = P' + columns[i] + ', '

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

    def generate_api_list(self, table_name, columns, columns_type, is_nullable, default_value):
        double_tab_space = "        "
        try:
            template_file = open(
                os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "assets", "api_list_template.txt"),
                "r")
            template_r = template_file.read()
            template: str = template_r

            name = table_name.replace("t", "", 1)
            api_list_file_name = self.camel_case_to_snake_case(name)
            json_name = self.camel_case_to_snake_case(name) + "_json"

            if not os.path.exists(
                    os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "api", api_list_file_name + ".txt")):
                list_of_columns = columns.split(',')
                list_of_columns = [double_tab_space + i.lower() + ':' for i in list_of_columns]
                key_list = '\n'.join(list_of_columns)
                template = template.replace('<table-name>', name.lower())
                template = template.replace('<keylist>', key_list)
                template = template.replace('<Json_Name>', json_name)
                api_list_file = open(
                    os.path.join(settings.PROJECT_ROOT, self.code_root_dir_name, "api-list",
                                 api_list_file_name + ".txt"), "w+")
                api_list_file.write(template)
                template_file.close()
                api_list_file.close()
        except Exception as ex:
            print(str(ex))
