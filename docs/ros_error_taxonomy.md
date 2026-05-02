# ROS Error Taxonomy

## 1. Purpose Of The Taxonomy

This file defines the first ROS error categories that ROS AI Debugger should detect in MVP 1.

The taxonomy helps the analyzer by giving it a clear list of:

- Error patterns to look for.
- Likely root causes.
- Beginner-friendly fixes.
- Verification commands.
- Confidence rules.
- Expected structured output.

The MVP 1 analyzer should use this file as the starting point for rule-based detection. It should not try to fully understand every ROS system. It should detect common text patterns and return practical next debugging steps.

## 2. Error Category Template

Each category uses this format:

- Category name
- ROS version relevance: ROS 1, ROS 2, or both
- Common error messages
- Typical root causes
- Suggested fixes
- Verification commands
- Confidence rules
- Example input
- Expected analyzer output

Expected analyzer output should map to the backend response fields:

- `summary`
- `detected_errors`
- `likely_root_causes`
- `recommended_fixes`
- `verification_commands`
- `confidence`
- `ros_version_guess`
- `related_files`
- `next_debugging_steps`

## 3. MVP 1 Error Categories

### 3.1 Missing ROS Package

- Category name: Missing ROS package
- ROS version relevance: both
- Common error messages:
  - `Resource not found`
  - `package '<name>' not found`
  - `Package '<name>' not found`
  - `ament_index_python.packages.PackageNotFoundError`
  - `RLException: [<file>] is neither a launch file in package`
- Typical root causes:
  - The package is not installed.
  - The workspace was not built.
  - The workspace setup file was not sourced.
  - The package name is misspelled.
  - The user is mixing ROS 1 and ROS 2 commands.
- Suggested fixes:
  - Check the package name for spelling.
  - Install the missing package if it is an external dependency.
  - Rebuild the workspace.
  - Source the correct workspace setup file.
  - Use ROS 1 commands for ROS 1 packages and ROS 2 commands for ROS 2 packages.
- Verification commands:
  - `rospack find <package_name>`
  - `roscd <package_name>`
  - `ros2 pkg list`
  - `ros2 pkg prefix <package_name>`
  - `source devel/setup.bash`
  - `source install/setup.bash`
- Confidence rules:
  - High: Message includes `package not found`, `Resource not found`, or `PackageNotFoundError` with a package name.
  - Medium: Message mentions a launch file or executable in a package that cannot be located.
  - Low: Input only mentions a package name without a clear missing-package phrase.
- Example input:

```text
Package 'my_robot_bringup' not found: "package 'my_robot_bringup' not found"
```

- Expected analyzer output:
  - `summary`: ROS package `my_robot_bringup` could not be found.
  - `detected_errors`: Missing ROS package.
  - `likely_root_causes`: Package missing, workspace not sourced, workspace not built, or package name typo.
  - `recommended_fixes`: Check package name, build workspace, source setup file, install dependency.
  - `confidence`: high
  - `ros_version_guess`: ROS 2 if `ros2` or `ament` appears, ROS 1 if `roslaunch` or `rospack` appears, otherwise unknown.

### 3.2 Missing Dependency

- Category name: Missing dependency
- ROS version relevance: both
- Common error messages:
  - `Could not find a package configuration file provided by`
  - `Could not find the required component`
  - `Failed to find package`
  - `No module named <module>`
  - `cannot find -l<library>`
  - `rosdep` missing dependency output
- Typical root causes:
  - A system dependency is not installed.
  - A ROS dependency is missing from the environment.
  - `rosdep install` was not run.
  - `package.xml` does not declare the dependency.
  - `CMakeLists.txt` does not find or link the dependency.
- Suggested fixes:
  - Run `rosdep install` for the workspace.
  - Install the missing ROS package or system library.
  - Add the dependency to `package.xml`.
  - Add the dependency to `CMakeLists.txt` when needed.
  - Rebuild the workspace after installing dependencies.
- Verification commands:
  - `rosdep install --from-paths src --ignore-src -r -y`
  - `apt-cache search <dependency_name>`
  - `rospack find <dependency_name>`
  - `ros2 pkg list`
  - `catkin_make`
  - `colcon build`
