import esphome.codegen as cg
from esphome.components import climate_ir
import esphome.config_validation as cv
from esphome.const import CONF_MODEL

AUTO_LOAD = ["climate_ir"]
CODEOWNERS = ["@kbx81", "@DavideGarbi"]

CONF_SUPPORTS_SWING_MODES = "supports_swing_modes"
CONF_SUPPORTS_FAN_ONLY_MODE = "supports_fan_only_mode"

toshiba_ns = cg.esphome_ns.namespace("toshiba")
ToshibaClimate = toshiba_ns.class_("ToshibaClimate", climate_ir.ClimateIR)

Model = toshiba_ns.enum("Model")
MODELS = {
    "GENERIC": Model.MODEL_GENERIC,
    "RAC-PT1411HWRU-C": Model.MODEL_RAC_PT1411HWRU_C,
    "RAC-PT1411HWRU-F": Model.MODEL_RAC_PT1411HWRU_F,
}

CONFIG_SCHEMA = climate_ir.climate_ir_with_receiver_schema(ToshibaClimate).extend(
    {
        cv.Optional(CONF_MODEL, default="generic"): cv.enum(MODELS, upper=True),
        cv.Optional(CONF_SUPPORTS_SWING_MODES, default=False): cv.boolean,
        cv.Optional(CONF_SUPPORTS_FAN_ONLY_MODE, default=True): cv.boolean,
    }
)


async def to_code(config):
    var = await climate_ir.new_climate_ir(config)
    cg.add(var.set_model(config[CONF_MODEL]))
    cg.add(var.set_supports_swing_modes(config[CONF_SUPPORTS_SWING_MODES]))
    cg.add(var.set_supports_fan_only_mode(config[CONF_SUPPORTS_FAN_ONLY_MODE]))