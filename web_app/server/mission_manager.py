import json
import shutil
from typing import List, Optional, Dict, Any

import strawberry
from strawberry.file_uploads import Upload


@strawberry.type
class MissionManagerQuery:
    @strawberry.field
    async def hello(self) -> str:
        return 'world'

@strawberry.type
class Response:
    id: str
    name: str
    files: List[str]


@strawberry.type
class MissionManagerMutation:
    @strawberry.mutation
    async def create_mission_plan(
            self, id: str, name: str, files: List[Upload]) -> Response:
        results = []
        for file in files:
            file_contents = (await file.read()).decode("utf-8")
            results.append(file_contents)
        print(id, name, results)
        return Response(id, name, results)
     
        
mission_manager_schema = strawberry.Schema(
    query=MissionManagerQuery, mutation=MissionManagerMutation)
