#!/usr/bin/env python3

"""
    Copyright 2023 carlkidcrypto, All rights reserved.
    Helpers and constants for the test files.
"""

DATA_IN_1 = {
    "api_version": "V1.0.11-0.0.34",
    "time_stamp": 1659710288,
    "data_time_stamp": 1659710232,
    "max_age": 604800,
    "firmware_default_version": "7.00",
    "fields": ["sensor_index", "name"],
    "data": [[1, "TEST1"], [2, "TEST2"], [3, "TEST3"]],
}

DATA_IN_2 = {
    "api_version": "V1.0.11-0.0.42",
    "time_stamp": 1676263167,
    "data_time_stamp": 1676263122,
    "sensor": {
        "sensor_index": 131190,
        "last_modified": 1646085907,
        "date_created": 1633034575,
        "last_seen": 1676263011,
    },
}

DATA_OUT_1 = [
    {
        "data_time_stamp": 1659710232,
        "sensor_index": 1,
        "name": "TEST1",
        "icon": 0,
        "model": "",
        "hardware": "",
        "location_type": 0,
        "private": 0,
        "latitude": 0.0,
        "longitude": 0.0,
        "altitude": 0.0,
        "position_rating": 0,
        "led_brightness": 0,
        "firmware_version": "",
        "firmware_upgrade": "",
        "rssi": 0,
        "uptime": 0,
        "pa_latency": 0,
        "memory": 0,
        "last_seen": 0,
        "last_modified": 0,
        "date_created": 0,
        "channel_state": 0,
        "channel_flags": 0,
        "channel_flags_manual": 0,
        "channel_flags_auto": 0,
        "confidence": 0,
        "confidence_manual": 0,
        "confidence_auto": 0,
        "humidity": 0,
        "humidity_a": 0,
        "humidity_b": 0,
        "temperature": 0,
        "temperature_a": 0,
        "temperature_b": 0,
        "pressure": 0.0,
        "pressure_a": 0.0,
        "pressure_b": 0.0,
        "voc": 0.0,
        "voc_a": 0.0,
        "voc_b": 0.0,
        "ozone1": 0.0,
        "analog_input": 0.0,
        "pm1.0": 0.0,
        "pm1.0_a": 0.0,
        "pm1.0_b": 0.0,
        "pm1.0_atm": 0.0,
        "pm1.0_atm_a": 0.0,
        "pm1.0_atm_b": 0.0,
        "pm1.0_cf_1": 0.0,
        "pm1.0_cf_1_a": 0.0,
        "pm1.0_cf_1_b": 0.0,
        "pm2.5_alt": 0.0,
        "pm2.5_alt_a": 0.0,
        "pm2.5_alt_b": 0.0,
        "pm2.5": 0.0,
        "pm2.5_a": 0.0,
        "pm2.5_b": 0.0,
        "pm2.5_atm": 0.0,
        "pm2.5_atm_a": 0.0,
        "pm2.5_atm_b": 0.0,
        "pm2.5_cf_1": 0.0,
        "pm2.5_cf_1_a": 0.0,
        "pm2.5_cf_1_b": 0.0,
        "pm2.5_10minute": 0.0,
        "pm2.5_10minute_a": 0.0,
        "pm2.5_10minute_b": 0.0,
        "pm2.5_30minute": 0.0,
        "pm2.5_30minute_a": 0.0,
        "pm2.5_30minute_b": 0.0,
        "pm2.5_60minute": 0.0,
        "pm2.5_60minute_a": 0.0,
        "pm2.5_60minute_b": 0.0,
        "pm2.5_6hour": 0.0,
        "pm2.5_6hour_a": 0.0,
        "pm2.5_6hour_b": 0.0,
        "pm2.5_24hour": 0.0,
        "pm2.5_24hour_a": 0.0,
        "pm2.5_24hour_b": 0.0,
        "pm2.5_1week": 0.0,
        "pm2.5_1week_a": 0.0,
        "pm2.5_1week_b": 0.0,
        "pm10.0": 0.0,
        "pm10.0_a": 0.0,
        "pm10.0_b": 0.0,
        "pm10.0_atm": 0.0,
        "pm10.0_atm_a": 0.0,
        "pm10.0_atm_b": 0.0,
        "pm10.0_cf_1": 0.0,
        "pm10.0_cf_1_a": 0.0,
        "pm10.0_cf_1_b": 0.0,
        "0.3_um_count": 0.0,
        "0.3_um_count_a": 0.0,
        "0.3_um_count_b": 0.0,
        "0.5_um_count": 0.0,
        "0.5_um_count_a": 0.0,
        "0.5_um_count_b": 0.0,
        "1.0_um_count": 0.0,
        "1.0_um_count_a": 0.0,
        "1.0_um_count_b": 0.0,
        "2.5_um_count": 0.0,
        "2.5_um_count_a": 0.0,
        "2.5_um_count_b": 0.0,
        "5.0_um_count": 0.0,
        "5.0_um_count_a": 0.0,
        "5.0_um_count_b": 0.0,
        "10.0_um_count": 0.0,
        "10.0_um_count_a": 0.0,
        "10.0_um_count_b": 0.0,
        "primary_id_a": 0,
        "primary_key_a": "",
        "secondary_id_a": 0,
        "secondary_key_a": "",
        "primary_id_b": 0,
        "primary_key_b": "",
        "secondary_id_b": 0,
        "secondary_key_b": "",
    },
    {
        "data_time_stamp": 1659710232,
        "sensor_index": 2,
        "name": "TEST2",
        "icon": 0,
        "model": "",
        "hardware": "",
        "location_type": 0,
        "private": 0,
        "latitude": 0.0,
        "longitude": 0.0,
        "altitude": 0.0,
        "position_rating": 0,
        "led_brightness": 0,
        "firmware_version": "",
        "firmware_upgrade": "",
        "rssi": 0,
        "uptime": 0,
        "pa_latency": 0,
        "memory": 0,
        "last_seen": 0,
        "last_modified": 0,
        "date_created": 0,
        "channel_state": 0,
        "channel_flags": 0,
        "channel_flags_manual": 0,
        "channel_flags_auto": 0,
        "confidence": 0,
        "confidence_manual": 0,
        "confidence_auto": 0,
        "humidity": 0,
        "humidity_a": 0,
        "humidity_b": 0,
        "temperature": 0,
        "temperature_a": 0,
        "temperature_b": 0,
        "pressure": 0.0,
        "pressure_a": 0.0,
        "pressure_b": 0.0,
        "voc": 0.0,
        "voc_a": 0.0,
        "voc_b": 0.0,
        "ozone1": 0.0,
        "analog_input": 0.0,
        "pm1.0": 0.0,
        "pm1.0_a": 0.0,
        "pm1.0_b": 0.0,
        "pm1.0_atm": 0.0,
        "pm1.0_atm_a": 0.0,
        "pm1.0_atm_b": 0.0,
        "pm1.0_cf_1": 0.0,
        "pm1.0_cf_1_a": 0.0,
        "pm1.0_cf_1_b": 0.0,
        "pm2.5_alt": 0.0,
        "pm2.5_alt_a": 0.0,
        "pm2.5_alt_b": 0.0,
        "pm2.5": 0.0,
        "pm2.5_a": 0.0,
        "pm2.5_b": 0.0,
        "pm2.5_atm": 0.0,
        "pm2.5_atm_a": 0.0,
        "pm2.5_atm_b": 0.0,
        "pm2.5_cf_1": 0.0,
        "pm2.5_cf_1_a": 0.0,
        "pm2.5_cf_1_b": 0.0,
        "pm2.5_10minute": 0.0,
        "pm2.5_10minute_a": 0.0,
        "pm2.5_10minute_b": 0.0,
        "pm2.5_30minute": 0.0,
        "pm2.5_30minute_a": 0.0,
        "pm2.5_30minute_b": 0.0,
        "pm2.5_60minute": 0.0,
        "pm2.5_60minute_a": 0.0,
        "pm2.5_60minute_b": 0.0,
        "pm2.5_6hour": 0.0,
        "pm2.5_6hour_a": 0.0,
        "pm2.5_6hour_b": 0.0,
        "pm2.5_24hour": 0.0,
        "pm2.5_24hour_a": 0.0,
        "pm2.5_24hour_b": 0.0,
        "pm2.5_1week": 0.0,
        "pm2.5_1week_a": 0.0,
        "pm2.5_1week_b": 0.0,
        "pm10.0": 0.0,
        "pm10.0_a": 0.0,
        "pm10.0_b": 0.0,
        "pm10.0_atm": 0.0,
        "pm10.0_atm_a": 0.0,
        "pm10.0_atm_b": 0.0,
        "pm10.0_cf_1": 0.0,
        "pm10.0_cf_1_a": 0.0,
        "pm10.0_cf_1_b": 0.0,
        "0.3_um_count": 0.0,
        "0.3_um_count_a": 0.0,
        "0.3_um_count_b": 0.0,
        "0.5_um_count": 0.0,
        "0.5_um_count_a": 0.0,
        "0.5_um_count_b": 0.0,
        "1.0_um_count": 0.0,
        "1.0_um_count_a": 0.0,
        "1.0_um_count_b": 0.0,
        "2.5_um_count": 0.0,
        "2.5_um_count_a": 0.0,
        "2.5_um_count_b": 0.0,
        "5.0_um_count": 0.0,
        "5.0_um_count_a": 0.0,
        "5.0_um_count_b": 0.0,
        "10.0_um_count": 0.0,
        "10.0_um_count_a": 0.0,
        "10.0_um_count_b": 0.0,
        "primary_id_a": 0,
        "primary_key_a": "",
        "secondary_id_a": 0,
        "secondary_key_a": "",
        "primary_id_b": 0,
        "primary_key_b": "",
        "secondary_id_b": 0,
        "secondary_key_b": "",
    },
    {
        "data_time_stamp": 1659710232,
        "sensor_index": 3,
        "name": "TEST3",
        "icon": 0,
        "model": "",
        "hardware": "",
        "location_type": 0,
        "private": 0,
        "latitude": 0.0,
        "longitude": 0.0,
        "altitude": 0.0,
        "position_rating": 0,
        "led_brightness": 0,
        "firmware_version": "",
        "firmware_upgrade": "",
        "rssi": 0,
        "uptime": 0,
        "pa_latency": 0,
        "memory": 0,
        "last_seen": 0,
        "last_modified": 0,
        "date_created": 0,
        "channel_state": 0,
        "channel_flags": 0,
        "channel_flags_manual": 0,
        "channel_flags_auto": 0,
        "confidence": 0,
        "confidence_manual": 0,
        "confidence_auto": 0,
        "humidity": 0,
        "humidity_a": 0,
        "humidity_b": 0,
        "temperature": 0,
        "temperature_a": 0,
        "temperature_b": 0,
        "pressure": 0.0,
        "pressure_a": 0.0,
        "pressure_b": 0.0,
        "voc": 0.0,
        "voc_a": 0.0,
        "voc_b": 0.0,
        "ozone1": 0.0,
        "analog_input": 0.0,
        "pm1.0": 0.0,
        "pm1.0_a": 0.0,
        "pm1.0_b": 0.0,
        "pm1.0_atm": 0.0,
        "pm1.0_atm_a": 0.0,
        "pm1.0_atm_b": 0.0,
        "pm1.0_cf_1": 0.0,
        "pm1.0_cf_1_a": 0.0,
        "pm1.0_cf_1_b": 0.0,
        "pm2.5_alt": 0.0,
        "pm2.5_alt_a": 0.0,
        "pm2.5_alt_b": 0.0,
        "pm2.5": 0.0,
        "pm2.5_a": 0.0,
        "pm2.5_b": 0.0,
        "pm2.5_atm": 0.0,
        "pm2.5_atm_a": 0.0,
        "pm2.5_atm_b": 0.0,
        "pm2.5_cf_1": 0.0,
        "pm2.5_cf_1_a": 0.0,
        "pm2.5_cf_1_b": 0.0,
        "pm2.5_10minute": 0.0,
        "pm2.5_10minute_a": 0.0,
        "pm2.5_10minute_b": 0.0,
        "pm2.5_30minute": 0.0,
        "pm2.5_30minute_a": 0.0,
        "pm2.5_30minute_b": 0.0,
        "pm2.5_60minute": 0.0,
        "pm2.5_60minute_a": 0.0,
        "pm2.5_60minute_b": 0.0,
        "pm2.5_6hour": 0.0,
        "pm2.5_6hour_a": 0.0,
        "pm2.5_6hour_b": 0.0,
        "pm2.5_24hour": 0.0,
        "pm2.5_24hour_a": 0.0,
        "pm2.5_24hour_b": 0.0,
        "pm2.5_1week": 0.0,
        "pm2.5_1week_a": 0.0,
        "pm2.5_1week_b": 0.0,
        "pm10.0": 0.0,
        "pm10.0_a": 0.0,
        "pm10.0_b": 0.0,
        "pm10.0_atm": 0.0,
        "pm10.0_atm_a": 0.0,
        "pm10.0_atm_b": 0.0,
        "pm10.0_cf_1": 0.0,
        "pm10.0_cf_1_a": 0.0,
        "pm10.0_cf_1_b": 0.0,
        "0.3_um_count": 0.0,
        "0.3_um_count_a": 0.0,
        "0.3_um_count_b": 0.0,
        "0.5_um_count": 0.0,
        "0.5_um_count_a": 0.0,
        "0.5_um_count_b": 0.0,
        "1.0_um_count": 0.0,
        "1.0_um_count_a": 0.0,
        "1.0_um_count_b": 0.0,
        "2.5_um_count": 0.0,
        "2.5_um_count_a": 0.0,
        "2.5_um_count_b": 0.0,
        "5.0_um_count": 0.0,
        "5.0_um_count_a": 0.0,
        "5.0_um_count_b": 0.0,
        "10.0_um_count": 0.0,
        "10.0_um_count_a": 0.0,
        "10.0_um_count_b": 0.0,
        "primary_id_a": 0,
        "primary_key_a": "",
        "secondary_id_a": 0,
        "secondary_key_a": "",
        "primary_id_b": 0,
        "primary_key_b": "",
        "secondary_id_b": 0,
        "secondary_key_b": "",
    },
]

