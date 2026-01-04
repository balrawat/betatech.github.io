#!/usr/bin/env python3
"""
Script to improve formatting in all Jekyll posts
"""
import re
import os
import glob

def fix_post_formatting(content):
    """Fix common formatting issues in posts"""
    
    # Fix image format: [![](url)][ref] -> ![alt](url)
    content = re.sub(r'\[!\[\]\(([^)]+)\)\]\[[^\]]+\]', r'![](\1)', content)
    
    # Remove excessive blank lines (more than 2 consecutive)
    content = re.sub(r'\n\s*\n\s*\n\s*\n+', '\n\n', content)
    content = re.sub(r'  \n', '\n', content)  # Remove trailing spaces before newlines
    
    # Fix headings: **Heading**\n\n* * *\n\n -> ## Heading\n\n
    content = re.sub(r'\*\*([^*]+)\*\*\s*\n\s*\n\s*\* \* \*\s*\n\s*\n', r'## \1\n\n', content)
    
    # Fix headings without separators: **Heading**\n\n -> ## Heading\n\n
    content = re.sub(r'\*\*([^*]+)\*\*\s*\n\s*\n(?!\* \* \*)', r'## \1\n\n', content)
    
    # Fix subheadings: **Subheading**\n\n* * * -> ### Subheading\n\n
    content = re.sub(r'\*\*Step ([^*]+)\*\*\s*\n\s*\n\s*\* \* \*', r'### Step \1', content)
    content = re.sub(r'\*\*([^*]+)—([^*]+)\*\*\s*\n\s*\n\s*\* \* \*', r'### \1—\2', content)
    
    # Fix bullet points: · item -> - item
    content = re.sub(r'^·\s+', '- ', content, flags=re.MULTILINE)
    content = re.sub(r'^\\-\s+', '- ', content, flags=re.MULTILINE)
    
    # Fix single-line code: _command_ -> `command` (only if it looks like code)
    # Pattern: standalone italic text that's likely code
    def fix_inline_code(match):
        text = match.group(1)
        # If it contains common code patterns, convert to code
        if any(x in text for x in ['/', 'sudo', 'yum', 'apt', 'vi ', 'nano ', 'mkdir', 'chmod', 'chown', 'cd ', 'wget', 'curl', 'echo', 'grep', 'cat', 'ls ', 'ps ', 'kill', 'service', 'systemctl']):
            return f'`{text}`'
        return match.group(0)
    
    content = re.sub(r'_([^_\n]+)_', fix_inline_code, content)
    
    # Fix multi-line code blocks (italic HTML/config blocks)
    # Pattern: Multiple lines starting with _ and ending with _
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Check if this looks like start of italic code block
        if stripped.startswith('_') and stripped.endswith('_') and ('<' in stripped or any(cmd in stripped for cmd in ['sudo', 'yum', 'apt', 'vi', 'nano', 'mkdir', 'chmod', 'chown', 'cd', 'wget', 'curl', 'echo', 'grep', 'cat', 'ls', 'ps', 'kill', 'service', 'systemctl', '#', '/etc/', '/var/', 'Protocol', 'Listen', 'VirtualHost', 'ServerAdmin', 'DocumentRoot', 'ServerName'])):
            # Collect consecutive italic lines
            code_lines = []
            lang = 'bash'
            if '<' in stripped:
                lang = 'html'
            elif 'VirtualHost' in stripped or 'ServerAdmin' in stripped:
                lang = 'apache'
            
            j = i
            while j < len(lines) and lines[j].strip().startswith('_') and lines[j].strip().endswith('_'):
                code_line = lines[j].strip().strip('_')
                code_lines.append(code_line)
                j += 1
            
            if len(code_lines) > 1 or (len(code_lines) == 1 and len(code_lines[0]) > 20):
                # It's a code block
                result.append('```' + lang)
                result.extend(code_lines)
                result.append('```')
                i = j
                continue
        
        result.append(line)
        i += 1
    
    content = '\n'.join(result)
    
    # Clean up any remaining excessive blank lines
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    return content

def process_all_posts():
    """Process all markdown files in _posts directory"""
    posts_dir = '_posts'
    if not os.path.exists(posts_dir):
        print(f"Directory {posts_dir} not found!")
        return
    
    md_files = glob.glob(os.path.join(posts_dir, '*.md'))
    print(f"Found {len(md_files)} markdown files")
    
    fixed_count = 0
    for filepath in sorted(md_files):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if already processed (has proper markdown headings)
            if '## ' in content and not re.search(r'\*\*[^*]+\*\*\s*\n\s*\n\s*\* \* \*', content):
                continue
            
            original_content = content
            fixed_content = fix_post_formatting(content)
            
            if fixed_content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                fixed_count += 1
                print(f"Fixed: {os.path.basename(filepath)}")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
    
    print(f"\nFixed {fixed_count} files")

if __name__ == '__main__':
    process_all_posts()

