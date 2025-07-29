
from time import sleep
import sys


def is_temperature_critical(temperature):
    return temperature > 102 or temperature < 95


def is_pulse_rate_critical(pulse_rate):
    return pulse_rate < 60 or pulse_rate > 100


def is_spo2_critical(spo2):
    return spo2 < 90


def flash_alert():
    for i in range(6):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)


def check_vital_and_alert(vital_value, check_function, alert_message):
    if check_function(vital_value):
        print(alert_message)
        flash_alert()
        return False
    return True


def vitals_ok(temperature, pulseRate, spo2):
    temperature_ok = check_vital_and_alert(
        temperature, is_temperature_critical, 'Temperature critical!'
    )
    pulse_ok = check_vital_and_alert(
        pulseRate, is_pulse_rate_critical, 'Pulse Rate is out of range!'
    )
    spo2_ok = check_vital_and_alert(
        spo2, is_spo2_critical, 'Oxygen Saturation out of range!'
    )
    
    return temperature_ok and pulse_ok and spo2_ok
