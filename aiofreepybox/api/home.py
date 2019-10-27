_DEFAULT_CAMERA_INDEX = 0
_DEFAULT_CHANNEL = 2
_DEFAULT_SIZE = 4
_DEFAULT_QUALITY = 5


class Home:
    """
    Home

    Freebox home data structure : adapter > node > endpoint
    """

    def __init__(self, access):
        self._access = access

    create_home_node_rule_payload_schema = {
        "icon_url": "",
        "id": 0,
        "label": "",
        "name": "",
        "role": 0,
        "role_label": "",
        "type": "",
    }
    node_rule_role_schema = {"node": [0], "role": 0}
    node_rule_configuration_data_schema = {"roles": [node_rule_role_schema]}
    next_pairing_step_payload_schema = {"session": 0, "pageid": 0, "fields": [None]}
    sms_number_data_schema = {
        "description": "Mon numero",
        "phone_number": "",
        "sms_enabled": True,
        "voicemail_enabled": True,
    }
    sms_validation_data_schema = {"application_hash": ""}
    sms_number_validation_data_schema = {"validation_code": ""}
    start_pairing_step_payload_schema = {"nfc": True, "qrcode": False, "type": ""}
    stop_pairing_step_payload_schema = {"session": 0}

    async def create_sms_number(self, sms_number_data):
        """
        Create sms number

        sms_number_data : `dict`
        """
        return await self._access.post("home/sms/numbers", sms_number_data)

    async def del_home_adapter(self, home_adapter_id):
        """
        Delete home adapter

        home_adapter_id : `int`
        """
        return await self._access.delete(f"home/adapters/{home_adapter_id}")

    async def del_home_link(self, link_id):
        """
        Delete home link

        link_id : `int`
        """
        return await self._access.delete(f"home/links/{link_id}")

    async def del_home_node(self, node_id):
        """
        Delete home node id

        node_id : `int`
        """
        return await self._access.delete(f"home/nodes/{node_id}")

    async def edit_sms_number(self, sms_number_id, sms_number_data):
        """
        Edit sms number

        sms_number_id : `int`
        sms_number_data : `dict`
        """
        return await self._access.put(
            f"home/sms/numbers/{sms_number_id}", sms_number_data
        )

    async def get_camera(self):
        """
        Get camera info
        """
        return await self._access.get("camera")

    async def get_camera_configuration(self):
        """
        Get camera configuration
        """
        return await self._access.get("camera/config")

    async def get_camera_records(self, camera_id):
        """
        Get camera records

        camera_id : `int`
        """
        return await self._access.get(f"camera/{camera_id}/records")

    async def get_camera_snapshot(
        self,
        camera_index=_DEFAULT_CAMERA_INDEX,
        size=_DEFAULT_SIZE,
        quality=_DEFAULT_QUALITY,
    ):
        """
        Get camera snapshot

        camera_index : `int`
            , Default to _DEFAULT_CAMERA_INDEX
        size : 2 = 320x240, 3 = 640x480, 4 = 1280x720
            , Default to _DEFAULT_SIZE
        quality : quality index
            , Default to _DEFAULT_QUALITY
        """

        fbx_cameras = await self.get_camera()
        return await self._access.get(
            fbx_cameras[camera_index]["stream_url"].replace(
                "stream.m3u8", f"snapshot.cgi?size={size}&quality={quality}"
            )[1:]
        )

    async def get_camera_stream_m3u8(
        self, camera_index=_DEFAULT_CAMERA_INDEX, channel=_DEFAULT_CHANNEL
    ):
        """
        Get camera stream

        camera_index : `int`
            , Default to _DEFAULT_CAMERA_INDEX
        channel : 1 is SD, 2 is HD
            , Default to _DEFAULT_CHANNEL
        """

        fbx_cameras = await self.get_camera()
        return await self._access.get(
            fbx_cameras[camera_index]["stream_url"].replace(
                "stream.m3u8", f"stream.m3u8?channel={channel}"
            )[1:]
        )

    async def get_camera_ts(self, ts_name, camera_index=_DEFAULT_CAMERA_INDEX):
        """
        Get camera stream

        ts_name : `str`
        camera_index : `int`
            , Default to _DEFAULT_CAMERA_INDEX
        """

        fbx_cameras = await self.get_camera()
        return await self._access.get(
            fbx_cameras[camera_index]["stream_url"].replace(
                "stream.m3u8", f"{ts_name}"
            )[1:]
        )

    async def get_home_adapter(self, home_adapter_id):
        """
        Retrieve a registered home adapter

        home_adapter_id : `int`
        """
        return await self._access.get(f"home/adapters/{home_adapter_id}")

    async def get_home_adapters(self):
        """
        Retrieve the list of registered home adapters
        """
        return await self._access.get("home/adapters")

    async def get_home_endpoint_value(self, node_id, endpoint_id):
        """
        Get home endpoint value

        node_id : `int`
        endpoint_id : `int`
        """
        return await self._access.get(f"home/endpoints/{node_id}/{endpoint_id}")

    async def get_home_endpoint_values(self, endpoint_list):
        """
        Get home endpoint values

        endpoint_list : `[endpoint_id]`
        """
        return await self._access.post("home/endpoints/get", endpoint_list)

    async def get_home_link(self, link_id):
        """
        Get home link

        link_id : `int`
        """
        return await self._access.get(f"home/links/{link_id}")

    async def get_home_links(self):
        """
        Get home links
        """
        return await self._access.get("home/links")

    async def get_home_node(self, node_id):
        """
        Get home node id

        node_id : `int`
        """
        return await self._access.get(f"home/nodes/{node_id}")

    async def edit_home_node(self, node_id, node_data):
        """
        Edit home node data

        node_id : `int`
        node_data : `dict`
        """
        return await self._access.put(f"home/nodes/{node_id}", node_data)

    async def get_home_nodes(self):
        """
        Get home nodes
        """
        return await self._access.get("home/nodes")

    async def create_home_node_rule(self, template_name, create_home_node_rule_payload):
        """
        Create home node rule

        template_name : `str`
        create_home_node_rule_payload : `dict`
        """
        return await self._access.post(
            f"home/rules/{template_name}", create_home_node_rule_payload
        )

    async def get_home_node_existing_rule_config(self, node_id, rule_node_id, role_id):
        """
        Get home node existing rule configuration data

        node_id : `int`
        rule_node_id : `int`
        role_id : `int`
        """
        return await self._access.get(
            f"home/nodes/{node_id}/rules/node/{rule_node_id}/{role_id}"
        )

    async def get_home_node_new_rules(self, node_id):
        """
        Get node new rules

        node_id : `int`
        """
        return await self._access.get(f"home/nodes/{node_id}/rules")

    async def get_home_node_template_rule_config(self, node_id, template_name, role_id):
        """
        Get node rule template configuration data

        node_id : `int`
        template_name : `str`
        role_id : `int`
        """
        return await self._access.get(
            f"home/nodes/{node_id}/rules/template/{template_name}/{role_id}"
        )

    async def get_home_pairing_state(self, home_adapter_id):
        """
        Get the current home pairing state

        home_adapter_id : `int`
        """
        return await self._access.get(f"home/pairing/{home_adapter_id}")

    async def get_home_tile(self, tile_id):
        """
        Get the home tile with provided id

        tile_id : `int`
        """
        return await self._access.get(f"home/tileset/{tile_id}")

    async def get_home_tilesets(self):
        """
        Get the list of home tileset
        """
        return await self._access.get("home/tileset/all")

    async def get_secmod(self):
        """
        Get security module
        """
        return await self._access.get("home/secmod")

    async def get_sms_numbers(self):
        """
        Get sms numbers
        """
        return await self._access.get("home/sms/numbers")

    async def next_home_pairing_step(self, home_adapter_id, next_p_s_payload):
        """
        Next home pairing step

        home_adapter_id : `int`
        next_p_s_payload : `dict`
        """
        return await self._access.post(
            f"home/pairing/{home_adapter_id}", next_p_s_payload
        )

    async def send_sms_number_validation(self, sms_number_id, sms_validation_data):
        """
        Send sms number validation

        sms_number_id : `int`
        sms_validation_data : `dict`
        """
        return await self._access.post(
            f"home/sms/numbers/{sms_number_id}/send_validation_sms", sms_validation_data
        )

    async def set_camera_configuration(self, camera_configuration):
        """
        Set camera configuration

        camera_configuration : `dict`
        """
        await self._access.put("camera/config", camera_configuration)

    async def set_home_endpoint_value(self, node_id, e_id, home_e_v_data):
        """
        Set home endpoint value

        node_id : `int`
        e_id : `int`
        home_e_v_data : dict`
        """
        return await self._access.put(f"home/endpoints/{node_id}/{e_id}", home_e_v_data)

    async def set_home_node_rule_config(self, rule_node_id, node_r_c_data):
        """
        Set node rule configuration data

        rule_node_id : `int`
        node_r_c_data : `dict`
        """
        return await self._access.put(f"home/rules/{rule_node_id}", node_r_c_data)

    async def start_home_pairing_step(self, home_adapter_id, start_p_s_payload):
        """
        Start home pairing step

        home_adapter_id : `int`
        start_p_s_payload : `dict`
        """
        return await self._access.post(
            f"home/pairing/{home_adapter_id}", start_p_s_payload
        )

    async def stop_home_pairing_step(self, home_adapter_id, stop_p_s_payload):
        """
        Stop home pairing

        home_adapter_id : `int`
        stop_p_s_payload : `dict`
        """
        return await self._access.post(
            f"home/pairing/{home_adapter_id}", stop_p_s_payload
        )

    async def update_home_endpoint_value(self, node_id, endpoint_id, value):
        """
        Update home endpoint value

        node_id : `int`
        endpoint_id : `int`
        value : `str`
        """

        home_e_v_data = {"value": value}
        return await self.set_home_endpoint_value(node_id, endpoint_id, home_e_v_data)

    async def validate_sms_number(self, sms_number_id, sms_n_v_data):
        """
        Validate sms number

        sms_number_id : `int`
        sms_n_v_data : `dict`
        """
        return await self._access.post(
            f"home/sms/numbers/{sms_number_id}/validate", sms_n_v_data
        )
