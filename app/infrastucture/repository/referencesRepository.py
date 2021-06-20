from app.dominio.repository.referencesRepositoryInterface import ReferencesRepositoryInterface
from app.infrastucture.schema.referenceSchema import ReferenceSchema
import requests
from app.main import config


class ReferencesRepository(ReferencesRepositoryInterface):
    def all(self) -> list:
        try:
            response = requests.get(config.get('api.host') + config.get('api.endpoints.references'))
            if response.status_code == 200:
                list_references = []
                for item in response.json():
                    list_references.append(ReferenceSchema().load(item))

                return list_references
        except:
            print("Error connection for api")

        return []