- Confidence rules:
  - High: Error includes `Could not find`, `required component`, `No module named`, or `cannot find -l`.
  - Medium: Build output names a dependency and fails during configuration or linking.
  - Low: Dependency is mentioned but no direct missing-dependency phrase appears.
- Example input:

```text
CMake Error at CMakeLists.txt:10 (find_package):
  Could not find a package configuration file provided by "tf2_ros"
```

- Expected analyzer output:
  - `summary`: Dependency `tf2_ros` appears to be missing or unavailable to the workspace.
  - `detected_errors`: Missing dependency.
  - `likely_root_causes`: Dependency not installed, not declared, or workspace environment not sourced.
  - `recommended_fixes`: Run rosdep, install dependency, update package metadata, rebuild.
  - `confidence`: high

### 3.3 Node/Executable Not Found

- Category name: Node/executable not found
- ROS version relevance: both
- Common error messages:
  - `Cannot locate node of type`
  - `Node executable not found`
  - `executable '<name>' not found`
  - `No executable found`
  - `libexec directory does not exist`
  - `ros2 run: No executable found`
- Typical root causes:
  - The node executable name is wrong.
  - The package was not built.
  - The workspace setup file was not sourced.
  - Python script is not installed correctly.
  - Python script is missing executable permission.
  - `CMakeLists.txt` or `setup.py` does not install the executable.
- Suggested fixes:
  - Check the package and executable names.
  - Rebuild the workspace.
  - Source the workspace setup file.
  - Check install rules for Python or C++ executables.
  - Check executable permission for ROS 1 Python scripts.
- Verification commands:
  - `rosrun <package_name> <executable_name>`
  - `roslaunch <package_name> <launch_file>`
  - `ros2 run <package_name> <executable_name>`
  - `ros2 pkg executables <package_name>`
  - `catkin_make`
  - `colcon build`
- Confidence rules:
  - High: Error says executable or node cannot be found.
  - Medium: Launch fails and mentions a node type or executable name.
  - Low: Input only shows a node name without a direct not-found message.
- Example input:

```text
ERROR: cannot launch node of type [my_robot/talker.py]: Cannot locate node of type [talker.py] in package [my_robot]
```

- Expected analyzer output:
  - `summary`: ROS could not find the requested node executable.
  - `detected_errors`: Node/executable not found.
  - `likely_root_causes`: Wrong executable name, missing build/install step, unsourced workspace, or missing execute permission.
  - `recommended_fixes`: Verify executable name, rebuild, source setup file, check install rules and permissions.
  - `confidence`: high

### 3.4 Wrong Topic Name Or Remapping Issue

- Category name: Wrong topic name or remapping issue
- ROS version relevance: both
- Common error messages:
  - `WARNING: no messages received`
  - `topic does not appear to be published`
  - `unknown topic`
  - `Could not find topic`
  - Symptoms where publisher and subscriber use different topic names.
- Typical root causes:
  - Publisher and subscriber use different topic names.
  - Remapping in the launch file is wrong.
  - Namespace changes the actual topic path.
  - ROS 1 and ROS 2 topic tools are mixed.
  - Node did not start, so the topic is never published.
- Suggested fixes:
  - List active topics.
  - Compare expected topic name with actual topic name.
  - Check launch remappings and namespaces.
  - Confirm the publisher node is running.
  - Use fully qualified topic names when debugging.
- Verification commands:
  - `rostopic list`
  - `rostopic echo /topic_name`
  - `rostopic info /topic_name`
  - `ros2 topic list`
  - `ros2 topic echo /topic_name`
  - `ros2 topic info /topic_name`
- Confidence rules:
  - High: Input includes topic-not-published text plus a topic name.
  - Medium: Input includes remap or namespace lines and topic communication symptoms.
  - Low: Input mentions a topic but no failure phrase.
- Example input:

```text
WARNING: no messages received and simulated time is active.
Is /cmd_vel being published?
```

