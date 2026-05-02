EXPECTED_ANALYSIS_RESPONSE_FIELDS = {
    "summary",
    "detected_errors",
    "likely_root_causes",
    "recommended_fixes",
    "verification_commands",
    "confidence",
    "ros_version_guess",
    "related_files",
    "next_debugging_steps",
}


def assert_analysis_response_shape(response_body: dict[str, object]) -> None:
    assert set(response_body) == EXPECTED_ANALYSIS_RESPONSE_FIELDS
    assert isinstance(response_body["summary"], str)
    assert isinstance(response_body["detected_errors"], list)
    assert isinstance(response_body["likely_root_causes"], list)
    assert isinstance(response_body["recommended_fixes"], list)
    assert isinstance(response_body["verification_commands"], list)
    assert response_body["confidence"] in {"low", "medium", "high"}
    assert isinstance(response_body["ros_version_guess"], str)
    assert isinstance(response_body["related_files"], list)
    assert isinstance(response_body["next_debugging_steps"], list)
