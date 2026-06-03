import sys
import glob
import asyncio
import logging
import importlib
import urllib3


from pathlib import Path
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def load_plugins(plugin_name):
    path = Path(f"MADARA/modules/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"MADARA.modules.{plugin_name}", path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["MADARA.modules." + plugin_name] = load
    print("Altron has Imported " + plugin_name)


files = glob.glob("MADARA/modules/*.py")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\n𝗢𝗫𝗬𝗚𝗘𝗡 𝐒𝐩𝐚𝐦 𝐁𝐨𝐭𝐬 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ⚡\nMy Master ---> @Oxygen_smg")


async def main():
    try:
        await asyncio.gather(
            X1.run_until_disconnected(),
            X2.run_until_disconnected(),
            X3.run_until_disconnected(),
            X4.run_until_disconnected(),
            X5.run_until_disconnected(),
            X6.run_until_disconnected(),
            X7.run_until_disconnected(),
            X8.run_until_disconnected(),
            X9.run_until_disconnected(),
            X10.run_until_disconnected(),
            return_exceptions=True
        )
    except (KeyboardInterrupt, asyncio.CancelledError):
        pass
    except Exception as e:
        logging.error(f"Error in main event loop: {e}")


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\n[!] Bot stopped by user")
    except Exception as e:
        logging.error(f"Fatal error: {e}")
