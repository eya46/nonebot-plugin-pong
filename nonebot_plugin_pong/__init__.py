from nonebot.plugin import PluginMetadata, on_command

__plugin_meta__ = PluginMetadata(
    name="pong",
    description="ping -> pong",
    usage="ping",
    type="application",
    homepage="https://github.com/eya46/nonebot-plugin-pong",
    supported_adapters=None,
)


ping = on_command("ping")


@ping.handle()
async def _():
    await ping.send("pong")