DATA_OUT_2 = {
    "data_time_stamp": 1676263122,
    "sensor_index": 131190,
    "last_modified": 1646085907,
    "date_created": 1633034575,
    "last_seen": 1676263011,
    "name": "",
    "icon": 0,
    "model": "",
    "hardware": "",
    "location_type": 0,
    "private": 0,
    "latitude": 0.0,
    "longitude": 0.0,
    "altitude": 0.0,
    "position_rating": 0,
    "led_brightness": 0,
    "firmware_version": "",
    "firmware_upgrade": "",
    "rssi": 0,
    "uptime": 0,
    "pa_latency": 0,
    "memory": 0,
    "channel_state": 0,
    "channel_flags": 0,
    "channel_flags_manual": 0,
    "channel_flags_auto": 0,
    "confidence": 0,
    "confidence_manual": 0,
    "confidence_auto": 0,
    "humidity": 0,
    "humidity_a": 0,
    "humidity_b": 0,
    "temperature": 0,
    "temperature_a": 0,
    "temperature_b": 0,
    "pressure": 0.0,
    "pressure_a": 0.0,
    "pressure_b": 0.0,
    "voc": 0.0,
    "voc_a": 0.0,
    "voc_b": 0.0,
    "ozone1": 0.0,
    "analog_input": 0.0,
    "pm1.0": 0.0,
    "pm1.0_a": 0.0,
    "pm1.0_b": 0.0,
    "pm1.0_atm": 0.0,
    "pm1.0_atm_a": 0.0,
    "pm1.0_atm_b": 0.0,
    "pm1.0_cf_1": 0.0,
    "pm1.0_cf_1_a": 0.0,
    "pm1.0_cf_1_b": 0.0,
    "pm2.5_alt": 0.0,
    "pm2.5_alt_a": 0.0,
    "pm2.5_alt_b": 0.0,
    "pm2.5": 0.0,
    "pm2.5_a": 0.0,
    "pm2.5_b": 0.0,
    "pm2.5_atm": 0.0,
    "pm2.5_atm_a": 0.0,
    "pm2.5_atm_b": 0.0,
    "pm2.5_cf_1": 0.0,
    "pm2.5_cf_1_a": 0.0,
    "pm2.5_cf_1_b": 0.0,
    "pm2.5_10minute": 0.0,
    "pm2.5_10minute_a": 0.0,
    "pm2.5_10minute_b": 0.0,
    "pm2.5_30minute": 0.0,
    "pm2.5_30minute_a": 0.0,
    "pm2.5_30minute_b": 0.0,
    "pm2.5_60minute": 0.0,
    "pm2.5_60minute_a": 0.0,
    "pm2.5_60minute_b": 0.0,
    "pm2.5_6hour": 0.0,
    "pm2.5_6hour_a": 0.0,
    "pm2.5_6hour_b": 0.0,
    "pm2.5_24hour": 0.0,
    "pm2.5_24hour_a": 0.0,
    "pm2.5_24hour_b": 0.0,
    "pm2.5_1week": 0.0,
    "pm2.5_1week_a": 0.0,
    "pm2.5_1week_b": 0.0,
    "pm10.0": 0.0,
    "pm10.0_a": 0.0,
    "pm10.0_b": 0.0,
    "pm10.0_atm": 0.0,
    "pm10.0_atm_a": 0.0,
    "pm10.0_atm_b": 0.0,
    "pm10.0_cf_1": 0.0,
    "pm10.0_cf_1_a": 0.0,
    "pm10.0_cf_1_b": 0.0,
    "0.3_um_count": 0.0,
    "0.3_um_count_a": 0.0,
    "0.3_um_count_b": 0.0,
    "0.5_um_count": 0.0,
    "0.5_um_count_a": 0.0,
    "0.5_um_count_b": 0.0,
    "1.0_um_count": 0.0,
    "1.0_um_count_a": 0.0,
    "1.0_um_count_b": 0.0,
    "2.5_um_count": 0.0,
    "2.5_um_count_a": 0.0,
    "2.5_um_count_b": 0.0,
    "5.0_um_count": 0.0,
    "5.0_um_count_a": 0.0,
    "5.0_um_count_b": 0.0,
    "10.0_um_count": 0.0,
    "10.0_um_count_a": 0.0,
    "10.0_um_count_b": 0.0,
    "primary_id_a": 0,
    "primary_key_a": "",
    "secondary_id_a": 0,
    "secondary_key_a": "",
    "primary_id_b": 0,
    "primary_key_b": "",
    "secondary_id_b": 0,
    "secondary_key_b": "",
}

