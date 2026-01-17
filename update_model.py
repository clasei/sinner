#!/usr/bin/env python3
"""Update MODEL_ID in .env file"""

import sys

if len(sys.argv) < 2:
    print("Usage: python update_model.py <model_id>")
    print("\nExample: python update_model.py qwen2.5-coder-1.5b-instruct-q4_k_m")
    sys.exit(1)

new_model = sys.argv[1]

# Read current .env
with open('.env', 'r') as f:
    lines = f.readlines()

# Update MODEL_ID line
updated_lines = []
for line in lines:
    if line.startswith('MODEL_ID='):
        updated_lines.append(f'MODEL_ID={new_model}\n')
        print(f"✓ Updated MODEL_ID to: {new_model}")
    else:
        updated_lines.append(line)

# Write back
with open('.env', 'w') as f:
    f.writelines(updated_lines)

print("\n✓ .env updated successfully!")
print("\nNow run: python test_connection.py")
