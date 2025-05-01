class ValidateResponse:

    @staticmethod
    def validate_response(response, model, status_code = None):
        if status_code!= None:
            assert response.status_code == status_code
        return model.model_validate(response.json())

    @staticmethod
    def validate_status_code(response, expected_status_code):
        assert response.status_code == expected_status_code
        return response

