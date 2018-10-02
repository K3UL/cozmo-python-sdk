import cozmo, time

def quick_flash(robot: cozmo.robot.Robot):
    delay = 0.1
    while True:
        robot.set_all_backpack_lights(cozmo.lights.red_light)
        time.sleep(delay)
        robot.set_all_backpack_lights(cozmo.lights.off_light)
        time.sleep(delay)
        robot.set_all_backpack_lights(cozmo.lights.red_light)
        time.sleep(delay)
        robot.set_all_backpack_lights(cozmo.lights.off_light)
        time.sleep(delay)
        robot.set_all_backpack_lights(cozmo.lights.blue_light)
        time.sleep(delay)
        robot.set_all_backpack_lights(cozmo.lights.off_light)
        time.sleep(delay)
        robot.set_all_backpack_lights(cozmo.lights.blue_light)

        time.sleep(delay)
        robot.set_all_backpack_lights(cozmo.lights.off_light)
        time.sleep(delay)


def quint_flash(robot: cozmo.robot.Robot):
    while True:
        robot.set_backpack_lights(cozmo.lights.off_light,
                                  cozmo.lights.blue_light, cozmo.lights.off_light, cozmo.lights.red_light,
                                  cozmo.lights.off_light)
        time.sleep(0.1)
        robot.set_all_backpack_lights(cozmo.lights.off_light)
        time.sleep(0.1)
        robot.set_backpack_lights(cozmo.lights.off_light,
                                  cozmo.lights.blue_light, cozmo.lights.off_light, cozmo.lights.red_light,
                                  cozmo.lights.off_light)
        time.sleep(0.1)
        robot.set_all_backpack_lights(cozmo.lights.off_light)
        time.sleep(1)

def quint_flash_p1_p1(robot: cozmo.robot.Robot):
    while True:
        robot.set_backpack_lights(cozmo.lights.off_light,
                                  cozmo.lights.blue_light, cozmo.lights.off_light, cozmo.lights.red_light,
                                  cozmo.lights.off_light)
        time.sleep(0.1)
        robot.set_all_backpack_lights(cozmo.lights.off_light)
        time.sleep(0.1)
        robot.set_backpack_lights(cozmo.lights.off_light,
                                  cozmo.lights.blue_light, cozmo.lights.off_light, cozmo.lights.red_light,
                                  cozmo.lights.off_light)
        time.sleep(0.1)
        robot.set_all_backpack_lights(cozmo.lights.off_light)
        time.sleep(1)

def quint_flash_p1_p2(robot: cozmo.robot.Robot):
    while True:
        robot.set_backpack_lights(cozmo.lights.red_light,
                                  cozmo.lights.off_light, cozmo.lights.off_light, cozmo.lights.red_light,
                                  cozmo.lights.red_light)
        time.sleep(0.1)
        robot.set_all_backpack_lights(cozmo.lights.off_light)
        time.sleep(0.1)
        robot.set_backpack_lights(cozmo.lights.red_light,
                                  cozmo.lights.off_light, cozmo.lights.off_light, cozmo.lights.red_light,
                                  cozmo.lights.red_light)
        time.sleep(0.3)
        robot.set_all_backpack_lights(cozmo.lights.off_light)
        time.sleep(0.1)

        robot.set_backpack_lights(cozmo.lights.off_light,
                                  cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.off_light,
                                  cozmo.lights.off_light)
        time.sleep(0.1)
        robot.set_all_backpack_lights(cozmo.lights.off_light)
        time.sleep(0.1)
        robot.set_backpack_lights(cozmo.lights.off_light,
                                  cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.off_light,
                                  cozmo.lights.off_light)
        time.sleep(0.3)
        robot.set_all_backpack_lights(cozmo.lights.off_light)
        time.sleep(0.1)

def single_flash_p1_p1(robot: cozmo.robot.Robot):
    while True:
        robot.set_backpack_lights(cozmo.lights.red_light,
                                  cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.red_light,
                                  cozmo.lights.red_light)
        time.sleep(0.150)
        robot.set_all_backpack_lights(cozmo.lights.off_light)
        time.sleep(0.800)

def single_flash_p1_p1(robot: cozmo.robot.Robot):
    while True:
        robot.set_backpack_lights(cozmo.lights.red_light,
                                  cozmo.lights.off_light, cozmo.lights.off_light, cozmo.lights.red_light,
                                  cozmo.lights.red_light)
        time.sleep(0.5)
        robot.set_backpack_lights(cozmo.lights.off_light,
                                  cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.off_light,
                                  cozmo.lights.off_light)
        time.sleep(0.5)

def manual_lights(robot: cozmo.robot.Robot):
    while True:
        robot.set_backpack_lights(cozmo.lights.red_light,
                                  cozmo.lights.off_light, cozmo.lights.off_light, cozmo.lights.red_light,
                                  cozmo.lights.red_light)
        time.sleep(0.5)
        robot.set_backpack_lights(cozmo.lights.off_light,
                                  cozmo.lights.blue_light, cozmo.lights.blue_light, cozmo.lights.off_light,
                                  cozmo.lights.off_light)
        time.sleep(0.5)

def cozmo_program(robot: cozmo.robot.Robot):
    manual_lights(robot)

cozmo.run_program(cozmo_program)