EXPECTED_VALUE_1 = {
    "name": "",
    "icon": 0,
    "model": "",
    "hardware": "",
    "location_type": 0,
    "private": 0,
    "latitude": 0.0,
    "longitude": 0.0,
    "altitude": 0.0,
    "position_rating": 0,
    "led_brightness": 0,
    "firmware_version": "",
    "firmware_upgrade": "",
    "rssi": 0,
    "uptime": 0,
    "pa_latency": 0,
    "memory": 0,
    "last_seen": 0,
    "last_modified": 0,
    "date_created": 0,
    "channel_state": 0,
    "channel_flags": 0,
    "channel_flags_manual": 0,
    "channel_flags_auto": 0,
    "confidence": 0,
    "confidence_manual": 0,
    "confidence_auto": 0,
    "humidity": 0,
    "humidity_a": 0,
    "humidity_b": 0,
    "temperature": 0,
    "temperature_a": 0,
    "temperature_b": 0,
    "pressure": 0.0,
    "pressure_a": 0.0,
    "pressure_b": 0.0,
    "voc": 0.0,
    "voc_a": 0.0,
    "voc_b": 0.0,
    "ozone1": 0.0,
    "analog_input": 0.0,
    "pm1.0": 0.0,
    "pm1.0_a": 0.0,
    "pm1.0_b": 0.0,
    "pm1.0_atm": 0.0,
    "pm1.0_atm_a": 0.0,
    "pm1.0_atm_b": 0.0,
    "pm1.0_cf_1": 0.0,
    "pm1.0_cf_1_a": 0.0,
    "pm1.0_cf_1_b": 0.0,
    "pm2.5_alt": 0.0,
    "pm2.5_alt_a": 0.0,
    "pm2.5_alt_b": 0.0,
    "pm2.5": 0.0,
    "pm2.5_a": 0.0,
    "pm2.5_b": 0.0,
    "pm2.5_atm": 0.0,
    "pm2.5_atm_a": 0.0,
    "pm2.5_atm_b": 0.0,
    "pm2.5_cf_1": 0.0,
    "pm2.5_cf_1_a": 0.0,
    "pm2.5_cf_1_b": 0.0,
    "pm2.5_10minute": 0.0,
    "pm2.5_10minute_a": 0.0,
    "pm2.5_10minute_b": 0.0,
    "pm2.5_30minute": 0.0,
    "pm2.5_30minute_a": 0.0,
    "pm2.5_30minute_b": 0.0,
    "pm2.5_60minute": 0.0,
    "pm2.5_60minute_a": 0.0,
    "pm2.5_60minute_b": 0.0,
    "pm2.5_6hour": 0.0,
    "pm2.5_6hour_a": 0.0,
    "pm2.5_6hour_b": 0.0,
    "pm2.5_24hour": 0.0,
    "pm2.5_24hour_a": 0.0,
    "pm2.5_24hour_b": 0.0,
    "pm2.5_1week": 0.0,
    "pm2.5_1week_a": 0.0,
    "pm2.5_1week_b": 0.0,
    "pm10.0": 0.0,
    "pm10.0_a": 0.0,
    "pm10.0_b": 0.0,
    "pm10.0_atm": 0.0,
    "pm10.0_atm_a": 0.0,
    "pm10.0_atm_b": 0.0,
    "pm10.0_cf_1": 0.0,
    "pm10.0_cf_1_a": 0.0,
    "pm10.0_cf_1_b": 0.0,
    "0.3_um_count": 0.0,
    "0.3_um_count_a": 0.0,
    "0.3_um_count_b": 0.0,
    "0.5_um_count": 0.0,
    "0.5_um_count_a": 0.0,
    "0.5_um_count_b": 0.0,
    "1.0_um_count": 0.0,
    "1.0_um_count_a": 0.0,
    "1.0_um_count_b": 0.0,
    "2.5_um_count": 0.0,
    "2.5_um_count_a": 0.0,
    "2.5_um_count_b": 0.0,
    "5.0_um_count": 0.0,
    "5.0_um_count_a": 0.0,
    "5.0_um_count_b": 0.0,
    "10.0_um_count": 0.0,
    "10.0_um_count_a": 0.0,
    "10.0_um_count_b": 0.0,
    "primary_id_a": 0,
    "primary_key_a": "",
    "secondary_id_a": 0,
    "secondary_key_a": "",
    "primary_id_b": 0,
    "primary_key_b": "",
    "secondary_id_b": 0,
    "secondary_key_b": "",
}

