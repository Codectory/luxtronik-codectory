"""Constants for the Paul Novus 300 Bus integration."""
import logging
from datetime import timedelta
from enum import Enum
from typing import Dict, Final

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.const import (CONF_HOST, CONF_PORT, DEVICE_CLASS_ENERGY,
                                 DEVICE_CLASS_PRESSURE,
                                 DEVICE_CLASS_TEMPERATURE,
                                 DEVICE_CLASS_TIMESTAMP,
                                 ELECTRIC_POTENTIAL_VOLT,
                                 ENERGY_KILO_WATT_HOUR, PERCENTAGE,
                                 PRESSURE_BAR, TEMP_CELSIUS, TEMP_KELVIN,
                                 TIME_HOURS, TIME_SECONDS)

DOMAIN: Final = "luxtronik2"

LOGGER: Final[logging.Logger] = logging.getLogger(__package__)
DEFAULT_PORT: Final = 8888

DEFAULT_TOLERANCE = 0.3

ATTR_PARAMETER: Final = "parameter"
ATTR_VALUE: Final = "value"

ATTR_STATUS_TEXT: Final = "status_text"

CONF_SAFE: Final = "safe"
CONF_LOCK_TIMEOUT: Final = "lock_timeout"
CONF_UPDATE_IMMEDIATELY_AFTER_WRITE: Final = "update_immediately_after_write"

CONF_PARAMETERS: Final = "parameters"
CONF_CALCULATIONS: Final = "calculations"
CONF_VISIBILITIES: Final = "visibilities"

CONF_COORDINATOR: Final = "coordinator"

CONF_CONTROL_MODE_HOME_ASSISTANT = "control_mode_home_assistant"
CONF_HA_SENSOR_INDOOR_TEMPERATURE = "ha_sensor_indoor_temperature"
CONF_LANGUAGE_SENSOR_NAMES = "language_sensor_names"


SERVICE_WRITE = "write"

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=10)

LANG_EN = 'en'
LANG_DE = 'de'
LANG_DEFAULT = LANG_EN
LANGUAGES = Enum(LANG_EN, LANG_DE)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_HOST): cv.string,
                vol.Required(CONF_PORT, default=DEFAULT_PORT): cv.port,
                vol.Optional(CONF_SAFE, default=True): cv.boolean,
                vol.Optional(CONF_LOCK_TIMEOUT, default=30): cv.positive_int,
                vol.Optional(
                    CONF_UPDATE_IMMEDIATELY_AFTER_WRITE, default=False
                ): cv.boolean,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)

SERVICE_WRITE_SCHEMA = vol.Schema(
    {
        vol.Required(ATTR_PARAMETER): cv.string,
        vol.Required(ATTR_VALUE): vol.Any(cv.Number, cv.string),
    }
)

# "binary_sensor"
PLATFORMS: Final[list[str]] = ["climate", "sensor", "number"]

PRESET_SECOND_HEATSOURCE: Final = 'second_heatsource'

LUX_MODE_OFF: Final = 'Off'
LUX_MODE_AUTOMATIC: Final = 'Automatic'
LUX_MODE_SECOND_HEATSOURCE: Final = 'Second heatsource'
LUX_MODE_PARTY: Final = 'Party'
LUX_MODE_HOLIDAYS: Final = 'Holidays'

LUX_STATUS_HEATING: Final = 'heating'                                   # 0
LUX_STATUS_DOMESTIC_WATER: Final = 'hot water'                          # 1
LUX_STATUS_SWIMMING_POOL_SOLAR: Final = 'swimming pool/solar'           # 2
LUX_STATUS_EVU: Final = 'evu'                                           # 3
LUX_STATUS_DEFROST: Final = 'defrost'                                   # 4
LUX_STATUS_NO_REQUEST: Final = 'no request'                             # 5
LUX_STATUS_HEATING_EXTERNAL_SOURCE: Final = 'heating external source'   # 6
LUX_STATUS_COOLING: Final = 'cooling'                                   # 7

LUX_STATES_ON = [LUX_STATUS_HEATING, LUX_STATUS_DOMESTIC_WATER, LUX_STATUS_SWIMMING_POOL_SOLAR,
                 LUX_STATUS_DEFROST, LUX_STATUS_HEATING_EXTERNAL_SOURCE, LUX_STATUS_COOLING]