- Expected analyzer output:
  - `summary`: The expected topic may not be published or may be remapped to a different name.
  - `detected_errors`: Wrong topic name or remapping issue.
  - `likely_root_causes`: Publisher not running, wrong topic name, namespace issue, or launch remap mismatch.
  - `recommended_fixes`: List topics, inspect remappings, confirm publisher node, test echo command.
  - `confidence`: medium

### 3.5 Launch File Syntax Error

- Category name: Launch file syntax error
- ROS version relevance: both
- Common error messages:
  - `Invalid roslaunch XML syntax`
  - `RLException: Invalid <param> tag`
  - `XML parse error`
  - `mismatched tag`
  - `InvalidFrontendLaunchFileError`
  - `SyntaxError` in a Python ROS 2 launch file
- Typical root causes:
  - Broken XML in ROS 1 launch files.
  - Invalid Python syntax in ROS 2 launch files.
  - Missing closing tag or quote.
  - Invalid launch tag or argument.
  - Wrong file type for the launch command.
- Suggested fixes:
  - Validate XML syntax for `.launch` files.
  - Check Python syntax for ROS 2 `.launch.py` files.
  - Review recently edited launch tags, parameters, and substitutions.
  - Use the correct launch command for ROS 1 or ROS 2.
- Verification commands:
  - `roslaunch <package_name> <launch_file>`
  - `roslaunch-check <launch_file>`
  - `python -m py_compile <launch_file>.py`
  - `ros2 launch <package_name> <launch_file>.py`
- Confidence rules:
  - High: Error includes XML parse, invalid launch file, mismatched tag, or Python launch syntax.
  - Medium: Error references a launch file and line number.
  - Low: Input only includes launch file content with no syntax error.
- Example input:

```text
RLException: Invalid roslaunch XML syntax: mismatched tag: line 12, column 2
```

- Expected analyzer output:
  - `summary`: The launch file appears to have a syntax error.
  - `detected_errors`: Launch file syntax error.
  - `likely_root_causes`: Broken XML tag, missing quote, invalid launch field, or Python syntax error.
  - `recommended_fixes`: Inspect the reported line, validate syntax, rerun launch command.
  - `confidence`: high

### 3.6 Missing Executable Permission

- Category name: Missing executable permission
- ROS version relevance: mostly ROS 1, sometimes both
- Common error messages:
  - `Permission denied`
  - `Couldn't find executable named`
  - `Cannot locate node of type`
  - Python node exists but cannot be run.
- Typical root causes:
  - Python script does not have execute permission.
  - Script has no shebang line.
  - Script is not installed as an executable.
  - Windows-created file was copied into Linux/WSL without execute permission.
- Suggested fixes:
  - Add execute permission in the ROS/Linux environment.
  - Add a valid Python shebang.
  - Check install rules for scripts.
  - Rebuild and source the workspace.
- Verification commands:
  - `ls -l scripts/<node>.py`
  - `chmod +x scripts/<node>.py`
  - `head -n 1 scripts/<node>.py`
  - `rosrun <package_name> <node>.py`
- Confidence rules:
  - High: Error includes `Permission denied` for a `.py` node.
  - Medium: Node cannot be located and input references a Python script.
  - Low: Input only contains a Python file path without permission error.
- Example input:

```text
/home/user/catkin_ws/src/my_robot/scripts/talker.py: Permission denied
```

- Expected analyzer output:
  - `summary`: The Python node may not be executable.
  - `detected_errors`: Missing executable permission.
  - `likely_root_causes`: Missing execute bit, missing shebang, or missing install rule.
  - `recommended_fixes`: Add execute permission, check shebang, rebuild and source workspace.
  - `confidence`: high

### 3.7 `catkin_make` Build Error

- Category name: catkin_make build error
- ROS version relevance: ROS 1
- Common error messages:
  - `catkin_make` failed
  - `Invoking "make" failed`
  - `Could not find catkin`
  - `The specified base path ... contains a package but "catkin_make" must be invoked`
  - CMake errors during catkin configure or build.
- Typical root causes:
  - Missing dependency.
  - Invalid `CMakeLists.txt`.
  - Invalid `package.xml`.
  - Command run from the wrong directory.
  - ROS 1 environment not sourced.
