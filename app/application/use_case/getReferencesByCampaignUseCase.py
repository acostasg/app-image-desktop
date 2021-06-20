from app.application.use_case.getReferencesByCampaignResponse import GetReferencesByCampaignResponse
from app.dominio.repository.referencesRepositoryInterface import ReferencesRepositoryInterface


class GetReferencesByCampaignUseCase:
    def __init__(self, references_repository: ReferencesRepositoryInterface):
        self.reference_repository = references_repository

    def execute(self) -> GetReferencesByCampaignResponse:
        references = self.reference_repository.all()
        return GetReferencesByCampaignResponse(references)
