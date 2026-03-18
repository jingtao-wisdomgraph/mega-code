"""Historical session data loading and analysis.

This module provides a unified interface for loading coding session
data from multiple sources:

- MEGA-Code collector storage (~/.local/share/mega-code/)
- Codex CLI sessions
- Parquet datasets (ZAI CC-Bench, NLILE, etc.)

Example:
    from mega_code.client.history import create_loader, Session
    from pathlib import Path

    # Create loader with default sources
    loader = create_loader()

    # Or with custom datasets
    loader = create_loader(
        dataset_paths={
            "zai_bench": Path("datasets/zai-cc-bench/train.parquet"),
        }
    )

    # Iterate over all sessions
    for session in loader.iter_all():
        print(f"[{session.metadata.source}] {session.metadata.session_id}")
        print(f"  Messages: {len(session.messages)}")
        print(f"  Tool calls: {session.stats.tool_call_count}")

    # Load specific session
    session = loader.load_from("mega_code", "abc123-...")
"""

from mega_code.client.history.loader import (
    DataLoader,
    create_loader,
    load_session_by_id,
    load_sessions_from_project,
)
from mega_code.client.history.models import (
    HistorySessionMetadata,
    HistorySessionStats,
    Message,
    Session,
    TokenUsage,
    ToolCall,
)
from mega_code.client.history.protocol import DataSource
from mega_code.client.history.sources import (
    CodexSource,
    CursorSource,
    GeminiSource,
    MegaCodeSource,
    OpenCodeSource,
    ParquetDatasetSource,
)

__all__ = [
    # Sources
    "CodexSource",
    "CursorSource",
    "DataLoader",
    # Protocol
    "DataSource",
    "GeminiSource",
    "HistorySessionMetadata",
    "HistorySessionStats",
    "MegaCodeSource",
    # Models
    "Message",
    "OpenCodeSource",
    "ParquetDatasetSource",
    "Session",
    "TokenUsage",
    "ToolCall",
    # Main API
    "create_loader",
    "load_session_by_id",
    "load_sessions_from_project",
]
