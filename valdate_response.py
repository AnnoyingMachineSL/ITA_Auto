class ValidateResponse:

    @staticmethod
    def validate_response(response, model, status_code):
        assert response.status_code == status_code
        return model.model_validate(response.json())