LUX_STATE_ICON_MAP: Dict[str, str] = {
    LUX_STATUS_HEATING: 'mdi:radiator',
    LUX_STATUS_DOMESTIC_WATER: 'mdi:waves',
    LUX_STATUS_SWIMMING_POOL_SOLAR: None,
    LUX_STATUS_EVU: 'mdi:power-plug-off',
    LUX_STATUS_DEFROST: 'mdi:car-defrost-rear',
    LUX_STATUS_NO_REQUEST: 'mdi:radiator-disabled',
    LUX_STATUS_HEATING_EXTERNAL_SOURCE: None,
    LUX_STATUS_COOLING: 'mdi:air-conditioner'
}

# region Luxtronik Sensor ids
LUX_SENSOR_DETECT_COOLING: Final = 'calculations.ID_WEB_FreigabKuehl'
LUX_SENSOR_STATUS: Final = 'calculations.ID_WEB_WP_BZ_akt'

LUX_SENSOR_HEATING_TEMPERATURE_CORRECTION: Final = 'parameters.ID_Einst_WK_akt'
LUX_SENSOR_HEATING_HEATER: Final = 'parameters.ID_Ba_Hz_akt'

LUX_SENSOR_DOMESTIC_WATER_CURRENT_TEMPERATURE: Final = 'calculations.ID_WEB_Temperatur_TBW'
LUX_SENSOR_DOMESTIC_WATER_TARGET_TEMPERATURE: Final = 'parameters.ID_Einst_BWS_akt'
# LUX_SENSOR_DOMESTIC_WATER_TARGET_TEMPERATURE: Final = 'calculations.ID_WEB_Einst_BWS_akt'
# LUX_SENSOR_DOMESTIC_WATER_TARGET_TEMPERATURE_WRITE: Final = 'ID_Einst_BWS_akt'
LUX_SENSOR_DOMESTIC_WATER_HEATER: Final = 'parameters.ID_Ba_Bw_akt'
# endregion Luxtronik Sensor ids

# region Legacy consts
CONF_GROUP = "group"

CONF_CELSIUS = "celsius"
CONF_SECONDS = "seconds"
CONF_TIMESTAMP = "timestamp"
CONF_KELVIN = "kelvin"
CONF_BAR = "bar"
CONF_PERCENT = "percent"
CONF_ENERGY = "energy"
CONF_HOURS = "hours"
CONF_VOLTAGE = "voltage"
CONF_FLOW = "flow"

DEFAULT_DEVICE_CLASS = None

ICONS = {
    CONF_CELSIUS: "mdi:thermometer",
    CONF_SECONDS: "mdi:timer-sand",
    "pulses": "mdi:pulse",
    "ipaddress": "mdi:ip-network-outline",
    CONF_TIMESTAMP: "mdi:calendar-range",
    "errorcode": "mdi:alert-circle-outline",
    CONF_KELVIN: "mdi:thermometer",
    CONF_BAR: "mdi:arrow-collapse-all",
    CONF_PERCENT: "mdi:percent",
    "rpm": "mdi:rotate-right",
    CONF_ENERGY: "mdi:lightning-bolt-circle",
    CONF_VOLTAGE: "mdi:flash-outline",
    CONF_HOURS: "mdi:clock-outline",
    CONF_FLOW: "mdi:chart-bell-curve",
    "level": "mdi:format-list-numbered",
    "count": "mdi:counter",
    "version": "mdi:information-outline",
}

DEVICE_CLASSES = {
    CONF_CELSIUS: DEVICE_CLASS_TEMPERATURE,
    CONF_KELVIN: DEVICE_CLASS_TEMPERATURE,
    CONF_BAR: DEVICE_CLASS_PRESSURE,
    CONF_SECONDS: DEVICE_CLASS_TIMESTAMP,
    CONF_HOURS: DEVICE_CLASS_TIMESTAMP,
    CONF_TIMESTAMP: DEVICE_CLASS_TIMESTAMP,
    CONF_ENERGY: DEVICE_CLASS_ENERGY,
}

UNITS = {
    CONF_CELSIUS: TEMP_CELSIUS,
    CONF_SECONDS: TIME_SECONDS,
    CONF_KELVIN: TEMP_KELVIN,
    CONF_BAR: PRESSURE_BAR,
    CONF_PERCENT: PERCENTAGE,
    CONF_ENERGY: ENERGY_KILO_WATT_HOUR,
    CONF_VOLTAGE: ELECTRIC_POTENTIAL_VOLT,
    CONF_HOURS: TIME_HOURS,
    CONF_FLOW: "l/h",
}
# endregion Legacy consts