- Suggested fixes:
  - Run `catkin_make` from the workspace root.
  - Source the ROS 1 environment.
  - Install dependencies with `rosdep`.
  - Fix the first CMake error in the output.
  - Clean and rebuild if needed.
- Verification commands:
  - `pwd`
  - `source /opt/ros/noetic/setup.bash`
  - `rosdep install --from-paths src --ignore-src -r -y`
  - `catkin_make`
  - `source devel/setup.bash`
- Confidence rules:
  - High: Input includes `catkin_make` and `Invoking "make" failed`.
  - Medium: Input includes catkin CMake errors without the final failure line.
  - Low: Input mentions catkin but no build failure.
- Example input:

```text
Base path: /home/user/catkin_ws
Invoking "make -j8 -l8" failed
```

- Expected analyzer output:
  - `summary`: The ROS 1 catkin workspace build failed.
  - `detected_errors`: catkin_make build error.
  - `likely_root_causes`: Missing dependency, CMake issue, package metadata issue, or wrong environment.
  - `recommended_fixes`: Inspect first CMake error, run rosdep, source ROS setup, rebuild.
  - `confidence`: high

### 3.8 `colcon` Build Error

- Category name: colcon build error
- ROS version relevance: ROS 2
- Common error messages:
  - `colcon build` failed
  - `Failed <<< <package_name>`
  - `Summary: 0 packages finished`
  - `stderr: <package_name>`
  - CMake or Python packaging errors during colcon build.
- Typical root causes:
  - Missing dependency.
  - Invalid `CMakeLists.txt`.
  - Invalid `package.xml`.
  - Python packaging issue.
  - ROS 2 environment not sourced.
- Suggested fixes:
  - Source the ROS 2 environment.
  - Run `rosdep install`.
  - Build one failing package with more console output.
  - Fix the first error shown for the failed package.
  - Source `install/setup.bash` after a successful build.
- Verification commands:
  - `source /opt/ros/humble/setup.bash`
  - `rosdep install --from-paths src --ignore-src -r -y`
  - `colcon build`
  - `colcon build --packages-select <package_name> --event-handlers console_direct+`
  - `source install/setup.bash`
- Confidence rules:
  - High: Input includes `colcon build` and `Failed <<<`.
  - Medium: Input includes ROS 2 package build output and CMake/Python errors.
  - Low: Input mentions colcon but no failure.
- Example input:

```text
Starting >>> my_robot
Failed <<< my_robot [2.31s, exited with code 1]
```

- Expected analyzer output:
  - `summary`: A ROS 2 colcon build failed for package `my_robot`.
  - `detected_errors`: colcon build error.
  - `likely_root_causes`: Missing dependency, package config issue, CMake issue, or Python packaging issue.
  - `recommended_fixes`: Inspect first package error, run rosdep, build selected package, source environment.
  - `confidence`: high

### 3.9 `CMakeLists.txt` Issue

- Category name: CMakeLists.txt issue
- ROS version relevance: both
- Common error messages:
  - `CMake Error at CMakeLists.txt`
  - `Unknown CMake command`
  - `Target ... links to target ... but the target was not found`
  - `Cannot specify link libraries for target`
  - `add_executable` or `install` problems.
- Typical root causes:
  - Missing `find_package`.
  - Wrong target name.
  - Missing install rule.
  - Dependency not linked.
  - ROS 1 catkin and ROS 2 ament patterns are mixed.
- Suggested fixes:
  - Inspect the CMake line number in the error.
  - Add or correct `find_package`.
  - Check target names.
  - Add missing install rules.
  - Keep catkin and ament CMake patterns separate.
- Verification commands:
  - `catkin_make`
  - `colcon build`
  - `colcon build --packages-select <package_name> --event-handlers console_direct+`
  - `grep -n "find_package\\|add_executable\\|install" CMakeLists.txt`
- Confidence rules:
  - High: Error explicitly references `CMakeLists.txt`.
  - Medium: Build output contains CMake errors without a file line.
  - Low: Input includes CMake content but no failing message.
- Example input:

