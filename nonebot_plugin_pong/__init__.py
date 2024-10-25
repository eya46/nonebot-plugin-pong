from nonebot.plugin import PluginMetadata
from nonebot.plugin.on import on_command


__plugin_meta__ = PluginMetadata(
    name="pong",
    description="ping -> pong",
    usage="ping",
    type="application",
    homepage="https://github.com/eya46/nonebot-plugin-pong",
)


ping = on_command("ping")


@ping.handle()
async def _():
    await ping.send("pong")
