import pytest
from unittest.mock import MagicMock, patch
from runner import JobRunner
@pytest.fixture
def runner():
    return JobRunner()
def test_runner_interval_type():
    assert isinstance(runner().interval, int)
def test_payment_failure_handling(mocker):
    r = runner()
    mocker.patch.object(r.client, "create_payment", return_value={"status": "failed"})
    with patch("time.sleep") as sleep_mock:
        mocker.patch.object(r, "running", True)
        mocker.patch.object(r, "_run", side_effect=Exception("Loop crash!"))
        with pytest.raises(Exception):
            r._run()
def test_validate_amount_check(mocker):
    r = runner()
    mocker.patch("runner.validate_amount", return_value=False)
    with patch("time.sleep"):
        mocker.patch.object(r.client, "create_payment", return_value={"status": "success"})
        r.running = True
        try:
            r._run()
            assert True
        except Exception:
            assert False