EXPECTED_FILE_CONTENTS_1 = {
    "data_time_stamp": 1663733772,
    "sensor_index": 53,
    "last_modified": 1520025982,
    "date_created": 1454548891,
    "last_seen": 1663733769,
    "private": 0,
    "is_owner": 0,
    "name": "Lakeshore",
    "icon": 0,
    "location_type": 0,
    "model": "UNKNOWN",
    "hardware": "1.0+1M+PMSX003-O",
    "led_brightness": 25,
    "firmware_version": "6.06a",
    "rssi": -33,
    "uptime": 7567,
    "pa_latency": 336,
    "memory": 15640,
    "position_rating": 5,
    "latitude": 40.246742,
    "longitude": -111.7048,
    "channel_state": 1,
    "channel_flags": 0,
    "channel_flags_manual": 0,
    "channel_flags_auto": 0,
    "confidence": 30,
    "analog_input": 0.0,
    "pm1.0": 0.0,
    "pm1.0_a": 0.0,
    "pm2.5": 0.0,
    "pm2.5_a": 0.0,
    "pm2.5_alt": 1.4,
    "pm2.5_alt_a": 1.4,
    "pm10.0": 0.0,
    "pm10.0_a": 0.0,
    "scattering_coefficient": 14.9,
    "scattering_coefficient_a": 14.9,
    "deciviews": 10.2,
    "deciviews_a": 10.2,
    "visual_range": 140.1,
    "visual_range_a": 140.1,
    "0.3_um_count": 991,
    "0.3_um_count_a": 991,
    "0.5_um_count": 64,
    "0.5_um_count_a": 64,
    "1.0_um_count": 3,
    "1.0_um_count_a": 3,
    "2.5_um_count": 0,
    "2.5_um_count_a": 0,
    "5.0_um_count": 0,
    "5.0_um_count_a": 0,
    "10.0_um_count": 0,
    "10.0_um_count_a": 0,
    "pm1.0_cf_1": 0.0,
    "pm1.0_cf_1_a": 0.0,
    "pm1.0_atm": 0.0,
    "pm1.0_atm_a": 0.0,
    "pm2.5_atm": 0.0,
    "pm2.5_atm_a": 0.0,
    "pm2.5_cf_1": 0.0,
    "pm2.5_cf_1_a": 0.0,
    "pm10.0_atm": 0.0,
    "pm10.0_atm_a": 0.0,
    "pm10.0_cf_1": 0.0,
    "pm10.0_cf_1_a": 0.0,
    "primary_id_a": 84144,
    "primary_key_a": "DYBYPI2LSK4QGFNM",
    "primary_id_b": 725391,
    "primary_key_b": "DGNHAFD7NZV9H2RZ",
    "secondary_id_a": 84145,
    "secondary_key_a": "ITY12CRN3H8KPBJY",
    "secondary_id_b": 725392,
    "secondary_key_b": "EB6SJL8KOR7K7WCA",
    "stats_pm2.5": 0.0,
    "pm2.5_10minute": 0.0,
    "pm2.5_30minute": 0.0,
    "pm2.5_60minute": 0.0,
    "pm2.5_6hour": 0.0,
    "pm2.5_24hour": 0.2,
    "pm2.5_1week": 1.5,
    "pm2.5_time_stamp": 1663733769,
    "pm2.5_10minute_a": 0.0,
    "pm2.5_30minute_a": 0.0,
    "pm2.5_60minute_a": 0.0,
    "pm2.5_6hour_a": 0.0,
    "pm2.5_24hour_a": 0.2,
    "pm2.5_1week_a": 1.5,
    "time_stamp_a": 1663733769,
}
EXPECTED_FILE_CONTENTS_2 = {
    "data_time_stamp": 1676262962,
    "sensor_index": 77,
    "last_modified": 1575074907,
    "date_created": 1456896339,
    "last_seen": 1676262862,
    "private": 0,
    "is_owner": 0,
    "name": "Sunnyside",
    "icon": 0,
    "location_type": 0,
    "model": "PA-I",
    "hardware": "2.0+1M+PMSX003-A",
    "led_brightness": 25,
    "firmware_version": "6.06b",
    "rssi": -61,
    "uptime": 12824,
    "pa_latency": 328,
    "memory": 16656,
    "position_rating": 5,
    "latitude": 40.750816,
    "longitude": -111.82529,
    "channel_state": 1,
    "channel_flags": 0,
    "channel_flags_manual": 0,
    "channel_flags_auto": 0,
    "confidence": 30,
    "analog_input": 0.01,
    "pm1.0": 43.6,
    "pm1.0_a": 43.6,
    "pm2.5": 57.7,
    "pm2.5_a": 57.7,
    "pm2.5_alt": 35.2,
    "pm2.5_alt_a": 35.2,
    "pm10.0": 73.3,
    "pm10.0_a": 73.3,
    "scattering_coefficient": 241.1,
    "scattering_coefficient_a": 241.1,
    "deciviews": 34.0,
    "deciviews_a": 34.0,
    "visual_range": 13.0,
    "visual_range_a": 13.0,
    "0.3_um_count": 16072,
    "0.3_um_count_a": 16072,
    "0.5_um_count": 2507,
    "0.5_um_count_a": 2507,
    "1.0_um_count": 177,
    "1.0_um_count_a": 177,
    "2.5_um_count": 18,
    "2.5_um_count_a": 18,
    "5.0_um_count": 6,
    "5.0_um_count_a": 6,
    "10.0_um_count": 2,
    "10.0_um_count_a": 2,
    "pm1.0_cf_1": 61.0,
    "pm1.0_cf_1_a": 60.96,
    "pm1.0_atm": 43.6,
    "pm1.0_atm_a": 43.61,
    "pm2.5_atm": 57.7,
    "pm2.5_atm_a": 57.74,
    "pm2.5_cf_1": 71.6,
    "pm2.5_cf_1_a": 71.59,
    "pm10.0_atm": 73.3,
    "pm10.0_atm_a": 73.28,
    "pm10.0_cf_1": 81.6,
    "pm10.0_cf_1_a": 81.55,
    "primary_id_a": 92577,
    "primary_key_a": "8FBX16XKWTHHXMSP",
    "primary_id_b": 725363,
    "primary_key_b": "YWFLDV8KI4KHR6K6",
    "secondary_id_a": 92578,
    "secondary_key_a": "QX6J1413BUOIWJF0",
    "secondary_id_b": 725364,
    "secondary_key_b": "RGGZKX2J6N4YUYYA",
    "stats_pm2.5": 57.7,
    "pm2.5_10minute": 77.9,
    "pm2.5_30minute": 73.4,
    "pm2.5_60minute": 67.5,
    "pm2.5_6hour": 56.7,
    "pm2.5_24hour": 45.1,
    "pm2.5_1week": 41.5,
    "pm2.5_time_stamp": 1676262862,
    "pm2.5_10minute_a": 77.9,
    "pm2.5_30minute_a": 73.4,
    "pm2.5_60minute_a": 67.5,
    "pm2.5_6hour_a": 56.7,
    "pm2.5_24hour_a": 45.1,
    "pm2.5_1week_a": 41.5,
    "time_stamp_a": 1676262862,
}
EXPECTED_FILE_CONTENTS_3 = {
    "data_time_stamp": 1695569064,
    "sensor_index": 163965,
    "last_modified": 1664215336,
    "date_created": 1663784441,
    "last_seen": 1695568955,
    "private": 0,
    "is_owner": 0,
    "name": "carlkidcrypto-purpleair2",
    "icon": 0,
    "location_type": 1,
    "model": "PA-I",
    "hardware": "2.0+BME280+PMSX003-A",
    "led_brightness": 100,
    "firmware_version": "7.02",
    "rssi": -75,
    "uptime": 69901,
    "pa_latency": 943,
    "memory": 15944,
    "position_rating": 5,
    "latitude": 46.74709,
    "longitude": -116.998924,
    "altitude": 2647,
    "channel_state": 1,
    "channel_flags": 0,
    "channel_flags_manual": 0,
    "channel_flags_auto": 0,
    "confidence": 30,
    "humidity": 31,
    "humidity_a": 31,
    "temperature": 79,
    "temperature_a": 79,
    "pressure": 923.43,
    "pressure_a": 923.43,
    "analog_input": 0.0,
    "pm1.0": 2.6,
    "pm1.0_a": 2.6,
    "pm2.5": 4.4,
    "pm2.5_a": 4.4,
    "pm2.5_alt": 3.4,
    "pm2.5_alt_a": 3.4,
    "pm10.0": 4.4,
    "pm10.0_a": 4.4,
    "scattering_coefficient": 10.4,
    "scattering_coefficient_a": 10.4,
    "deciviews": 8.1,
    "deciviews_a": 8.1,
    "visual_range": 173.8,
    "visual_range_a": 173.8,
    "0.3_um_count": 691,
    "0.3_um_count_a": 691,
    "0.5_um_count": 178,
    "0.5_um_count_a": 178,
    "1.0_um_count": 35,
    "1.0_um_count_a": 35,
    "2.5_um_count": 0,
    "2.5_um_count_a": 0,
    "5.0_um_count": 0,
    "5.0_um_count_a": 0,
    "10.0_um_count": 0,
    "10.0_um_count_a": 0,
    "pm1.0_cf_1": 2.6,
    "pm1.0_cf_1_a": 2.61,
    "pm1.0_atm": 2.6,
    "pm1.0_atm_a": 2.61,
    "pm2.5_atm": 4.4,
    "pm2.5_atm_a": 4.35,
    "pm2.5_cf_1": 4.4,
    "pm2.5_cf_1_a": 4.35,
    "pm10.0_atm": 4.4,
    "pm10.0_atm_a": 4.35,
    "pm10.0_cf_1": 4.4,
    "pm10.0_cf_1_a": 4.35,
    "primary_id_a": 1868567,
    "primary_key_a": "3XJ73Z60EX66XSHH",
    "primary_id_b": 1868571,
    "primary_key_b": "4TZ413W55H4ZCXMB",
    "secondary_id_a": 1868569,
    "secondary_key_a": "H8X58IEXEOBAPMQY",
    "secondary_id_b": 1868573,
    "secondary_key_b": "TWNBKVZZDWFMWSPV",
    "stats_pm2.5": 4.4,
    "pm2.5_10minute": 4.2,
    "pm2.5_30minute": 4.2,
    "pm2.5_60minute": 4.1,
    "pm2.5_6hour": 4.2,
    "pm2.5_24hour": 2.5,
    "pm2.5_1week": 3.5,
    "pm2.5_time_stamp": 1695568955,
    "pm2.5_10minute_a": 4.2,
    "pm2.5_30minute_a": 4.2,
    "pm2.5_60minute_a": 4.1,
    "pm2.5_6hour_a": 4.2,
    "pm2.5_24hour_a": 2.5,
    "pm2.5_1week_a": 3.5,
    "time_stamp_a": 1695568955,
}
EXPECTED_FILE_CONTENTS_4 = {
    "data_time_stamp": 1658588700,
    "sensor_index": 14867,
    "last_modified": 1561137879,
    "date_created": 1536015895,
    "last_seen": 1658588620,
    "private": 0,
    "is_owner": 0,
    "name": "Kangerlussuaq, Greenland - University of Michigan Climate and Space",
    "icon": 0,
    "location_type": 0,
    "model": "PA-II",
    "hardware": "2.0+BME280+PMSX003-B+PMSX003-A",
    "led_brightness": 35,
    "firmware_version": "7.00",
    "rssi": -60,
    "uptime": 40557,
    "pa_latency": 442,
    "memory": 15672,
    "position_rating": 0,
    "latitude": 66.996,
    "longitude": -50.6215,
    "altitude": 971,
    "channel_state": 3,
    "channel_flags": 0,
    "channel_flags_manual": 0,
    "channel_flags_auto": 0,
    "confidence": 100,
    "confidence_auto": 100,
    "confidence_manual": 100,
    "humidity": 55,
    "humidity_a": 55,
    "temperature": 60,
    "temperature_a": 60,
    "pressure": 982.39,
    "pressure_a": 982.39,
    "analog_input": 0.02,
    "pm1.0": 1.1,
    "pm1.0_a": 1.0,
    "pm1.0_b": 1.2,
    "pm2.5": 1.7,
    "pm2.5_a": 1.1,
    "pm2.5_b": 2.2,
    "pm2.5_alt": 1.3,
    "pm2.5_alt_a": 1.0,
    "pm2.5_alt_b": 1.7,
    "pm10.0": 1.8,
    "pm10.0_a": 1.3,
    "pm10.0_b": 2.3,
    "scattering_coefficient": 4.6,
    "scattering_coefficient_a": 4.0,
    "scattering_coefficient_b": 5.2,
    "deciviews": 4.4,
    "deciviews_a": 3.9,
    "deciviews_b": 4.8,
    "visual_range": 252.1,
    "visual_range_a": 263.4,
    "visual_range_b": 240.9,
    "0.3_um_count": 305,
    "0.3_um_count_a": 267,
    "0.3_um_count_b": 344,
    "0.5_um_count": 97,
    "0.5_um_count_a": 84,
    "0.5_um_count_b": 110,
    "1.0_um_count": 11,
    "1.0_um_count_a": 7,
    "1.0_um_count_b": 16,
    "2.5_um_count": 0,
    "2.5_um_count_a": 0,
    "2.5_um_count_b": 1,
    "5.0_um_count": 0,
    "5.0_um_count_a": 0,
    "5.0_um_count_b": 0,
    "10.0_um_count": 0,
    "10.0_um_count_a": 0,
    "10.0_um_count_b": 0,
    "pm1.0_cf_1": 1.1,
    "pm1.0_cf_1_a": 0.95,
    "pm1.0_cf_1_b": 1.16,
    "pm1.0_atm": 1.1,
    "pm1.0_atm_a": 0.95,
    "pm1.0_atm_b": 1.16,
    "pm2.5_atm": 1.7,
    "pm2.5_atm_a": 1.08,
    "pm2.5_atm_b": 2.22,
    "pm2.5_cf_1": 1.7,
    "pm2.5_cf_1_a": 1.08,
    "pm2.5_cf_1_b": 2.22,
    "pm10.0_atm": 1.8,
    "pm10.0_atm_a": 1.28,
    "pm10.0_atm_b": 2.31,
    "pm10.0_cf_1": 1.8,
    "pm10.0_cf_1_a": 1.28,
    "pm10.0_cf_1_b": 2.31,
    "primary_id_a": 568591,
    "primary_key_a": "FD9JF1Q2HM8Z1ZER",
    "primary_id_b": 568593,
    "primary_key_b": "CNQTXQCBZJ3F762X",
    "secondary_id_a": 568592,
    "secondary_key_a": "PJWR908B6ONVFZGF",
    "secondary_id_b": 568594,
    "secondary_key_b": "HL3MVK8ZU7D0BZRN",
    "stats_pm2.5": 1.7,
    "pm2.5_10minute": 2.2,
    "pm2.5_30minute": 2.2,
    "pm2.5_60minute": 2.2,
    "pm2.5_6hour": 2.3,
    "pm2.5_24hour": 2.0,
    "pm2.5_1week": 0.8,
    "pm2.5_time_stamp": 1658588620,
    "pm2.5_10minute_a": 2.0,
    "pm2.5_30minute_a": 2.1,
    "pm2.5_60minute_a": 2.1,
    "pm2.5_6hour_a": 2.2,
    "pm2.5_24hour_a": 1.9,
    "pm2.5_1week_a": 0.7,
    "time_stamp_a": 1658588620,
    "pm2.5_10minute_b": 2.3,
    "pm2.5_30minute_b": 2.3,
    "pm2.5_60minute_b": 2.3,
    "pm2.5_6hour_b": 2.4,
    "pm2.5_24hour_b": 2.1,
    "pm2.5_1week_b": 0.8,
    "time_stamp_b": 1658588620,
}
EXPECTED_FILE_CONTENTS_5 = {
    "data_time_stamp": 1676263264,
    "sensor_index": 137236,
    "last_modified": 1666627408,
    "date_created": 1636572956,
    "last_seen": 1675087378,
    "private": 0,
    "is_owner": 0,
    "name": "Idaea_2",
    "icon": 0,
    "location_type": 0,
    "model": "PA-I-SD",
    "hardware": "2.0+OPENLOG+31037 MB+DS3231+BME280+PMSX003-A",
    "led_brightness": 35,
    "firmware_version": "7.02",
    "rssi": -45,
    "uptime": 4,
    "memory": 16728,
    "position_rating": 5,
    "latitude": 41.38754,
    "longitude": 2.1154,
    "altitude": 261,
    "channel_state": 3,
    "channel_flags": 1,
    "channel_flags_manual": 0,
    "channel_flags_auto": 1,
    "confidence": 0,
    "confidence_auto": 0,
    "confidence_manual": 0,
    "humidity": 22,
    "humidity_a": 22,
    "temperature": 75,
    "temperature_a": 75,
    "pressure": 1013.55,
    "pressure_a": 1013.55,
    "analog_input": 0.06,
    "pm1.0_a": 2020.0,
    "pm2.5_a": 2020.0,
    "pm2.5_alt_a": 0.1,
    "pm10.0_a": 2020.0,
    "scattering_coefficient_a": 0.5,
    "deciviews_a": 0.6,
    "visual_range_a": 368.8,
    "0.3_um_count_a": 32,
    "0.5_um_count_a": 10,
    "1.0_um_count_a": 0,
    "2.5_um_count_a": 0,
    "5.0_um_count_a": 0,
    "10.0_um_count_a": 0,
    "pm1.0_cf_1_a": 3030.34,
    "pm1.0_atm_a": 2020.0,
    "pm2.5_atm_a": 2020.0,
    "pm2.5_cf_1_a": 3030.34,
    "pm10.0_atm_a": 2020.0,
    "pm10.0_cf_1_a": 3030.34,
    "primary_id_a": 1566363,
    "primary_key_a": "WC9GBNIBV6EA19ZJ",
    "primary_id_b": 1566365,
    "primary_key_b": "HVKTP5FAY62ZQGR6",
    "secondary_id_a": 1566364,
    "secondary_key_a": "63FXIGMH8F7JLETX",
    "secondary_id_b": 1566366,
    "secondary_key_b": "8BZC8PVWJMB5CG20",
    "stats_pm2.5": None,
    "pm2.5_10minute": 11.3,
    "pm2.5_30minute": 11.6,
    "pm2.5_60minute": 12.1,
    "pm2.5_6hour": 7.8,
    "pm2.5_24hour": 4.7,
    "pm2.5_1week": 6.2,
    "pm2.5_time_stamp": 1675087378,
    "pm2.5_10minute_a": 10.5,
    "pm2.5_30minute_a": 11.3,
    "pm2.5_60minute_a": 12.2,
    "pm2.5_6hour_a": 8.2,
    "pm2.5_24hour_a": 4.9,
    "pm2.5_1week_a": 6.3,
    "time_stamp_a": 1675087378,
    "pm2.5_b": None,
    "pm2.5_10minute_b": 11.3,
    "pm2.5_30minute_b": 11.6,
    "pm2.5_60minute_b": 12.1,
    "pm2.5_6hour_b": 7.8,
    "pm2.5_24hour_b": 4.7,
    "pm2.5_1week_b": 6.2,
    "time_stamp_b": 1675087378,
}
EXPECTED_FILE_CONTENTS_6 = {
    "data_time_stamp": 1676263122,
    "sensor_index": 131190,
    "last_modified": 1646085907,
    "date_created": 1633034575,
    "last_seen": 1676263011,
    "private": 0,
    "is_owner": 0,
    "name": "Lanterns at Rock Creek",
    "icon": 0,
    "location_type": 0,
    "model": "PA-II-SD",
    "hardware": "2.0+OPENLOG+31037 MB+DS3231+BME280+PMSX003-B+PMSX003-A",
    "led_brightness": 35,
    "firmware_version": "7.02",
    "rssi": -69,
    "uptime": 66182,
    "pa_latency": 239,
    "memory": 16240,
    "position_rating": 5,
    "latitude": 39.94589,
    "longitude": -105.14925,
    "altitude": 5471,
    "channel_state": 3,
    "channel_flags": 0,
    "channel_flags_manual": 0,
    "channel_flags_auto": 0,
    "confidence": 100,
    "confidence_auto": 100,
    "confidence_manual": 100,
    "humidity": 38,
    "humidity_a": 38,
    "temperature": 41,
    "temperature_a": 41,
    "pressure": 832.34,
    "pressure_a": 832.34,
    "analog_input": 0.0,
    "pm1.0": 0.0,
    "pm1.0_a": 0.0,
    "pm1.0_b": 0.0,
    "pm2.5": 1.8,
    "pm2.5_a": 1.9,
    "pm2.5_b": 1.6,
    "pm2.5_alt": 1.3,
    "pm2.5_alt_a": 1.4,
    "pm2.5_alt_b": 1.2,
    "pm10.0": 2.1,
    "pm10.0_a": 2.6,
    "pm10.0_b": 1.6,
    "0.3_um_count": 228,
    "0.3_um_count_a": 240,
    "0.3_um_count_b": 216,
    "0.5_um_count": 219,
    "0.5_um_count_a": 232,
    "0.5_um_count_b": 206,
    "1.0_um_count": 1,
    "1.0_um_count_a": 1,
    "1.0_um_count_b": 1,
    "2.5_um_count": 0,
    "2.5_um_count_a": 0,
    "2.5_um_count_b": 0,
    "5.0_um_count": 0,
    "5.0_um_count_a": 0,
    "5.0_um_count_b": 0,
    "10.0_um_count": 0,
    "10.0_um_count_a": 0,
    "10.0_um_count_b": 0,
    "pm1.0_cf_1": 0.0,
    "pm1.0_cf_1_a": 0.0,
    "pm1.0_cf_1_b": 0.0,
    "pm1.0_atm": 0.0,
    "pm1.0_atm_a": 0.0,
    "pm1.0_atm_b": 0.0,
    "pm2.5_atm": 1.8,
    "pm2.5_atm_a": 1.91,
    "pm2.5_atm_b": 1.64,
    "pm2.5_cf_1": 1.8,
    "pm2.5_cf_1_a": 1.91,
    "pm2.5_cf_1_b": 1.64,
    "pm10.0_atm": 2.1,
    "pm10.0_atm_a": 2.64,
    "pm10.0_atm_b": 1.64,
    "pm10.0_cf_1": 2.1,
    "pm10.0_cf_1_a": 2.64,
    "pm10.0_cf_1_b": 1.64,
    "primary_id_a": 1523479,
    "primary_key_a": "XJD1ZRIXS13NQI06",
    "primary_id_b": 1664817,
    "primary_key_b": "LTKCX2OQJVSON7RS",
    "secondary_id_a": 1523480,
    "secondary_key_a": "SEV906OKLV2D1Q3S",
    "secondary_id_b": 1664818,
    "secondary_key_b": "G3OJQEJG0DRMLRZV",
    "stats_pm2.5": 1.8,
    "pm2.5_10minute": 1.9,
    "pm2.5_30minute": 1.6,
    "pm2.5_60minute": 1.4,
    "pm2.5_6hour": 1.5,
    "pm2.5_24hour": 1.5,
    "pm2.5_1week": 3.2,
    "pm2.5_time_stamp": 1676263011,
    "pm2.5_10minute_a": 2.1,
    "pm2.5_30minute_a": 1.9,
    "pm2.5_60minute_a": 1.6,
    "pm2.5_6hour_a": 1.6,
    "pm2.5_24hour_a": 1.6,
    "pm2.5_1week_a": 3.5,
    "time_stamp_a": 1676263011,
    "pm2.5_10minute_b": 1.7,
    "pm2.5_30minute_b": 1.4,
    "pm2.5_60minute_b": 1.2,
    "pm2.5_6hour_b": 1.3,
    "pm2.5_24hour_b": 1.3,
    "pm2.5_1week_b": 2.9,
    "time_stamp_b": 1676263011,
}
EXPECTED_FILE_CONTENTS_7 = {
    "data_time_stamp": 1676263211,
    "sensor_index": 146330,
    "last_modified": 1654484887,
    "date_created": 1648763897,
    "last_seen": 1676263160,
    "private": 0,
    "is_owner": 0,
    "name": "indoor",
    "icon": 0,
    "location_type": 1,
    "model": "PA-I-LED",
    "hardware": "3.0+BME280+BME680+PMSX003-A",
    "led_brightness": 20,
    "firmware_version": "7.02",
    "rssi": -67,
    "uptime": 58166,
    "pa_latency": 278,
    "memory": 16568,
    "position_rating": 1,
    "latitude": 40.077816,
    "longitude": -111.57601,
    "altitude": 5154,
    "channel_state": 1,
    "channel_flags": 0,
    "channel_flags_manual": 0,
    "channel_flags_auto": 0,
    "confidence": 30,
    "humidity": 17,
    "humidity_a": 18,
    "humidity_b": 17,
    "temperature": 82,
    "temperature_a": 82,
    "temperature_b": 83,
    "pressure": 857.92,
    "pressure_a": 858.0,
    "pressure_b": 857.85,
    "voc": 246.8,
    "voc_b": 246.75,
    "analog_input": 0.58,
    "pm1.0": 33.6,
    "pm1.0_a": 33.6,
    "pm2.5": 55.0,
    "pm2.5_a": 55.0,
    "pm2.5_alt": 31.8,
    "pm2.5_alt_a": 31.8,
    "pm10.0": 59.5,
    "pm10.0_a": 59.5,
    "scattering_coefficient": 90.8,
    "scattering_coefficient_a": 90.8,
    "deciviews": 24.8,
    "deciviews_a": 24.8,
    "visual_range": 32.8,
    "visual_range_a": 32.8,
    "0.3_um_count": 6054,
    "0.3_um_count_a": 6054,
    "0.5_um_count": 1715,
    "0.5_um_count_a": 1715,
    "1.0_um_count": 349,
    "1.0_um_count_a": 349,
    "2.5_um_count": 23,
    "2.5_um_count_a": 23,
    "5.0_um_count": 5,
    "5.0_um_count_a": 5,
    "10.0_um_count": 1,
    "10.0_um_count_a": 1,
    "pm1.0_cf_1": 33.6,
    "pm1.0_cf_1_a": 33.59,
    "pm1.0_atm": 27.4,
    "pm1.0_atm_a": 27.43,
    "pm2.5_atm": 43.5,
    "pm2.5_atm_a": 43.51,
    "pm2.5_cf_1": 55.0,
    "pm2.5_cf_1_a": 54.97,
    "pm10.0_atm": 53.7,
    "pm10.0_atm_a": 53.68,
    "pm10.0_cf_1": 59.5,
    "pm10.0_cf_1_a": 59.49,
    "primary_id_a": 1692079,
    "primary_key_a": "R27RO2JSMWZKDIVW",
    "primary_id_b": 1692081,
    "primary_key_b": "RE0WK8H3GM79STTL",
    "secondary_id_a": 1692080,
    "secondary_key_a": "2QQFR5Q50EQC5LWK",
    "secondary_id_b": 1692082,
    "secondary_key_b": "DQS4JXPQYN7O6TK5",
    "stats_pm2.5": 55.0,
    "pm2.5_10minute": 59.3,
    "pm2.5_30minute": 74.7,
    "pm2.5_60minute": 102.8,
    "pm2.5_6hour": 103.9,
    "pm2.5_24hour": 41.7,
    "pm2.5_1week": 8.5,
    "pm2.5_time_stamp": 1676263160,
    "pm2.5_10minute_a": 59.3,
    "pm2.5_30minute_a": 74.7,
    "pm2.5_60minute_a": 102.8,
    "pm2.5_6hour_a": 103.9,
    "pm2.5_24hour_a": 41.7,
    "pm2.5_1week_a": 8.5,
    "time_stamp_a": 1676263160,
}
EXPECTED_FILE_CONTENTS_8 = {
    "data_time_stamp": 1695569365,
    "sensor_index": 123456,
    "last_modified": 1656033161,
    "date_created": 1653666655,
    "last_seen": 1695569319,
    "private": 0,
    "is_owner": 0,
    "name": "A NAME GOES HERE",
    "icon": 0,
    "location_type": 0,
    "model": "PA-II-FLEX",
    "hardware": "3.0+OPENLOG+31037 MB+DS3231+BME280+BME68X+PMSX003-A+PMSX003-B",
    "led_brightness": 100,
    "firmware_version": "7.04",
    "rssi": -62,
    "uptime": 137,
    "pa_latency": 732,
    "memory": 5672,
    "position_rating": 5,
    "latitude": 123.123,
    "longitude": -123.123,
    "altitude": 123,
    "channel_state": 3,
    "channel_flags": 0,
    "channel_flags_manual": 0,
    "channel_flags_auto": 0,
    "confidence": 100,
    "confidence_auto": 100,
    "confidence_manual": 100,
    "humidity": 46,
    "humidity_a": 44,
    "humidity_b": 49,
    "temperature": 63,
    "temperature_a": 64,
    "temperature_b": 62,
    "pressure": 924.6,
    "pressure_a": 925.33,
    "pressure_b": 923.87,
    "voc": 598.9,
    "voc_b": 598.89,
    "analog_input": 0.06,
    "pm1.0": 23.7,
    "pm1.0_a": 23.3,
    "pm1.0_b": 24.0,
    "pm2.5": 34.7,
    "pm2.5_a": 35.0,
    "pm2.5_b": 34.5,
    "pm2.5_alt": 22.1,
    "pm2.5_alt_a": 23.2,
    "pm2.5_alt_b": 21.1,
    "pm10.0": 44.4,
    "pm10.0_a": 46.7,
    "pm10.0_b": 42.0,
    "scattering_coefficient": 70.1,
    "scattering_coefficient_a": 70.1,
    "scattering_coefficient_b": 70.1,
    "deciviews": 22.4,
    "deciviews_a": 22.4,
    "deciviews_b": 22.4,
    "visual_range": 41.5,
    "visual_range_a": 41.5,
    "visual_range_b": 41.4,
    "0.3_um_count": 4671,
    "0.3_um_count_a": 4671,
    "0.3_um_count_b": 4672,
    "0.5_um_count": 1330,
    "0.5_um_count_a": 1330,
    "0.5_um_count_b": 1330,
    "1.0_um_count": 230,
    "1.0_um_count_a": 253,
    "1.0_um_count_b": 208,
    "2.5_um_count": 21,
    "2.5_um_count_a": 25,
    "2.5_um_count_b": 18,
    "5.0_um_count": 9,
    "5.0_um_count_a": 11,
    "5.0_um_count_b": 7,
    "10.0_um_count": 4,
    "10.0_um_count_a": 9,
    "10.0_um_count_b": 0,
    "pm1.0_cf_1": 27.0,
    "pm1.0_cf_1_a": 26.48,
    "pm1.0_cf_1_b": 27.53,
    "pm1.0_atm": 23.7,
    "pm1.0_atm_a": 23.34,
    "pm1.0_atm_b": 23.98,
    "pm2.5_atm": 34.7,
    "pm2.5_atm_a": 34.95,
    "pm2.5_atm_b": 34.46,
    "pm2.5_cf_1": 38.1,
    "pm2.5_cf_1_a": 38.61,
    "pm2.5_cf_1_b": 37.56,
    "pm10.0_atm": 44.4,
    "pm10.0_atm_a": 46.68,
    "pm10.0_atm_b": 42.05,
    "pm10.0_cf_1": 45.2,
    "pm10.0_cf_1_a": 48.2,
    "pm10.0_cf_1_b": 42.2,
    "primary_id_a": 1750199,
    "primary_key_a": "M9M66UHOIS8YIAGH",
    "primary_id_b": 1750201,
    "primary_key_b": "D9M2N0ZO81PTA210",
    "secondary_id_a": 1750200,
    "secondary_key_a": "O4T8GWNDUROR5EP6",
    "secondary_id_b": 1750202,
    "secondary_key_b": "2YTJ6VA9HS3T8K07",
    "stats_pm2.5": 34.7,
    "pm2.5_10minute": 31.6,
    "pm2.5_30minute": 32.2,
    "pm2.5_60minute": 32.5,
    "pm2.5_6hour": 22.2,
    "pm2.5_24hour": 13.6,
    "pm2.5_1week": 9.9,
    "pm2.5_time_stamp": 1695569319,
    "pm2.5_10minute_a": 32.0,
    "pm2.5_30minute_a": 32.5,
    "pm2.5_60minute_a": 32.8,
    "pm2.5_6hour_a": 22.3,
    "pm2.5_24hour_a": 13.6,
    "pm2.5_1week_a": 9.8,
    "time_stamp_a": 1695569319,
    "pm2.5_10minute_b": 31.3,
    "pm2.5_30minute_b": 31.8,
    "pm2.5_60minute_b": 32.2,
    "pm2.5_6hour_b": 22.1,
    "pm2.5_24hour_b": 13.5,
    "pm2.5_1week_b": 9.9,
    "time_stamp_b": 1695569319,
}
