from typing import Any, Dict, List


class Freeplug:
    """
    Freeplug
    """

    def __init__(self, access) -> None:
        self._access = access

    async def get_freeplug_networks(self) -> List[Dict[str, Any]]:
        """
        Get freeplug networks
        """
        return await self._access.get("freeplug/")

    async def reset_freeplug(self, freeplug_id: int) -> None:
        """
        Reset freeplug

        freeplug_id : `int`
        """
        await self._access.post(f"freeplug/{freeplug_id}/reset/")
