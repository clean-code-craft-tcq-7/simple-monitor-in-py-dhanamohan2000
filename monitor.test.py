import unittest
from unittest.mock import patch
from monitor import (
    vitals_ok, 
    is_temperature_critical, 
    is_pulse_rate_critical, 
    is_spo2_critical
)


class MonitorTest(unittest.TestCase):
    # Test pure functions - minimal boundary tests
    def test_temperature_critical(self):
        self.assertTrue(is_temperature_critical(103))   # Above upper limit
        self.assertTrue(is_temperature_critical(94))    # Below lower limit
        self.assertFalse(is_temperature_critical(98.6)) # Normal
    
    def test_pulse_rate_critical(self):
        self.assertTrue(is_pulse_rate_critical(101))    # Above upper limit
        self.assertTrue(is_pulse_rate_critical(59))     # Below lower limit
        self.assertFalse(is_pulse_rate_critical(70))    # Normal
    
    def test_spo2_critical(self):
        self.assertTrue(is_spo2_critical(89))           # Below limit
        self.assertFalse(is_spo2_critical(95))          # Normal
    
    # Test vitals_ok with mocked I/O to avoid actual alerts
    @patch('monitor.flash_alert')
    @patch('builtins.print')
    def test_vitals_ok_all_normal(self, mock_print, mock_flash):
        self.assertTrue(vitals_ok(98.6, 70, 95))
        mock_print.assert_not_called()
        mock_flash.assert_not_called()
    
    @patch('monitor.flash_alert')
    @patch('builtins.print')
    def test_vitals_ok_temperature_critical(self, mock_print, mock_flash):
        self.assertFalse(vitals_ok(103, 70, 95))
        mock_print.assert_called_with('Temperature critical!')
    
    @patch('monitor.flash_alert')
    @patch('builtins.print')
    def test_vitals_ok_pulse_critical(self, mock_print, mock_flash):
        self.assertFalse(vitals_ok(98.6, 101, 95))
        mock_print.assert_called_with('Pulse Rate is out of range!')
    
    @patch('monitor.flash_alert')
    @patch('builtins.print')
    def test_vitals_ok_spo2_critical(self, mock_print, mock_flash):
        self.assertFalse(vitals_ok(98.6, 70, 89))
        mock_print.assert_called_with('Oxygen Saturation out of range!')


if __name__ == '__main__':
    unittest.main()
