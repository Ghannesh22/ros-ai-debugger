import re
from collections.abc import Iterable
from dataclasses import dataclass

from app.models import AnalysisResponse, ConfidenceLevel


@dataclass(frozen=True)
class UploadedFileContext:
    filename: str
    content: str


@dataclass(frozen=True)
class AnalyzerRule:
    category: str
    patterns: tuple[str, ...]
    summary: str
    likely_root_causes: tuple[str, ...]
    recommended_fixes: tuple[str, ...]
    verification_commands: tuple[str, ...]
    next_debugging_steps: tuple[str, ...]
    partial_patterns: tuple[str, ...] = ()
    ros_version_guess: str | None = None


@dataclass(frozen=True)
class RuleMatch:
    rule: AnalyzerRule
    confidence: ConfidenceLevel


RULES: tuple[AnalyzerRule, ...] = (
    AnalyzerRule(
        category="Python import error",
        patterns=(
            r"modulenotfounderror:\s+no module named",
            r"importerror:\s+no module named",
            r"cannot import name",
            r"pkg_resources\.distributionnotfound",
        ),
        summary="A Python module required by the ROS node appears to be missing or unavailable.",
        likely_root_causes=(
            "A Python dependency is not installed.",
            "The node is running in the wrong Python environment.",
            "The ROS workspace was not rebuilt or sourced after changes.",
            "The package layout or setup.py configuration may be incorrect.",
        ),
        recommended_fixes=(
            "Install the missing Python package in the ROS environment.",
            "Check whether the node is using python or python3 as expected.",
            "Rebuild the workspace and source the setup file.",
            "For ROS 2 Python packages, check setup.py and package layout.",
        ),
        verification_commands=(
            'python3 -c "import <module_name>"',
            "pip show <module_name>",
            "rosrun <package_name> <node>.py",
            "ros2 run <package_name> <executable_name>",
        ),
        next_debugging_steps=(
            "Find the missing module name in the traceback.",
            "Check which Python executable the ROS node is using.",
        ),
        partial_patterns=(
            r"python.+import",
            r"import.+python",
            r"missing.+python.+module",
        ),
    ),
    AnalyzerRule(
        category="TF frame missing",
        patterns=(
            r"could not find a connection between",
            r"could not transform",
            r"frame .+ does not exist",
            r"no transform from",
            r"invalid frame id",
            r"lookup would require extrapolation",
        ),
        summary="A required TF transform or frame appears to be missing.",
        likely_root_causes=(
            "A TF broadcaster is not running.",
            "A frame name is misspelled or uses the wrong namespace.",
            "A static transform is missing.",
            "The launch order may start consumers before TF publishers are ready.",
        ),
        recommended_fixes=(
            "Check the exact source and target frame names.",
            "Confirm robot_state_publisher or the expected static transform publisher is running.",
            "Inspect launch files for missing TF publishers.",
            "Check simulation time settings if the error mentions time.",
        ),
        verification_commands=(
            "rosrun tf view_frames",
            "rosrun tf tf_echo <source_frame> <target_frame>",
            "ros2 run tf2_tools view_frames",
            "ros2 run tf2_ros tf2_echo <source_frame> <target_frame>",
        ),
        next_debugging_steps=(
            "List the TF tree and confirm both frame names exist.",
            "Check whether the missing transform should be static or dynamic.",
        ),
        partial_patterns=(
            r"tf.+frame",
            r"frame.+missing",
            r"missing.+frame",
        ),
    ),
    AnalyzerRule(
        category="Gazebo plugin load error",
        patterns=(
            r"failed to load plugin",
            r"gazebo.+could not load library",
            r"could not load library.+gazebo",
            r"libgazebo_ros",
            r"gazebo.+undefined symbol",
        ),
        summary="Gazebo could not load a required ROS plugin library.",
        likely_root_causes=(
            "The Gazebo ROS plugin package is not installed.",
            "The plugin library path or filename is wrong.",
            "The workspace containing the plugin was not sourced.",
            "Gazebo and ROS plugin versions may be incompatible.",
        ),
        recommended_fixes=(
            "Install the required Gazebo ROS plugin package.",
            "Check the plugin filename in URDF, SDF, or launch files.",
            "Source the ROS and workspace setup files.",
            "Rebuild plugin packages if they are part of the workspace.",
        ),
        verification_commands=(
            "echo $GAZEBO_PLUGIN_PATH",
            "rospack find gazebo_ros",
            "ros2 pkg list | grep gazebo",
            "catkin_make",
            "colcon build",
        ),
        next_debugging_steps=(
            "Identify the exact plugin library name from the error.",
            "Check whether that library exists in the expected install path.",
        ),
        partial_patterns=(
            r"gazebo.+plugin",
            r"plugin.+gazebo",
            r"missing.+gazebo.+plugin",
        ),
    ),
    AnalyzerRule(
        category="Missing ROS package",
        patterns=(
            r"resource not found",
            r"package ['\"].+?['\"] not found",
            r"package .+ not found",
            r"packagenotfounderror",
            r"is neither a launch file in package",
        ),
        summary="A ROS package appears to be missing or unavailable to the current environment.",
        likely_root_causes=(
            "The package is not installed.",
            "The workspace was not built.",
            "The workspace setup file was not sourced.",
            "The package name may be misspelled.",
            "ROS 1 and ROS 2 commands or environments may be mixed.",
        ),
        recommended_fixes=(
            "Check the package name for spelling.",
            "Install the missing ROS package or dependency.",
            "Rebuild the workspace.",
            "Source the correct setup file for the workspace.",
        ),
        verification_commands=(
            "rospack find <package_name>",
            "roscd <package_name>",
            "ros2 pkg list",
            "ros2 pkg prefix <package_name>",
            "source devel/setup.bash",
            "source install/setup.bash",
        ),
        next_debugging_steps=(
            "Confirm whether the package should come from apt, source code, or another workspace.",
            "Check that the terminal is sourced for the right ROS distribution.",
        ),
        partial_patterns=(
            r"missing.+ros.+package",
            r"ros.+package.+missing",
            r"package.+missing",
        ),
    ),
    AnalyzerRule(
        category="Node/executable not found",
        patterns=(
            r"cannot locate node of type",
            r"node executable not found",
            r"executable ['\"].+?['\"] not found",
            r"no executable found",
            r"libexec directory does not exist",
            r"ros2 run.+no executable found",
        ),
        summary="ROS could not find the requested node or executable.",
        likely_root_causes=(
            "The node or executable name is wrong.",
            "The package was not built or installed correctly.",
            "The workspace setup file was not sourced.",
            "A Python script may be missing execute permission or install rules.",
        ),
        recommended_fixes=(
            "Check the package name and executable name.",
            "Rebuild the workspace.",
            "Source the workspace setup file.",
            "Check executable permissions and install rules for scripts.",
        ),
        verification_commands=(
            "rosrun <package_name> <executable_name>",
            "roslaunch <package_name> <launch_file>",
            "ros2 run <package_name> <executable_name>",
            "ros2 pkg executables <package_name>",
            "catkin_make",
            "colcon build",
        ),
        next_debugging_steps=(
            "List executables for the package and compare names exactly.",
            "Check CMakeLists.txt, setup.py, or launch file executable names.",
        ),
        partial_patterns=(
            r"missing.+node",
            r"node.+missing",
            r"missing.+executable",
            r"executable.+missing",
        ),
    ),
    AnalyzerRule(
        category="ROS_MASTER_URI issue",
        patterns=(
            r"unable to contact my own server",
            r"unable to communicate with master",
            r"failed to contact master",
            r"ros_master_uri",
            r"roscore not running",
            r"connection refused.+ros",
        ),
        summary="ROS 1 cannot contact the ROS master.",
        likely_root_causes=(
            "roscore is not running.",
            "ROS_MASTER_URI points to the wrong host or port.",
            "ROS_IP or ROS_HOSTNAME is misconfigured.",
            "The ROS 1 environment was not sourced in this shell.",
        ),
        recommended_fixes=(
            "Start roscore if this is a ROS 1 system.",
            "Check ROS_MASTER_URI, ROS_IP, and ROS_HOSTNAME.",
            "Source the correct ROS 1 setup file.",
            "Verify network reachability if using multiple machines.",
        ),
        verification_commands=(
            "roscore",
            "echo $ROS_MASTER_URI",
            "echo $ROS_IP",
            "echo $ROS_HOSTNAME",
            "rostopic list",
        ),
        next_debugging_steps=(
            "Confirm that roscore is running in a reachable terminal.",
            "Check that every ROS 1 shell has the same master URI settings.",
        ),
        partial_patterns=(
            r"ros.+master",
            r"master.+uri",
        ),
        ros_version_guess="ROS 1",
    ),
    AnalyzerRule(
        category="ROS 2 DDS or ROS_DOMAIN_ID issue",
        patterns=(
            r"ros_domain_id",
            r"dds.+discover",
            r"discover.+dds",
            r"rmw_implementation",
            r"fast dds",
            r"cyclone dds",
            r"nodes do not see each other",
        ),
        summary="ROS 2 discovery or domain configuration may be preventing communication.",
        likely_root_causes=(
            "Different terminals or machines use different ROS_DOMAIN_ID values.",
            "DDS discovery is blocked by the network, firewall, or VPN.",
            "Different RMW implementations are being mixed.",
            "The ROS 2 environment is not sourced consistently.",
        ),
        recommended_fixes=(
            "Use the same ROS_DOMAIN_ID in every terminal.",
            "Check RMW_IMPLEMENTATION settings.",
            "Source the same ROS 2 distribution and workspace in each shell.",
            "Test DDS discovery on one machine before debugging across machines.",
        ),
        verification_commands=(
            "echo $ROS_DOMAIN_ID",
            "echo $RMW_IMPLEMENTATION",
            "ros2 node list",
            "ros2 topic list",
            "ros2 doctor",
            "ros2 multicast receive",
            "ros2 multicast send",
        ),
        next_debugging_steps=(
            "Compare ROS_DOMAIN_ID in each terminal.",
            "Check whether firewall or VPN settings block DDS discovery.",
        ),
        partial_patterns=(
            r"domain id",
            r"dds",
            r"ros 2.+discovery",
        ),
        ros_version_guess="ROS 2",
    ),
    AnalyzerRule(
        category="catkin_make build error",
        patterns=(
            r"catkin_make.+failed",
            r"invoking [\"']?make",
            r"could not find catkin",
            r"catkin_make must be invoked",
        ),
        summary="The ROS 1 catkin workspace build appears to have failed.",
        likely_root_causes=(
            "A dependency is missing.",
            "CMakeLists.txt or package.xml has an error.",
            "catkin_make was run from the wrong directory.",
            "The ROS 1 environment was not sourced.",
        ),
        recommended_fixes=(
            "Run catkin_make from the workspace root.",
            "Fix the first CMake or compiler error in the output.",
            "Run rosdep to install missing dependencies.",
            "Source the ROS 1 setup file before building.",
        ),
        verification_commands=(
            "pwd",
            "source /opt/ros/noetic/setup.bash",
            "rosdep install --from-paths src --ignore-src -r -y",
            "catkin_make",
            "source devel/setup.bash",
        ),
        next_debugging_steps=(
            "Scroll to the first error above the final build failure line.",
            "Build again after installing dependencies and sourcing the environment.",
        ),
        partial_patterns=(
            r"catkin_make",
            r"catkin.+build",
        ),
        ros_version_guess="ROS 1",
    ),
    AnalyzerRule(
        category="colcon build error",
        patterns=(
            r"colcon build.+failed",
            r"failed <<<",
            r"summary:.+packages? finished",
            r"stderr:.+",
        ),
        summary="The ROS 2 colcon workspace build appears to have failed.",
        likely_root_causes=(
            "A dependency is missing.",
            "CMakeLists.txt, package.xml, or Python packaging has an error.",
            "The ROS 2 environment was not sourced.",
            "A specific package failed and stopped the build.",
        ),
        recommended_fixes=(
            "Source the ROS 2 setup file before building.",
            "Run rosdep to install missing dependencies.",
            "Build the failing package with direct console output.",
            "Fix the first error shown for the failed package.",
        ),
        verification_commands=(
            "source /opt/ros/humble/setup.bash",
            "rosdep install --from-paths src --ignore-src -r -y",
            "colcon build",
            "colcon build --packages-select <package_name> --event-handlers console_direct+",
            "source install/setup.bash",
        ),
        next_debugging_steps=(
            "Find the first package after the Failed <<< line.",
            "Rerun colcon for only that package with console_direct+ output.",
        ),
        partial_patterns=(r"colcon",),
        ros_version_guess="ROS 2",
    ),
)


