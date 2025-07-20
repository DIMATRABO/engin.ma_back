from config.app_factory import create_app
from config.config_handler import ConfigHandler

config = ConfigHandler()
app = create_app()

if __name__ == "__main__":
    app.run(
        host=config.app_host,
        port=config.app_port,
        debug=config.app_debug
    )
