import asyncio
import logging
import os
import uvloop

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from strawberry.fastapi import GraphQLRouter

from server.mission_manager import mission_manager_schema

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def start_webserver() -> None:
    """Initializes FastAPI webserver with route to ground_station_telemetry"""
    logging.info("Starting webserver")
    app = FastAPI()
    # app.include_router(GraphQLRouter(mission_manager_schema), prefix="/mission_manager")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.mount('/', StaticFiles(directory='/build', html=True), name='mission manager')
    port = int(os.environ.get("PORT", 3000))
    config = uvicorn.Config(app, port=port, host="0.0.0.0")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(start_webserver())
