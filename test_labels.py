from labels import labels
from click.testing import CliRunner
from cvcli import calllabels


def test_lion():
    myLabels = labels("cloud-comp-found-function-bike-rider", "lion.jpg")
    assert type(myLabels) == list
    label1 = myLabels[0]
    assert type(label1) == dict
    assert label1.get("Name") == "Lion"
    assert label1.get("Confidence") >= 0.98


def test_tiger():
    myLabels = labels("cloud-comp-found-function-bike-rider", "tiger.jpg")
    assert type(myLabels) == list
    label1 = myLabels[0]
    assert type(label1) == dict
    assert label1.get("Name") == "Tiger"
    assert label1.get("Confidence") >= 0.98


def test_cvcli():
    runner = CliRunner()
    result = runner.invoke(
        calllabels,
        ["--bucket", "cloud-comp-found-function-bike-rider", "--name", "lion.jpg"],
    )
    assert result.exit_code == 0
    assert "Lion" in result.output
