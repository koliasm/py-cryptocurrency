from unittest import mock
from pytest import mark

from app.main import cryptocurrency_action


@mark.parametrize("rate_prediction,expected_action",
                  [
                      (2, "Buy more cryptocurrency"),
                      (0.5, "Sell all your cryptocurrency"),
                      (1.05, "Do nothing"),
                      (0.95, "Do nothing"),
                  ])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_prediction: mock.Mock,
                               rate_prediction: int | float,
                               expected_action: str) -> None:
    mocked_prediction.return_value = rate_prediction
    assert cryptocurrency_action(1) == expected_action