```text
CMake Error at CMakeLists.txt:22 (target_link_libraries):
  Cannot specify link libraries for target "talker" which is not built by this project.
```

- Expected analyzer output:
  - `summary`: The build is failing because of a `CMakeLists.txt` target configuration issue.
  - `detected_errors`: CMakeLists.txt issue.
  - `likely_root_causes`: Wrong target name, missing executable target, or incorrect link rule.
  - `recommended_fixes`: Check target names and CMake line number, fix target definition, rebuild.
  - `confidence`: high

### 3.10 `package.xml` Dependency Issue

- Category name: package.xml dependency issue
- ROS version relevance: both
- Common error messages:
  - `package.xml`
  - `The manifest contains invalid XML`
  - `Invalid package manifest`
  - `Package format`
  - Missing dependency found by build or rosdep.
- Typical root causes:
  - Dependency missing from `package.xml`.
  - Invalid XML syntax.
  - Wrong package format for ROS version.
  - Package name mismatch.
  - Build tool dependency is missing.
- Suggested fixes:
  - Validate `package.xml` syntax.
  - Add missing dependencies.
  - Check package name consistency.
  - Use correct ROS 1 or ROS 2 build tool tags.
  - Rerun dependency installation and rebuild.
- Verification commands:
  - `catkin_make`
  - `colcon build`
  - `rosdep check --from-paths src --ignore-src`
  - `rosdep install --from-paths src --ignore-src -r -y`
  - `xmllint --noout package.xml`
- Confidence rules:
  - High: Error directly says package manifest or `package.xml` is invalid.
  - Medium: Missing dependency appears and `package.xml` content is available.
  - Low: `package.xml` is uploaded but no dependency or syntax error is present.
- Example input:

```text
Error(s) in package '/home/user/ws/src/my_robot/package.xml':
The manifest contains invalid XML: mismatched tag
```

- Expected analyzer output:
  - `summary`: The package manifest has an XML or dependency problem.
  - `detected_errors`: package.xml dependency issue.
  - `likely_root_causes`: Invalid XML, missing dependency, wrong package format, or package name mismatch.
  - `recommended_fixes`: Validate XML, fix tags, add dependencies, run rosdep, rebuild.
  - `confidence`: high

### 3.11 TF Frame Missing

- Category name: TF frame missing
- ROS version relevance: both
- Common error messages:
  - `Frame <frame> does not exist`
  - `Could not transform`
  - `Lookup would require extrapolation`
  - `Invalid frame ID`
  - `No transform from <frame_a> to <frame_b>`
- Typical root causes:
  - A TF broadcaster is not running.
  - Frame name is misspelled.
  - Static transform is missing.
  - Launch order prevents transform from being available.
  - Simulation or robot state publisher is not publishing expected frames.
- Suggested fixes:
  - List the TF tree.
  - Check frame names exactly.
  - Confirm `robot_state_publisher` or static transform publisher is running.
  - Check launch files for missing TF publishers.
  - Check whether simulation time is configured correctly.
- Verification commands:
  - `rosrun tf view_frames`
  - `rosrun tf tf_echo <source_frame> <target_frame>`
  - `ros2 run tf2_tools view_frames`
  - `ros2 run tf2_ros tf2_echo <source_frame> <target_frame>`
  - `ros2 topic echo /tf`
- Confidence rules:
  - High: Error includes missing frame or no transform between named frames.
  - Medium: Input includes TF lookup or transform warnings.
  - Low: Input mentions frame names without a TF failure.
- Example input:

```text
Could not transform from [base_link] to [map]. Frame [map] does not exist.
```

- Expected analyzer output:
  - `summary`: A required TF frame is missing.
  - `detected_errors`: TF frame missing.
  - `likely_root_causes`: Missing TF broadcaster, wrong frame name, missing static transform, or launch order issue.
  - `recommended_fixes`: Inspect TF tree, check frame names, start required publisher, verify transform.
  - `confidence`: high

### 3.12 Parameter Not Found

- Category name: Parameter not found
- ROS version relevance: both
- Common error messages:
  - `Parameter not set`
  - `ParameterNotDeclaredException`
  - `parameter '<name>' is not set`
  - `KeyError` for a parameter name
  - `Could not find parameter`
