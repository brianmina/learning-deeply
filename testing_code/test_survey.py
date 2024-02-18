from survey_class import (AnonymoushSurvey)


def test_store_single_response():
    """Test that a single response is stored prpperly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymoushSurvey(question)
    language_survey.store_response("English")
    assert "English" in language_survey.responses


def test_store_three_responses():
    """Test thatt three individual responses are store correctly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymoushSurvey(question)
    responses = ["English", "French", "Spanish"]
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses