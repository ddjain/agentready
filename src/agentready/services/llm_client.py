"""Factory for Anthropic / AnthropicVertex client based on environment."""

import os

from anthropic import Anthropic, AnthropicVertex


def create_anthropic_client(api_key: str | None = None) -> Anthropic | AnthropicVertex:
    """Create Anthropic or AnthropicVertex client based on env vars.

    When USE_CLAUDE_VERTEX=1: requires ANTHROPIC_VERTEX_PROJECT_ID and
    CLOUD_ML_REGION (no API key). Otherwise requires ANTHROPIC_API_KEY.

    Returns:
        Anthropic or AnthropicVertex client (same .messages.create() interface).
    """
    use_vertex = os.environ.get("USE_CLAUDE_VERTEX", "").strip()
    if use_vertex == "1":
        project_id = os.environ.get("ANTHROPIC_VERTEX_PROJECT_ID")
        region = os.environ.get("CLOUD_ML_REGION")
        if not project_id:
            raise ValueError(
                "ANTHROPIC_VERTEX_PROJECT_ID env var required when USE_CLAUDE_VERTEX=1"
            )
        if not region:
            raise ValueError(
                "CLOUD_ML_REGION env var required when USE_CLAUDE_VERTEX=1"
            )
        return AnthropicVertex(project_id=project_id, region=region)
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY required when not using Vertex")
    return Anthropic(api_key=api_key)