- Typical root causes:
  - Parameter was not loaded.
  - YAML file path is wrong.
  - Parameter name or namespace is wrong.
  - ROS 2 parameter was not declared.
  - Launch file does not pass the parameter file.
- Suggested fixes:
  - Check parameter name and namespace.
  - Confirm YAML file is loaded.
  - Inspect launch file parameter configuration.
  - Declare ROS 2 parameters if required.
  - List parameters at runtime.
- Verification commands:
  - `rosparam list`
  - `rosparam get /parameter_name`
  - `ros2 param list`
  - `ros2 param get <node_name> <parameter_name>`
  - `ros2 param dump <node_name>`
- Confidence rules:
  - High: Error directly says parameter is missing, unset, or undeclared.
  - Medium: Input includes YAML and launch parameter loading warnings.
  - Low: Parameter is mentioned but no failure phrase appears.
- Example input:

```text
rclcpp::exceptions::ParameterNotDeclaredException: parameter 'robot_description' has not been declared
```

- Expected analyzer output:
  - `summary`: A required ROS parameter is missing or undeclared.
  - `detected_errors`: Parameter not found.
  - `likely_root_causes`: Parameter not loaded, wrong namespace, wrong YAML path, or ROS 2 declaration issue.
  - `recommended_fixes`: Check launch parameters, load YAML, declare parameter, list runtime parameters.
  - `confidence`: high

### 3.13 Gazebo Plugin Load Error

- Category name: Gazebo plugin load error
- ROS version relevance: both
- Common error messages:
  - `Failed to load plugin`
  - `Could not load library`
  - `libgazebo_ros`
  - `undefined symbol`
  - `GazeboRosFactory`
  - `SystemPaths.cc`
- Typical root causes:
  - Gazebo plugin package is not installed.
  - Plugin library path is wrong.
  - Plugin name is wrong in URDF, SDF, or launch file.
  - Gazebo and ROS plugin versions are incompatible.
  - Workspace was not sourced.
- Suggested fixes:
  - Install the required Gazebo ROS plugin package.
  - Check plugin filename and path.
  - Source the workspace and ROS environment.
  - Check `GAZEBO_PLUGIN_PATH`.
  - Rebuild plugin packages.
- Verification commands:
  - `echo $GAZEBO_PLUGIN_PATH`
  - `ros2 pkg list | grep gazebo`
  - `rospack find gazebo_ros`
  - `colcon build`
  - `catkin_make`
- Confidence rules:
  - High: Error includes `Failed to load plugin` or `Could not load library` with Gazebo context.
  - Medium: Input mentions Gazebo plugin library warnings.
  - Low: Input mentions Gazebo but no plugin load failure.
- Example input:

```text
[Err] [Plugin.hh:178] Failed to load plugin libgazebo_ros_diff_drive.so: libgazebo_ros_diff_drive.so: cannot open shared object file
```

- Expected analyzer output:
  - `summary`: Gazebo could not load a required plugin library.
  - `detected_errors`: Gazebo plugin load error.
  - `likely_root_causes`: Missing plugin package, wrong plugin path, wrong library name, or unsourced workspace.
  - `recommended_fixes`: Install plugin package, check plugin path/name, source environment, rebuild.
  - `confidence`: high

### 3.14 Python Import Error

- Category name: Python import error
- ROS version relevance: both
- Common error messages:
  - `ModuleNotFoundError: No module named`
  - `ImportError: No module named`
  - `cannot import name`
  - `pkg_resources.DistributionNotFound`
  - Python traceback during node startup.
- Typical root causes:
  - Python dependency is not installed.
  - Wrong Python environment is active.
  - ROS package is not installed correctly.
  - `setup.py` or package layout is wrong.
  - Workspace setup file was not sourced.
- Suggested fixes:
  - Install the missing Python dependency.
  - Check virtual environment and ROS Python version.
  - Rebuild and source the workspace.
  - Check `setup.py` for ROS 2 Python packages.
  - Check package imports and module names.
