#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

import logging
# Importing models and REST client class from Community Edition version
from tb_rest_client.rest_client_ce import *
from tb_rest_client.rest import ApiException


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# ThingsBoard REST API URL
url = "http://192.168.11.22:8080"

# Default Tenant Administrator credentials
# username = "tenant@thingsboard.org"
username = "customer@thingsboard.org"
password = "customer"


# Creating the REST client object with context manager to get auto token refresh
with RestClientCE(base_url=url) as rest_client:
    try:
        # Auth with credentials
        rest_client.login(username=username, password=password)

        user = rest_client.get_user()
        logging.info("User: ", user.customer_id)

        # Creating an Asset
        farm_asset = Asset(name="Farm 2", type="farm", customer_id=user.customer_id)
        logging.info("Asset: ", farm_asset)
        farm_asset = rest_client.save_asset(farm_asset)

        pond_asset = Asset(name="Pond 2", type="pond", customer_id=user.customer_id)
        logging.info("Asset: ", pond_asset)
        pond_asset = rest_client.save_asset(pond_asset)

        farm_pond_relation = EntityRelation(_from=farm_asset.id, to=pond_asset.id, type="Contains")
        rest_client.save_relation(farm_pond_relation)

        # logging.info("Asset was created:\n%r\n", asset)
        device_profile_id = list(filter(lambda x: x.type == 'DEFAULT', rest_client.get_device_profiles(10, 0).data))[0]
        logging.info("Device profile :\n%r\n", device_profile_id)

        # creating a Device
        device = Device(name="Thermometer 4", type="thermometer", customer_id=user.customer_id, device_profile_id=device_profile_id.id)
        device = rest_client.save_device(device)
        logging.info(" Device was created:\n%r\n", device)

        pond_device_relation = EntityRelation(_from=pond_asset.id, to=device.id, type="Contains")
        rest_client.save_relation(pond_device_relation)

        # Creating relations from device to asset
        # relation = EntityRelation(_from=asset.id, to=device.id, type="Contains")
        # relation = rest_client.save_relation(relation)

        # logging.info(" Relation was created:\n%r\n", relation)
    except ApiException as e:
        logging.exception(e)

