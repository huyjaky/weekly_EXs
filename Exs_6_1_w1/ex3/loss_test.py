import unittest
from unittest.mock import patch
import random
import math
from loss import calc_mae, calc_mae, calc_mse, calc_rmse, export_process, create_predict_loss


# Assuming the functions are in a module named `your_module`
# from your_module import export_process, create_predict_loss, calc_mae, calc_mse, calc_rmse

class TestPredictLossFunctions(unittest.TestCase):
    
    @patch('builtins.print')
    def test_export_process(self, mock_print):
        # Testing export_process function with sample inputs
        export_process(predict=5.0, target=5.0, loss_name="MAE", sample=1, loss=0.0)
        mock_print.assert_called_with(
            "loss name: MAE, sample: 1, pred: 5.0, target: 5.0, loss: 0.0"
        )
    
    @patch('random.uniform')
    def test_create_predict_loss(self, mock_random):
        # Mocking random.uniform to return specific values
        mock_random.side_effect = [3.5, 7.2]
        result = create_predict_loss()
        self.assertEqual(result, {"predict": 3.5, "target": 7.2})
    
    @patch('builtins.print')
    @patch('random.uniform')
    def test_calc_mae(self, mock_random, mock_print):
        # Mocking random.uniform to return a series of values
        mock_random.side_effect = [3.0, 7.0, 2.0, 8.0, 1.0, 9.0]
        
        # Calculating MAE with the mocked values
        calc_mae(3)
        
        # Verifying the print calls
        expected_calls = [
            (("loss name: MAE, sample: 0, pred: 3.0, target: 7.0, loss: 4.0",),),
            (("loss name: MAE, sample: 1, pred: 2.0, target: 8.0, loss: 6.0",),),
            (("loss name: MAE, sample: 2, pred: 1.0, target: 9.0, loss: 8.0",),),
            (("final MAE: 6.0",),)
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)
    
    @patch('builtins.print')
    @patch('random.uniform')
    def test_calc_mse(self, mock_random, mock_print):
        # Mocking random.uniform to return a series of values
        mock_random.side_effect = [3.0, 7.0, 2.0, 8.0, 1.0, 9.0]
        
        # Calculating MSE with the mocked values
        calc_mse(3)
        
        # Verifying the print calls
        expected_calls = [
            (("loss name: MSE, sample: 0, pred: 3.0, target: 7.0, loss: 16.0",),),
            (("loss name: MSE, sample: 1, pred: 2.0, target: 8.0, loss: 36.0",),),
            (("loss name: MSE, sample: 2, pred: 1.0, target: 9.0, loss: 64.0",),),
            (("final MSE: 38.666666666666664",),)
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    @patch('random.uniform')
    def test_calc_rmse(self, mock_random, mock_print):
        # Mocking random.uniform to return a series of values
        mock_random.side_effect = [3.0, 7.0, 2.0, 8.0, 1.0, 9.0]
        
        # Calculating RMSE with the mocked values
        calc_rmse(3)
        
        # Verifying the print calls
        expected_calls = [
            (("loss name: MSE, sample: 0, pred: 3.0, target: 7.0, loss: 16.0",),),
            (("loss name: MSE, sample: 1, pred: 2.0, target: 8.0, loss: 36.0",),),
            (("loss name: MSE, sample: 2, pred: 1.0, target: 9.0, loss: 64.0",),),
            (("final RMSE: 6.2182527020592095",),)
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()