- Verification commands:
  - `python -c "import <module_name>"`
  - `python3 -c "import <module_name>"`
  - `pip show <module_name>`
  - `rosrun <package_name> <node>.py`
  - `ros2 run <package_name> <executable_name>`
- Confidence rules:
  - High: Python traceback includes `ModuleNotFoundError` or `ImportError`.
  - Medium: Node crashes during Python startup and module names are shown.
  - Low: Input mentions Python file but no import failure.
- Example input:

```text
ModuleNotFoundError: No module named 'serial'
```

- Expected analyzer output:
  - `summary`: A Python module required by the ROS node is missing.
  - `detected_errors`: Python import error.
  - `likely_root_causes`: Missing Python package, wrong environment, unsourced workspace, or package layout issue.
  - `recommended_fixes`: Install module, check Python environment, rebuild/source workspace, test import manually.
  - `confidence`: high

### 3.15 `ROS_MASTER_URI` Issue

- Category name: ROS_MASTER_URI issue
- ROS version relevance: ROS 1
- Common error messages:
  - `Unable to communicate with master`
  - `Failed to contact master`
  - `roscore` not running
  - `Connection refused`
  - `ROS_MASTER_URI`
- Typical root causes:
  - `roscore` is not running.
  - `ROS_MASTER_URI` points to the wrong host or port.
  - Network hostname or IP configuration is wrong.
  - ROS 1 environment variables are not set.
  - User is trying ROS 1 networking commands in the wrong shell.
- Suggested fixes:
  - Start `roscore`.
  - Check `ROS_MASTER_URI`.
  - Check `ROS_HOSTNAME` or `ROS_IP`.
  - Confirm machines can reach each other on the network.
  - Source the correct ROS 1 setup file.
- Verification commands:
  - `roscore`
  - `echo $ROS_MASTER_URI`
  - `echo $ROS_IP`
  - `echo $ROS_HOSTNAME`
  - `rostopic list`
- Confidence rules:
  - High: Error mentions ROS master, `roscore`, or `ROS_MASTER_URI`.
  - Medium: ROS 1 command fails with connection refused.
  - Low: Input mentions ROS networking but no master connection failure.
- Example input:

```text
ERROR: Unable to communicate with master!
```

- Expected analyzer output:
  - `summary`: ROS 1 cannot contact the ROS master.
  - `detected_errors`: ROS_MASTER_URI issue.
  - `likely_root_causes`: `roscore` not running, wrong master URI, or network environment mismatch.
  - `recommended_fixes`: Start roscore, check environment variables, source ROS setup, verify network.
  - `confidence`: high
  - `ros_version_guess`: ROS 1

### 3.16 ROS 2 DDS Or `ROS_DOMAIN_ID` Issue

- Category name: ROS 2 DDS or ROS_DOMAIN_ID issue
- ROS version relevance: ROS 2
- Common error messages:
  - Nodes do not see each other.
  - Topics are missing even though nodes are running.
  - `ROS_DOMAIN_ID`
  - DDS participant or discovery warnings.
  - Fast DDS, Cyclone DDS, or RMW implementation warnings.
- Typical root causes:
  - Different terminals or machines use different `ROS_DOMAIN_ID` values.
  - DDS discovery is blocked by network configuration.
  - Different RMW implementations are being mixed.
  - ROS 2 environment is not sourced consistently.
  - Firewall or VPN blocks discovery traffic.
- Suggested fixes:
  - Check `ROS_DOMAIN_ID` in every terminal.
  - Use the same ROS 2 distribution and setup environment.
  - Check `RMW_IMPLEMENTATION`.
  - Test discovery on one machine first.
  - Check firewall, VPN, or network restrictions.
- Verification commands:
  - `echo $ROS_DOMAIN_ID`
  - `echo $RMW_IMPLEMENTATION`
  - `ros2 node list`
  - `ros2 topic list`
  - `ros2 doctor`
  - `ros2 multicast receive`
  - `ros2 multicast send`
- Confidence rules:
  - High: Input mentions `ROS_DOMAIN_ID`, DDS discovery, or RMW warnings.
  - Medium: ROS 2 nodes run but topics/nodes are not visible.
  - Low: Input says communication failed but does not mention ROS 2 or DDS clues.
