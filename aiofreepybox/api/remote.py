import asyncio
from asyncio import TimeoutError as Timeout
from typing import Any, Dict, List, Optional, Union

from aiohttp import client_exceptions as cl_ex

from aiofreepybox.access import Access

_PL_LOCAL = "Freebox-Player.local"
_PL_HOST = "freeboxhd"
_PL_DOMAIN = ".freebox.fr"
_PL_STATUS = 200
_REMOTE_CONTROL = "/pub/remote_control"
_DEFAULT_ACCESS_MODE = "local"
_DEFAULT_DELAY = 1
_DEFAULT_LONG_PRESS = "False"
_DEFAULT_PL_ID = 1
_DEFAULT_REPEAT = 0
_DEFAULT_TIMEOUT = 5


class Remote:
    """
    Remote
    """

    def __init__(self, access: Access, access_m: Optional[str] = None) -> None:
        self._access = access
        self.set_player_host(access_m)

    codes = {
        "red",  # Bouton rouge
        "green",  # Bouton vert
        "blue",  # Bouton bleu
        "yellow",  # Bouton jaune
        "power",  # Bouton Power
        "list",  # Affichage de la liste des chaines
        "tv",  # Bouton tv
        "1",  # Bouton 1
        "2",  # Bouton 2
        "3",  # Bouton 3
        "4",  # Bouton 4
        "5",  # Bouton 5
        "6",  # Bouton 6
        "7",  # Bouton 7
        "8",  # Bouton 8
        "9",  # Bouton 9
        "back",  # Bouton jaune (retour)
        "0",  # Bouton 0
        "swap",  # Bouton swap
        "info",  # Bouton info
        "epg",  # Bouton epg (fct+)
        "mail",  # Bouton mail
        "media",  # Bouton media (fct+)
        "help",  # Bouton help
        "options",  # Bouton options (fct+)
        "pip",  # Bouton pip
        "vol_inc",  # Bouton volume +
        "vol_dec",  # Bouton volume -
        "ok",  # Bouton ok
        "up",  # Bouton haut
        "right",  # Bouton droite
        "down",  # Bouton bas
        "left",  # Bouton gauche
        "prgm_inc",  # Bouton programme +
        "prgm_dec",  # Bouton programme -
        "mute",  # Bouton sourdine
        "home",  # Bouton Free
        "rec",  # Bouton Rec
        "bwd",  # Bouton << retour arrière
        "prev",  # Bouton |<< précédent
        "play",  # Bouton Lecture / Pause
        "fwd",  # Bouton >> avance rapide
        "next",  # Bouton >>| suivant
    }
    key_macro_test = [{"key": "info", "long": "False"}, {"key": "info", "repeat": 0}]

    def build_key(self, **key_data: Union[str, int]) -> Dict[str, Any]:
        """
        Build key dict

        code : `str`
        key : `str`
        long : `str`
        repeat : `int`
        """

        if "long" in key_data and key_data["long"] == "False":
            try:
                del key_data["long"]
            except KeyError:
                pass
        if "repeat" in key_data and key_data["repeat"] == 0:
            try:
                del key_data["repeat"]
            except KeyError:
                pass

        return key_data

    async def send_key(
        self,
        code: str,
        key: str,
        long_press: str = _DEFAULT_LONG_PRESS,
        repeat: int = _DEFAULT_REPEAT,
    ):
        """
        Send Key

        code : `str`
        key : `str`
        long_press : `str`, optional
            Default to "False"
        repeat : `int`, optional
            Default to 0
        """
        return await self.set_key(
            key_data=self.build_key(code=code, key=key, long=long_press, repeat=repeat)
        )

    async def send_macro(
        self,
        keys_data: List[Dict[str, Any]],
        code: Optional[str] = None,
        delay: float = _DEFAULT_DELAY,
    ) -> bool:
        """
        Send macro

        keys_data : `list[key]`
        code : `str`, optional
            Default to None
        delay : `float`, optional
            Default to _DEFAULT_DELAY
        """

        for key_data in keys_data:
            if await self.set_key(key_data, code=code):
                await asyncio.sleep(delay)
            else:
                return False

        return True

    async def set_key(
        self, key_data: Dict[str, Any], code: Optional[str] = None
    ) -> bool:
        """
        Set Key

        key_data : `dict`
        code : `str`, optional
            Default to None

        Returns `True` if the key was accepted or `False` if an error occurred
        """

        if code is not None and (not "code" in key_data or key_data["code"] != code):
            key_data["code"] = code
        elif not "code" in key_data:
            return False

        try:
            r = await self._access.session.get(
                f"http://{self.player_host}{_REMOTE_CONTROL}",
                params=self.build_key(**key_data),
                timeout=_DEFAULT_TIMEOUT,
                skip_auto_headers=[
                    "Accept",
                    "Accept-Encoding",
                    "Content-type",
                    "User-Agent",
                ],
            )
            async with r:
                await r.read()
                if r.status == _PL_STATUS and r.content_length == 0:
                    return True
        except (Timeout, cl_ex.ServerDisconnectedError):
            pass

        return False

    def set_player_host(
        self,
        access_m: Optional[str] = None,
        host: Optional[str] = None,
        player_id: Optional[int] = None,
    ) -> None:
        """
        Set player host

        access_m : `str`, "local", "host", "fbxhd"
            Default to _DEFAULT_ACCESS_MODE
        host : `str`, optional
            Default to None
        player_id : `int`, optional
            Default to _DEFAULT_PL_ID
        """

        self.access_mode = _DEFAULT_ACCESS_MODE if access_m is None else access_m
        if self.access_mode == "fbxhd":
            self.player_host = f"{_PL_HOST}"
            f"{_DEFAULT_PL_ID if player_id is None else player_id}{_PL_DOMAIN}"
        elif self.access_mode == "host" and host is not None:
            self.player_host = host
        else:
            self.player_host = _PL_LOCAL