def analyze_ros_input(
    *,
    text: str = "",
    filename: str | None = None,
    ros_version_hint: str | None = None,
    uploaded_files: list[UploadedFileContext] | None = None,
) -> AnalysisResponse:
    uploaded_files = uploaded_files or []
    related_files = _related_files(filename=filename, uploaded_files=uploaded_files)
    combined_text = _combined_text(text=text, uploaded_files=uploaded_files)
    normalized_text = _normalize_text(combined_text)

    matches = [
        rule_match
        for rule in RULES
        if (rule_match := _match_rule(rule, normalized_text)) is not None
    ]

    if not matches:
        return _unknown_response(
            normalized_text=normalized_text,
            related_files=related_files,
            ros_version_hint=ros_version_hint,
        )

    return AnalysisResponse(
        summary=_summary_for_rules([match.rule for match in matches]),
        detected_errors=[match.rule.category for match in matches],
        likely_root_causes=_dedupe(
            cause
            for match in matches
            for cause in match.rule.likely_root_causes
        ),
        recommended_fixes=_dedupe(
            fix
            for match in matches
            for fix in match.rule.recommended_fixes
        ),
        verification_commands=_dedupe(
            command
            for match in matches
            for command in match.rule.verification_commands
        ),
        confidence=_highest_confidence(match.confidence for match in matches),
        ros_version_guess=_guess_ros_version(
            normalized_text=normalized_text,
            ros_version_hint=ros_version_hint,
            matched_rules=[match.rule for match in matches],
        ),
        related_files=related_files,
        next_debugging_steps=_dedupe(
            step
            for match in matches
            for step in match.rule.next_debugging_steps
        ),
    )