- Example input:

```text
ros2 topic list does not show /camera/image even though the camera node is running in another terminal.
ROS_DOMAIN_ID=7 in one terminal and ROS_DOMAIN_ID=0 in another.
```

- Expected analyzer output:
  - `summary`: ROS 2 discovery may be split by different domain IDs.
  - `detected_errors`: ROS 2 DDS or ROS_DOMAIN_ID issue.
  - `likely_root_causes`: Different `ROS_DOMAIN_ID`, DDS discovery problem, RMW mismatch, or network blocking.
  - `recommended_fixes`: Match domain IDs, check RMW, source same ROS environment, test multicast.
  - `confidence`: high
  - `ros_version_guess`: ROS 2

## 4. Detection Strategy

The MVP 1 analyzer should detect errors using several simple signals together.

Keywords:

- Look for strong phrases such as `package not found`, `No module named`, `Failed to load plugin`, `Unable to communicate with master`, or `ParameterNotDeclaredException`.

Patterns:

- Use regular expressions for package names, node names, frame names, file paths, and command output.
- Prefer patterns that capture useful names, such as the missing package or missing Python module.

File names:

- Use filenames as context.
- `package.xml` should increase confidence for package metadata and dependency issues.
- `CMakeLists.txt` should increase confidence for CMake and build issues.
- `.launch`, `.launch.py`, `.yaml`, `.py`, and `.cpp` files should guide the analyzer toward relevant categories.

Command context:

- `roslaunch`, `catkin_make`, `rospack`, and `roscore` suggest ROS 1.
- `ros2`, `colcon`, `ament`, and `rclcpp` suggest ROS 2.
- `gazebo`, `gzserver`, and plugin library names suggest Gazebo.
- `tf`, `tf2`, `base_link`, `map`, and transform language suggest TF/frame issues.

Multiple signals:

- The analyzer should combine signals instead of using one keyword alone.
- For example, `Failed <<< my_robot` plus `colcon build` is stronger than `Failed` by itself.

## 5. Prioritization Rules

When multiple patterns match, the analyzer should choose the most likely issue using these rules:

1. Prefer direct error messages over general context.

   Example: `ModuleNotFoundError` should classify as Python import error even if the file is also a launch log.

2. Prefer specific categories over broad build categories.

   Example: If `catkin_make` fails because `Could not find tf2_ros`, classify missing dependency first and catkin build error second.

3. Use command context to choose ROS version.

   Example: `colcon build` should increase ROS 2 confidence. `catkin_make` should increase ROS 1 confidence.

4. Use file context to raise confidence.

   Example: A dependency error plus `package.xml` content should raise confidence for package metadata issues.

5. Return multiple detected errors when useful.

   Example: A failed `colcon build` caused by a `CMakeLists.txt` error can include both categories, with the CMake issue as the more specific root cause.

6. Avoid overconfident answers.

   Example: If the input only says "node cannot talk to another node" without logs or commands, return low confidence and suggest next debugging steps.

Recommended priority order when several categories match:

1. Python import error, launch syntax error, TF frame missing, Gazebo plugin load error, or parameter not found when their direct phrases appear.
2. Missing package or missing dependency when direct missing-package/dependency phrases appear.
3. CMakeLists.txt or package.xml issues when file-specific errors appear.
4. Node/executable not found.
5. ROS_MASTER_URI or ROS 2 DDS/domain issues.
6. Broad catkin_make or colcon build error.
7. Wrong topic/remapping issue when evidence is mostly behavioral.

## 6. Limitations

MVP 1 will not fully understand every ROS system.

Important limitations:

- It does not run ROS commands.
- It does not inspect a live ROS graph.
- It does not connect to robot hardware.
- It does not parse rosbags.
- It does not guarantee that the first suggested fix is correct.
- It may miss uncommon error formats.
- It may return multiple possible causes when the input is incomplete.

The analyzer should be honest about uncertainty. When evidence is weak, it should return lower confidence and give clear next debugging steps instead of pretending the diagnosis is certain.
