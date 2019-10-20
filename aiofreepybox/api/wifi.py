class Wifi:
    """
    Wifi
    """

    def __init__(self, access):
        self._access = access

    # accessType can be full or net_only
    wifi_custom_key_params_schema = {
        "access_type": "full",
        "description": "",
        "duration": 0,
        "key": "",
        "max_use_count": 0,
    }

    wifi_custom_key_user_schema = {"host": "", "hostname": ""}

    wifi_custom_key_data_schema = {
        "id": 0,
        "params": wifi_custom_key_params_schema,
        "remaining": 0,
        "users": [wifi_custom_key_user_schema],
    }

    # type can be whitelist or blacklist
    wifi_mac_filter_schema = {"comment": "", "mac": "", "type": "blacklist"}

    start_wps_session_data_schema = {"bssid": ""}

    stop_wps_session_data_schema = {"sessionid": 0}

    async def create_wifi_custom_key(self, wifi_custom_key_data):
        """
        Create wifi custom key

        wifi_custom_key_data : `dict`
        """
        return await self._access.post("wifi/custom_key/", wifi_custom_key_data)

    async def create_wifi_mac_filter(self, wifi_mac_filter):
        """
        Create wifi mac filter

        wifi_mac_filter : `dict`
        """
        return await self._access.post("wifi/mac_filter/", wifi_mac_filter)

    async def delete_wifi_custom_key(self, key_id):
        """
        Delete wifi custom key

        key_id : `int`
        """
        return await self._access.delete(f"wifi/custom_key/{key_id}")

    async def delete_wifi_mac_filter(self, filter_id):
        """
        Delete wifi mac filter

        key_id : `int`
        """
        return await self._access.delete(f"wifi/mac_filter/{filter_id}")

    async def delete_wps_sessions(self):
        """
        Delete wps sessions
        """
        return await self._access.delete("wifi/wps/sessions")

    async def edit_wifi_access_point(self, ap_id, wifi_ap_configuration_data):
        """
        Edit wifi access point

        ap_id : `int`
        wifi_ap_configuration_data : `dict`
        """
        return await self._access.put(f"wifi/ap/{ap_id}", wifi_ap_configuration_data)

    async def edit_wifi_bss(self, bss_id, wifi_bss_data):
        """
        Edit wifi bss

        bss_id : `int`
        wifi_bss_data : `dict`
        """
        return await self._access.put(f"wifi/bss/{bss_id}", wifi_bss_data)

    async def edit_wifi_mac_filter(self, mac_filter, wifi_mac_filter):
        """
        Edit wifi mac filter

        mac_filter : `str`
        wifi_mac_filter : `dict`
        """
        return await self._access.put(f"wifi/mac_filter/{mac_filter}", wifi_mac_filter)

    async def get_ap(self, ap_id):
        """
        Get wifi access point with the specific id

        ap_id : `int`
        """
        return await self._access.get(f"wifi/ap/{ap_id}")

    async def get_ap_allowed_channel(self, ap_id):
        """
        Get allowed channels of the wifi access point

        ap_id : `int`
        """
        return await self._access.get(f"wifi/ap/{ap_id}/allowed_channel_comb/")

    async def get_wifi_access_point_channel_usage(self, ap_id):
        """
        get wifi access point channel usage

        ap_id : `int`
        """
        return await self._access.get(f"wifi/ap/{ap_id}/channel_usage/")

    async def get_ap_neighbors(self, ap_id):
        """
        Get the list of Wifi neighbors seen by the AP

        ap_id : `int`
        """
        return await self._access.get(f"wifi/ap/{ap_id}/neighbors/")

    async def get_wifi_access_point_station(self, ap_id, mac):
        """
        get wifi access point station

        ap_id : `int`
        mac : `str`
        """
        return await self._access.get(f"wifi/ap/{ap_id}/stations/{mac}")

    async def get_station_list(self, ap_id):
        """
        Get the list of Wifi Stations associated to the AP

        ap_id : `int`
        """
        return await self._access.get(f"wifi/ap/{ap_id}/stations/")

    async def get_ap_list(self):
        """
        Get wifi access points list
        """
        return await self._access.get("wifi/ap/")

    async def get_bss(self):
        """
        Get wifi bss
        """
        return await self._access.get("wifi/bss/")

    async def get_global_config(self):
        """
        Get wifi global configuration
        """
        return await self._access.get("wifi/config/")

    async def get_wifi_custom_keys(self):
        """
        Get wifi custom keys
        """
        return await self._access.get("wifi/custom_key/")

    async def get_wifi_mac_filters(self):
        """
        Get wifi mac filters
        """
        return await self._access.get("wifi/mac_filter/")

    async def get_wifi_planning(self):
        """
        Get wifi planning
        """
        return await self._access.get("wifi/planning/")

    async def get_wps_candidates(self):
        """
        Get wps candidates
        """
        return await self._access.get("wifi/wps/candidates/")

    async def get_wps_session(self, session_id):
        """
        Get wps session

        session_id : `int`
        """
        return await self._access.get(f"wifi/wps/sessions/{session_id}")

    async def get_wps_sessions(self, session_id):
        """
        Get wps sessions

        session_id : `int`
        """
        return await self._access.get("wifi/wps/sessions/")

    async def reset_wifi_configuration(self):
        """
        Reset wifi configuration
        """
        await self._access.put("wifi/config/reset/")

    async def set_global_config(self, global_configuration):
        """
        Update wifi global configuration

        global_configuration : `dict`
        """
        return await self._access.put("wifi/config/", global_configuration)

    async def set_wifi_planning(self, wifi_planning):
        """
        Set wifi planning

        wifi_planning : `dict`
        """
        return await self._access.put("wifi/planning/", wifi_planning)

    async def start_wifi_access_point_neighbors_scan(self, ap_id):
        """
        Start wifi access point neighbors scan

        ap_id : `int`
        """
        await self._access.post(f"wifi/ap/{ap_id}/neighbors/scan/")

    async def start_wps_session(self, start_wps_session_data):
        """
        Start wps session

        start_wps_session_data : `dict`
        """
        return await self._access.post("wifi/wps/start/", start_wps_session_data)

    async def stop_wps_session(self, stop_wps_session_data):
        """
        stop wps session

        stop_wps_session_data : `dict`
        """
        await self._access.post("wifi/wps/stop/", stop_wps_session_data)

