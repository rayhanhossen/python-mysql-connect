import json
from database.client import MySQLClient
from database.mysql_db import DatabaseOperation


def main():
    client = MySQLClient().connect()
    db_operation = DatabaseOperation(client)
    otf_commission_data = db_operation.select_data_from_table(
        "select * from PMT_DV_OTF_COMMISSION_CONFIGURATION_PROFILE")

    data_list = list()
    for otf_commission in otf_commission_data:
        data = {
            'ID': otf_commission[0],
            'BRAND': otf_commission[1],
            'NETWORK_NAME': otf_commission[2],
            'DOMAIN': otf_commission[3],
            'CATEGORY': otf_commission[4],
            'GEOGRAPHICAL_DOMAIN': otf_commission[5],
            'GRADE': otf_commission[6],
            'COMMISSION_PROFILE_SET': otf_commission[7],
        }
        data_list.append(data)
    print(json.dumps(data_list, indent=2))


if __name__ == '__main__':
    main()
