from typing import Any, Dict, Optional

from aiofreepybox.access import Access


class Netshare:
    """
    Netshare
    """

    def __init__(self, access: Access) -> None:
        self._access = access

    server_type = [
        "powerbook",
        "powermac",
        "macmini",
        "imac",
        "macbook",
        "macbookpro",
        "macbookair",
        "macpro",
        "appletv",
        "airport",
        "xserve",
    ]
    afp_configuration_schema = {
        "enabled": False,
        "guest_allow": False,
        "login_name": "",
        "login_password": "",
        "server_type": server_type[0],
    }
    samba_configuration_schema = {
        "file_share_enabled": False,
        "logon_enabled": False,
        "logon_password": "",
        "logon_user": "",
        "print_share_enabled": True,
        "workgroup": "workgroup",
    }

    async def afp_switch(self, enabled: Optional[bool] = None) -> Optional[bool]:
        """
        Afp server switch

        enabled : `bool` , optional
            , Default to None

        Returns `None` or enabled : `bool`
        """

        if enabled is not None:
            afp_config = {"enabled": enabled}
            config = await self.set_afp_configuration(afp_config)
        else:
            config = await self.get_afp_configuration()
        if config is not None:
            return config["enabled"]
        else:
            return None

    async def get_afp_configuration(self) -> Optional[Dict[str, Any]]:
        """
        Get afp configuration
        """
        return await self._access.get("netshare/afp/")

    async def get_samba_configuration(self) -> Optional[Dict[str, Any]]:
        """
        Get samba configuration
        """
        return await self._access.get("netshare/samba/")

    async def samba_file_share_switch(
        self, enabled: Optional[bool] = None
    ) -> Optional[bool]:
        """
        Samba file share switch

        enabled : `bool` , optional
            , Default to None

        Returns `None` or enabled : `bool`
        """

        if enabled is not None:
            samba_config = {"file_share_enabled": enabled}
            config = await self.set_samba_configuration(samba_config)
        else:
            config = await self.get_samba_configuration()
        if config is not None:
            return config["file_share_enabled"]
        else:
            return None

    async def samba_print_share_switch(
        self, enabled: Optional[bool] = None
    ) -> Optional[bool]:
        """
        Samba print share switch

        enabled : `bool` , optional
            , Default to None

        Returns `None` or enabled : `bool`
        """

        if enabled is not None:
            samba_config = {"print_share_enabled": enabled}
            config = await self.set_samba_configuration(samba_config)
        else:
            config = await self.get_samba_configuration()
        if config is not None:
            return config["print_share_enabled"]
        else:
            return None

    async def set_afp_configuration(
        self, afp_configuration: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """
        Set afp configuration

        afp_configuration : `dict`
        """
        return await self._access.put("netshare/afp/", afp_configuration)

    async def set_samba_configuration(
        self, samba_configuration: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """
        Set samba configuration

        samba_configuration : `dict`
        """
        return await self._access.put("netshare/samba/", samba_configuration)
