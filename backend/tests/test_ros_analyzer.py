import pytest

from app.services import analyze_ros_input


@pytest.mark.parametrize(
    ("text", "expected_category", "expected_ros_version"),
    [
        (
            "Resource not found: my_robot_bringup",
            "Missing ROS package",
            "unknown",
        ),
        (
            "Cannot locate node of type [talker.py] in package [my_robot]",
            "Node/executable not found",
            "unknown",
        ),
        (
            "ModuleNotFoundError: No module named 'serial'",
            "Python import error",
            "unknown",
        ),
        (
            "Could not find a connection between 'map' and 'base_link'",
            "TF frame missing",
            "unknown",
        ),
        (
            "Failed to load plugin libgazebo_ros_diff_drive.so",
            "Gazebo plugin load error",
            "unknown",
        ),
        (
            'catkin_make failed: Invoking "make" failed',
            "catkin_make build error",
            "ROS 1",
        ),
        (
            "colcon build failed. Failed <<< my_robot",
            "colcon build error",
            "ROS 2",
        ),
        (
            "ERROR: Unable to contact my own server. Check ROS_MASTER_URI.",
            "ROS_MASTER_URI issue",
            "ROS 1",
        ),
        (
            "ROS_DOMAIN_ID differs and DDS discovery cannot find nodes.",
            "ROS 2 DDS or ROS_DOMAIN_ID issue",
            "ROS 2",
        ),
    ],
)
def test_ros_analyzer_detects_mvp_rules(
    text: str,
    expected_category: str,
    expected_ros_version: str,
) -> None:
    response = analyze_ros_input(text=text)

    assert expected_category in response.detected_errors
    assert response.confidence == "high"
    assert response.ros_version_guess == expected_ros_version
    assert response.likely_root_causes
    assert response.recommended_fixes
    assert response.verification_commands
    assert response.next_debugging_steps


def test_ros_analyzer_returns_low_confidence_for_unknown_input() -> None:
    response = analyze_ros_input(text="The robot acts strangely after startup.")

    assert response.summary == "No known ROS error pattern was detected."
    assert response.detected_errors == []
    assert response.confidence == "low"
    assert response.ros_version_guess == "unknown"
    assert response.likely_root_causes
    assert response.recommended_fixes
    assert response.verification_commands
    assert response.next_debugging_steps
