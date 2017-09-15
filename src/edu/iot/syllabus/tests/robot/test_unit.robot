# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edu.iot.syllabus -t test_unit.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edu.iot.syllabus.testing.EDU_IOT_SYLLABUS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_unit.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Unit
  Given a logged-in site administrator
    and an add unit form
   When I type 'My Unit' into the title field
    and I submit the form
   Then a unit with the title 'My Unit' has been created

Scenario: As a site administrator I can view a Unit
  Given a logged-in site administrator
    and a unit 'My Unit'
   When I go to the unit view
   Then I can see the unit title 'My Unit'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add unit form
  Go To  ${PLONE_URL}/++add++Unit

a unit 'My Unit'
  Create content  type=Unit  id=my-unit  title=My Unit


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the unit view
  Go To  ${PLONE_URL}/my-unit
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a unit with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the unit title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
