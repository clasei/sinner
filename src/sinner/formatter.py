import re

class OutputFormatter:
    @staticmethod
    def clean_output(raw_output: str) -> str:
        # Remove emojis
        cleaned_output = re.sub(r'[\U0001F600-\U0001F64F]|[\U0001F300-\U0001F5FF]|[\U0001F680-\U0001F6FF]|[\U0001F700-\U0001F77F]|[\U0001F800-\U0001F8FF]|[\U0001F900-\U0001F9FF]|[\U0001FA00-\U0001FAFF]|[\U00002700-\U000027BF]', '', raw_output)
        # Remove excessive markdown
        cleaned_output = re.sub(r'\*\*|\*|__|_|`', '', cleaned_output)
        # Strip whitespace
        cleaned_output = ' '.join(cleaned_output.split())
        return cleaned_output