def _combined_text(*, text: str, uploaded_files: list[UploadedFileContext]) -> str:
    sections = [text]
    sections.extend(file.content for file in uploaded_files)
    return "\n".join(section for section in sections if section)


def _related_files(
    *,
    filename: str | None,
    uploaded_files: list[UploadedFileContext],
) -> list[str]:
    files = []
    if filename:
        files.append(filename)
    files.extend(file.filename for file in uploaded_files)
    return _dedupe(files)


def _normalize_text(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n").lower()


def _match_rule(rule: AnalyzerRule, normalized_text: str) -> RuleMatch | None:
    if _patterns_match(rule.patterns, normalized_text):
        return RuleMatch(rule=rule, confidence="high")

    if _patterns_match(rule.partial_patterns, normalized_text):
        return RuleMatch(rule=rule, confidence="medium")

    return None


def _patterns_match(patterns: tuple[str, ...], normalized_text: str) -> bool:
    return any(
        re.search(pattern, normalized_text, flags=re.DOTALL)
        for pattern in patterns
    )


def _summary_for_rules(matched_rules: list[AnalyzerRule]) -> str:
    primary = matched_rules[0]
    if len(matched_rules) == 1:
        return primary.summary

    other_categories = ", ".join(rule.category for rule in matched_rules[1:])
    return f"{primary.summary} Also detected: {other_categories}."


def _highest_confidence(confidences: Iterable[ConfidenceLevel]) -> ConfidenceLevel:
    order = {"low": 0, "medium": 1, "high": 2}
    return max(confidences, key=lambda confidence: order[confidence])


def _guess_ros_version(
    *,
    normalized_text: str,
    ros_version_hint: str | None,
    matched_rules: list[AnalyzerRule],
) -> str:
    if ros_version_hint:
        return ros_version_hint

    for rule in matched_rules:
        if rule.ros_version_guess:
            return rule.ros_version_guess

    if any(
        signal in normalized_text
        for signal in ("ros2", "colcon", "ament", "ros_domain_id", "dds", "rclcpp")
    ):
        return "ROS 2"

    if any(
        signal in normalized_text
        for signal in (
            "roslaunch",
            "catkin_make",
            "rospack",
            "roscore",
            "ros_master_uri",
        )
    ):
        return "ROS 1"

    return "unknown"


def _unknown_response(
    *,
    normalized_text: str,
    related_files: list[str],
    ros_version_hint: str | None,
) -> AnalysisResponse:
    return AnalysisResponse(
        summary="No known ROS error pattern was detected.",
        detected_errors=[],
        likely_root_causes=[
            "The input may not include enough error detail for the current rule-based analyzer."
        ],
        recommended_fixes=[
            "Paste the full command output, including the command that was run and the first error above the final failure line."
        ],
        verification_commands=[
            "ros2 doctor",
            "ros2 topic list",
            "rostopic list",
        ],
        confidence="low",
        ros_version_guess=_guess_ros_version(
            normalized_text=normalized_text,
            ros_version_hint=ros_version_hint,
            matched_rules=[],
        ),
        related_files=related_files,
        next_debugging_steps=[
            "Include the exact ROS command that failed.",
            "Include relevant launch, package.xml, CMakeLists.txt, or log file snippets.",
            "Check whether the issue is from ROS 1, ROS 2, Gazebo, TF, or the build system.",
        ],
    )


def _dedupe(items: Iterable[str]) -> list[str]:
    result: list[str] = []
    for item in items:
        if isinstance(item, str) and item not in result:
            result.append(item)
    return result
