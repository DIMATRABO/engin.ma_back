from config.app_factory import create_app
from config.config_handler import Config_handler

config = Config_handler()
app = create_app()

if __name__ == "__main__":
    app.run(
        host=config.app_host,
        port=config.app_port,
        debug=config.app_debug
    )
