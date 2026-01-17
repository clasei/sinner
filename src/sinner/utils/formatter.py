"""
Output formatter for cleaning LLM responses.
Removes emojis and excessive markdown.
"""

import re


class OutputFormatter:
    """Clean and format LLM output for professional use."""
    
    @staticmethod
    def clean_output(raw_output: str) -> str:
        """
        Clean output by removing emojis and excessive markdown.
        
        Args:
            raw_output: Raw text from LLM
            
        Returns:
            Cleaned text ready for paste
        """
        # Remove emojis
        cleaned = re.sub(
            r'[\U0001F600-\U0001F64F]|[\U0001F300-\U0001F5FF]|'
            r'[\U0001F680-\U0001F6FF]|[\U0001F700-\U0001F77F]|'
            r'[\U0001F800-\U0001F8FF]|[\U0001F900-\U0001F9FF]|'
            r'[\U0001FA00-\U0001FAFF]|[\U00002700-\U000027BF]',
            '',
            raw_output
        )
        
        # Remove excessive markdown (but keep basic formatting)
        # Only remove bold/italic markers, keep structure
        cleaned = re.sub(r'\*\*\*', '', cleaned)  # Remove triple asterisks
        
        # Strip excessive whitespace but preserve paragraph breaks
        lines = [line.strip() for line in cleaned.split('\n')]
        cleaned = '\n'.join(line for line in lines if line)
        
        return cleaned.strip()
