from langgraph_sdk import Auth
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

auth = Auth()

@auth.authenticate
async def authenticate(request, path, headers, method):
    logger.info("authenticate function called")
    user_agent = headers.get(b"user-agent")
    logger.info(f"User-Agent: {user_agent}")
    if user_agent and user_agent.startswith(b"Slackbot"):
        logger.info("Slackbot identified; authentication successful")
        return {"identity": "default-user", "permissions": ["read", "write"]}
    logger.warning("Authentication failed; User-Agent not recognized")
    return None