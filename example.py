#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This example can be run safely as it won't change anything in your box configuration
'''

import asyncio
import m3u8

from aiofreepybox import Freepybox
from aiofreepybox.exceptions import (NotOpenError, AuthorizationError)


async def demo():
    # Instantiate Freepybox class using default application descriptor
    # and default token_file location
    fbx = Freepybox()

    # To find out the HTTPS host and port of your freebox, go to
    # http://mafreebox.freebox.fr/api_version or let auto detect do it for you

    # Connect to the freebox
    # Be ready to authorize the application on the Freebox if you use this
    # example for the first time

    try:
        await fbx.open()
    except NotOpenError as e:
        print(f"Something went wrong {e}")
    except AuthorizationError as e:
        print(str(e))

    if fbx.api_version == 'v6':
        # Get a jpg snapshot from a camera
        fbx_cam_jpg = await fbx.home.get_camera_snapshot()
        fbx_cam_jpg.close()

        # Get a TS stream from a camera
        r = await fbx.home.get_camera_stream_m3u8()
        m3u8_obj = m3u8.loads(await r.text())
        r.close()
        fbx_ts = await fbx.home.get_camera_ts(m3u8_obj.files[0])
        fbx_ts.close()

    # Dump freebox configuration using system API
    # Extract temperature and mac address
    fbx_config = await fbx.system.get_config()
    print('Freebox temperature : {0}'.format(fbx_config['temp_sw']))
    print('Freebox mac address : {0}'.format(fbx_config['mac']))

    # Dump DHCP configuration using dhcp API
    fbx_dhcp_config = await fbx.dhcp.get_config()
    # Modify ip_range configuration
    fbx_dhcp_config['ip_range_start'] = '192.168.0.10'
    fbx_dhcp_config['ip_range_end'] = '192.168.0.50'
    # Send new configuration to the freebox. This line is commented to avoid any disaster.
    # await fbx.dhcp.set_config(fbx_dhcp_config)

    # Get the call list and print the last call entry
    fbx_call_list = await fbx.call.get_call_list()
    print(fbx_call_list[0])

    # Reboot your freebox. This line is commented to avoid any disaster.
    # await fbx.system.reboot()

    # Close the freebox session
    await fbx.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(demo())
loop.close()
