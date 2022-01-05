import pytest
import UI


@pytest.fixture
def app(qtbot):
    test_ui_app = UI.WebServerUI()
    qtbot.addWidget(test_ui_app)

    return test_ui_app





def testPortLabel(app):
    assert app.portLabel.text() == "Port Select:"

def testPortInputOff(app,qtbot):
    qtbot.keyClicks(app.portInput, '8888')
    assert app.portInput.text() == "8888"

def testPortInputOn(app,qtbot):
    qtbot.keyClicks(app.portInput, '8888')
    app.startButton.click()
    qtbot.keyClicks(app.portInput, '7777')
    assert app.portInput.text() == "8888"


def testMaintenanceOff(app):
    app.maintenance.click()
    assert app.maintenance.isChecked() == False


def testMaintenanceOn(app):
    app.startButton.click()
    app.maintenance.click()
    assert app.maintenance.isChecked() == True
    app.maintenance.click()
    assert app.maintenance.isChecked() == False


def testStopOff(app):
    assert app.stopLabel.isVisible() == False

def testStopOn(app,qtbot):
    app.startButton.click()
    app.stopButton.click()
    assert app.stopLabel.styleSheet() == "color : red"


def testStartOff(app):
    assert app.startLabel.isVisible() == False


def testStartOn(app):
    app.startButton.click()
    assert app.startLabel.styleSheet() == "color : green"