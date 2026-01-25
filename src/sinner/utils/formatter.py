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
    
    @staticmethod
    def format_pr_comment(raw_output: str) -> str:
        """
        Convert prose PR/squash comments into title + bullet format.
        
        Takes verbose prose output and reformats as:
        Title sentence
        
        - Key point 1
        - Key point 2
        - Key point 3
        
        Args:
            raw_output: Raw prose from LLM
            
        Returns:
            Formatted text with title and bullets
        """
        # Clean first
        cleaned = OutputFormatter.clean_output(raw_output)
        
        # Remove any leading dash, number, or bullet
        cleaned = re.sub(r'^[-•\*\d]+\.?\s*', '', cleaned.strip())
        
        # Remove bold markdown and other formatting artifacts
        cleaned = re.sub(r'\*\*([^*]+)\*\*', r'\1', cleaned)
        cleaned = re.sub(r'__([^_]+)__', r'\1', cleaned)
        
        # Remove standalone numbers that appear as list items
        cleaned = re.sub(r'\n\d+\n', '\n', cleaned)
        cleaned = re.sub(r'\n\d+\s*-', '\n-', cleaned)
        
        # Split by sentence boundaries (period + space + capital)
        parts = re.split(r'\.\s+(?=[A-Z])', cleaned)
        parts = [p.strip() for p in parts if p.strip()]
        
        if not parts:
            return cleaned
        
        # Convert all parts to bullets
        bullets = []
        for p in parts:
            # Remove any existing list markers (1., 2., -, *, etc.)
            p = re.sub(r'^[-•\*\d]+\.?\s*', '', p)
            # Remove standalone numbers that appear on their own line
            p = re.sub(r'^\d+$', '', p)
            # Remove trailing period
            text = p.rstrip('.').strip()
            # Skip if empty, meta-text, or too short
            if text and len(text.split()) > 3 and not any(skip in text.lower() for skip in ['includes several', 'this pr', 'this pull request']):
                bullets.append(f"- {text}")
        
        # Generate simple title from first bullet
        if bullets:
            first = bullets[0].replace('- ', '').lower()
            if 'updated' in first or 'changed' in first or 'added' in first:
                title = "Updated documentation and configuration"
            elif 'fixed' in first or 'resolved' in first:
                title = "Fixed issues and improved functionality"
            elif 'merged' in first:
                title = "Merged feature branches"
            else:
                title = "Updated project configuration"
            
            return f"{title}\n\n" + "\n".join(bullets)
        
        return cleaned
