"""Base reporter interface for generating assessment reports."""

from abc import ABC, abstractmethod
from pathlib import Path

from ..models.assessment import Assessment


class BaseReporter(ABC):
    """Abstract base class for all report generators.

    Reporters transform Assessment data into different output formats
    (HTML, Markdown, PDF, etc.) for human consumption.
    """

    @abstractmethod
    def generate(self, assessment: Assessment, output_path: Path) -> Path:
        """Generate report from assessment data.

        Args:
            assessment: Complete assessment with findings
            output_path: Path where report should be saved

        Returns:
            Path to generated report file

        Raises:
            IOError: If report cannot be written
        """
        pass
