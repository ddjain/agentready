"""Unit tests for LLM client factory."""

import os
from unittest.mock import patch

import pytest

from agentready.services.llm_client import create_anthropic_client


def test_create_anthropic_client_uses_api_key_when_vertex_disabled():
    """When USE_CLAUDE_VERTEX is not set, returns Anthropic client with api_key."""
    with patch.dict(os.environ, {"USE_CLAUDE_VERTEX": ""}, clear=False):
        client = create_anthropic_client(api_key="sk-test-key")
    assert client is not None
    from anthropic import Anthropic

    assert type(client).__name__ == "Anthropic"


def test_create_anthropic_client_raises_when_no_api_key_and_not_vertex():
    """When not using Vertex and api_key is missing, raises ValueError."""
    with patch.dict(os.environ, {"USE_CLAUDE_VERTEX": ""}, clear=False):
        with pytest.raises(ValueError, match="ANTHROPIC_API_KEY required"):
            create_anthropic_client(api_key=None)
    with patch.dict(os.environ, {"USE_CLAUDE_VERTEX": "0"}, clear=False):
        with pytest.raises(ValueError, match="ANTHROPIC_API_KEY required"):
            create_anthropic_client(api_key=None)


def test_create_anthropic_client_returns_vertex_when_configured():
    """When USE_CLAUDE_VERTEX=1 and Vertex env vars set, returns AnthropicVertex."""
    with patch.dict(
        os.environ,
        {
            "USE_CLAUDE_VERTEX": "1",
            "ANTHROPIC_VERTEX_PROJECT_ID": "my-gcp-project",
            "CLOUD_ML_REGION": "us-east5",
        },
        clear=False,
    ):
        client = create_anthropic_client(api_key=None)
    assert client is not None
    from anthropic import AnthropicVertex

    assert type(client).__name__ == "AnthropicVertex"


def test_create_anthropic_client_vertex_raises_without_project_id():
    """When USE_CLAUDE_VERTEX=1 but ANTHROPIC_VERTEX_PROJECT_ID missing, raises."""
    env = {"USE_CLAUDE_VERTEX": "1", "CLOUD_ML_REGION": "us-east5"}
    # Ensure project id is not set (patch.dict with clear=False keeps existing keys)
    env.pop("ANTHROPIC_VERTEX_PROJECT_ID", None)
    with patch.dict(os.environ, env, clear=False):
        # Remove in case it was set by another test or shell
        os.environ.pop("ANTHROPIC_VERTEX_PROJECT_ID", None)
        with pytest.raises(ValueError, match="ANTHROPIC_VERTEX_PROJECT_ID"):
            create_anthropic_client(api_key=None)


def test_create_anthropic_client_vertex_raises_without_region():
    """When USE_CLAUDE_VERTEX=1 but CLOUD_ML_REGION missing, raises."""
    env = {"USE_CLAUDE_VERTEX": "1", "ANTHROPIC_VERTEX_PROJECT_ID": "my-project"}
    with patch.dict(os.environ, env, clear=False):
        os.environ.pop("CLOUD_ML_REGION", None)
        with pytest.raises(ValueError, match="CLOUD_ML_REGION"):
            create_anthropic_client(api_key=None)


def test_create_anthropic_client_vertex_ignores_whitespace_in_use_vertex():
    """USE_CLAUDE_VERTEX is stripped; only '1' enables Vertex."""
    with patch.dict(
        os.environ,
        {
            "USE_CLAUDE_VERTEX": "  1  ",
            "ANTHROPIC_VERTEX_PROJECT_ID": "proj",
            "CLOUD_ML_REGION": "us-east5",
        },
        clear=False,
    ):
        client = create_anthropic_client(api_key=None)
    from anthropic import AnthropicVertex

    assert type(client).__name__ == "AnthropicVertex"
